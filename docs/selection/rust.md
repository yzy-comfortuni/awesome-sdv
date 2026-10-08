# 车载 Rust：工具链、任务调度与调试怎么选

[资源目录](../../README.md#rust) · [选型笔记](README.md) · ComfortUni（适宇科技）及贡献者

资料查阅：2026-10-08。以下特性来自各条所附官方资料；起步检查是本清单提出的评估方法，尚非本仓库的硬件实测结果。

## 先分清要替换哪一层

| 工程问题 | 优先阅读 |
| --- | --- |
| 传感器驱动要在不同 MCU 间复用 | [embedded-hal](#embedded-hal) |
| 多路外设等待、通信与定时任务难以组织 | [Embassy](#embassy)、[RTIC](#rtic)；二者都涉及异步任务，不能按“异步 / 非异步”二分 |
| 已有 C++ 工程，只准备改写一部分 | [CXX](#cxx)；先确定跨语言接口和构建链 |
| 需要车规目标支持或安全开发材料 | [HighTec](#hightec)、[Ferrocene](#ferrocene)；编译目标、库和工具鉴定分别核对 |
| 需要烧录、断点或压缩日志 | [probe-rs](#probe-rs)、[defmt](#defmt)；二者不是编译器 |

<a id="embedded-hal"></a>
## embedded-hal：复用外设驱动，不是替你适配芯片

传感器驱动依赖 SPI、I²C、GPIO 等 traits，具体 MCU 的 HAL 实现这些接口。同一个驱动由此可以换底层实现，而不把寄存器地址写进业务代码。1.0 主 crate 提供阻塞接口；异步接口在 `embedded-hal-async`，CAN 和字节流接口另在 `embedded-can`、`embedded-io`。这一拆分比笼统的“硬件抽象层”更影响依赖选择。[API 与 companion crates](https://docs.rs/embedded-hal/latest/embedded_hal/) · [1.0 设计说明](https://blog.rust-embedded.org/embedded-hal-v1/)

开始移植时，先对齐驱动与芯片 HAL 使用的 trait 版本，再选一个实际外设检查总线共享、错误返回和超时处理。使用相同 trait 不会自动补齐 DMA、时钟树或芯片专有外设。与 RTIC、Embassy 的关系是接口与调度层的组合，不是三选一。

<a id="embassy"></a>
## Embassy：把等待写成异步流程

Embassy 适合由外设完成事件推动的任务：等待串口、等待定时器、等待输入变化。执行器静态分配任务，不要求堆；任务让出执行后，其他任务才有机会在同一执行器上运行。多个不同优先级执行器可以实现抢占，因此不能把 Embassy 简化为“完全没有抢占”。[官方 Book：执行器与任务](https://embassy.dev/book/)

先在目标芯片的官方示例上同时运行周期任务和一次外设传输，记录响应延迟及 RAM 占用。再在任务中加入实际计算负载：长时间不让出的计算会拖住同一执行器的其他任务。选型要看任务怎样让出、在哪个优先级运行，而不只是源码里有没有 `async`。

<a id="rtic"></a>
## RTIC：显式描述任务优先级和共享资源

RTIC 利用中断控制器进行静态优先级调度，以 Stack Resource Policy 管理共享资源。v2 的软件任务也使用异步执行器；它与 Embassy 的关键比较点是任务与资源模型、优先级组织及目标支持，不是是否支持 `async`。官方模型围绕单核应用展开，不能直接推成多核资源共享方案。[RTIC v2：模型与 SRP](https://rtic.rs/2/book/en/)

从两个优先级任务争用同一资源的例子开始，检查临界区长度以及高优先级任务受阻时间。响应时间分析还需要实际执行时间和中断负载；语言对资源访问的约束本身不会给出项目的最坏执行时间。

<a id="probe-rs"></a>
## probe-rs：把烧录、运行和故障信息接进开发流程

probe-rs 通过调试探针执行烧录、内存访问、断点与复位，也能读取 RTT/defmt 日志。它并不限于 Rust 固件。当前概览明确列出 Arm 与 RISC-V；采购车规芯片前，应核对具体 target 和探针，而不是从“支持 Rust”推断支持 RH850 或 TriCore。[能力与架构范围](https://probe.rs/docs/overview/about-probe-rs/)

第一项检查是识别真实探针和芯片，随后烧录最小固件、停在一个断点并取得一次故障堆栈。把“可以下载镜像”“可以源码调试”“可以读取日志”分开验收；三者并不总在同一目标上同时可用。

<a id="defmt"></a>
## defmt：少传字符串，但要保留对应的解码材料

defmt 把格式字符串放入编译期字典，设备输出索引和参数，主机再还原可读日志。它仍需 RTT、ITM 等传输实现；当前文档要求 ELF 输出和相应链接配置。日志编码、传输和主机解码是三件事。[原理、限制与传输组件](https://defmt.ferrous-systems.com/)

归档日志时同时保留产生该日志的 ELF、构建标识和解码器版本。起步检查不只是“终端出现文字”，还应离线解码保存的日志，并在打开、关闭日志时比较任务时序。不要把 MCU 压缩日志当成已经建立了整车日志检索系统。

<a id="cxx"></a>
## CXX：给既有 C++ 模块增加受约束的 Rust 接口

CXX 从桥接声明生成两侧代码并检查边界类型，提供字符串、向量、智能指针等常见类型的映射。适合逐步迁移已有模块，减少手写 C 风格 FFI；它不是任意 C++ 头文件的自动转换器，也不会验证 C++ 函数体内部行为。[机制与可运行教程入口](https://cxx.rs/)

先选一个无硬件依赖的小接口，确定缓冲区所有权、对象销毁位置和错误传递方式，再接入目标交叉编译链。主机示例通过后，还要检查目标的 C++ ABI、链接和运行库配置；不要用桌面上的一次调用替代车端接入验收。

<a id="ferrocene"></a>
## Ferrocene：选的是具体工具链发行与适用范围

Ferrocene 的价值在于工具链与配套安全开发材料。公开源码和文档可查，但二进制发行、维护与支持是另一个取得路径。官方把编译器、目标平台、工具和库的范围分开说明，不能把一个目标的资格扩展到全部 Cargo 依赖。[产品与交付](https://ferrocene.dev/en) · [文档入口](https://public-docs.ferrocene.dev/)

评估时列出“宿主系统 → 目标三元组 → 编译器发行 → 运行库 → 第三方 crate”，要求交付材料逐项对应。公开文档的 `main` 页面带开发分支预览提示，适合了解文档结构，不应拿预览中的范围当采购版本承诺。[目标分类](https://public-docs.ferrocene.dev/main/user-manual/targets/index.html) · [资格范围](https://public-docs.ferrocene.dev/main/qualification/evaluation-plan/qualification-scope.html)

<a id="hightec"></a>
## HighTec Rust：从车规芯片与既有 C/C++ 工程出发

HighTec 的产品资料明确面向 AURIX、Stellar，并强调 Rust 与既有 C/C++ 工程的混合开发。与通用嵌入式框架相比，先看的是目标编译器、ABI、多核工程及厂商交付，而不是应用调度 API。[Rust Development Platform](https://hightec-rt.com/products/rust-development-platform)

拿自己的芯片型号和一个现有 C/C++ 静态库做评估：调用一个 Rust 函数，再返回到既有代码，核对启动、链接映射、调试符号及库依赖。报价时把芯片支持、编译器版本、调试器和所需安全材料列成独立项目；品牌名相同不等于所有目标与材料一并包含。

---

文档采用 [CC BY 4.0](../../LICENSE)，署名与来源见 [ATTRIBUTION.md](../../ATTRIBUTION.md)。
