# 软件定义汽车入门：技术栈、术语与工具入口

[Awesome SDV](../README.md) · ComfortUni（适宇科技）及贡献者

这篇导读帮助第一次接触 SDV 的读者找到资料，也方便工程师按问题查找已有分类。项目详情以 [完整清单](../README.md#contents) 及其上游文档为准。

<a id="what-is-sdv"></a>
## 软件定义汽车（SDV）是什么？

软件定义汽车（Software-Defined Vehicle，SDV）强调用可持续开发、部署和更新的软件组织车辆功能。它涉及基础软件、通信、车辆服务、应用和开发验证，不只指自动驾驶或座舱界面。可从 [Eclipse SDV](https://eclipsesdv.org/about/) 的项目分工和 [SOAFEE](https://www.soafee.io/) 的车云开发思路开始阅读。

在这份清单中，可以沿着“[平台](../README.md#platforms) → [通信](../README.md#middleware) → [车辆数据](../README.md#vehicle-data) → [验证](../README.md#simulation) → [更新](../README.md#ota)”梳理软件栈。这是阅读顺序，不要求将这些项目组合成一套系统。

<a id="autosar"></a>
## AUTOSAR 与 SDV 是什么关系？

SDV 是车辆软件的整体方向，AUTOSAR 提供其中的基础软件架构与接口规范。Classic 与 Adaptive 的规范、供应商实现和 ARXML 配置工具是不同交付物，应该分开查找。具体入口见 [AUTOSAR Classic](https://www.autosar.org/standards/classic-platform)、[Adaptive](https://www.autosar.org/standards/adaptive-platform) 和本清单的 [AUTOSAR 分类](../README.md#autosar)。

<a id="communication"></a>
## DDS、SOME/IP 和 VSS 怎么区分？

[DDS](https://www.omg.org/spec/DDS/) 规定数据分发与服务质量策略；[SOME/IP 实现](https://github.com/COVESA/vsomeip) 处理服务发现、请求响应和事件通信；[VSS](https://github.com/COVESA/vehicle_signal_specification) 规定车辆信号名称、结构与语义。数据模型和通信机制不是同一层的替代选项。

查找 RTI Connext Drive、Cyclone DDS、Fast DDS、RustDDS 或 Dust DDS，请看 [DDS 与配套工具](../README.md#dds)。查找 vsomeip、CommonAPI 或共享内存通信，请看 [SOME/IP 与进程间通信](../README.md#middleware)。

<a id="rust"></a>
## 车载 Rust 从哪里开始？

先用 [The Embedded Rust Book](https://docs.rust-embedded.org/book/) 理解裸机程序、外设访问和中断，再按工程问题查找硬件抽象、任务调度、调试及 C/C++ 接口。完整入口在 [Rust 与嵌入式开发](../README.md#rust)。

清单把 Ferrocene、HighTec 等工具链与 Embassy、RTIC、probe-rs 等开发组件分列；不要只凭编程语言选择整套车规软件方案。芯片支持和安全相关工具材料应回到对应项目文档确认。

<a id="chinese-tools"></a>
## 国产汽车软件和测试工具在哪里？

按工作内容找，比按公司名浏览全部产品更直接：

| 工作内容 | 清单中的入口 |
| --- | --- |
| 总线分析、诊断和测试 | [同星 TSMaster、致远 ZXDoc、经纬恒润 INTEWORK-VBA](../README.md#bus-tools) |
| ECU 基础软件与配置 | [NeuSAR、INTEWORK-EAS、ORIENTAIS](../README.md#autosar)，以及 [EasyXMen、RT-Thread](../README.md#mcu) |
| 建模与仿真 | [MWORKS.Sysplorer](../README.md#modeling) 与 [INTEWORK-TAE](../README.md#simulation) |

每个条目链接到对应厂商或项目资料。这里提供查找入口，不宣称同一分类内的产品功能、硬件兼容性或价格相同。

<a id="reuse"></a>
## 可以把这份清单放进培训材料、网站或知识库吗？

可以。文档按 CC BY 4.0 开放，允许商业使用、翻译和改编。公开传播受许可保护的内容时保留 ComfortUni（适宇科技）及贡献者的署名、来源与许可信息，并说明改动。可直接使用 [转载署名示例](../ATTRIBUTION.md#examples)。所链接的软件和标准有各自许可，清单的授权不替代上游授权。

<a id="glossary"></a>
## 术语速查

| 术语 | 全称、含义与相关分类 |
| --- | --- |
| SDV | Software-Defined Vehicle，软件定义汽车；[架构与生态](../README.md#ecosystem) |
| ECU / MCU | Electronic Control Unit / Microcontroller Unit，电子控制单元 / 微控制器；[MCU 与实时系统](../README.md#mcu) |
| RTOS | Real-Time Operating System，实时操作系统；[MCU 与实时系统](../README.md#mcu) |
| AUTOSAR / BSW | Automotive Open System Architecture / Basic Software，汽车开放系统架构 / 基础软件；[AUTOSAR](../README.md#autosar) |
| DDS | Data Distribution Service，数据分发服务；[DDS](../README.md#dds) |
| SOME/IP | Scalable service-Oriented MiddlewarE over IP，面向服务的 IP 中间件；[通信实现](../README.md#middleware) |
| IPC | Inter-Process Communication，进程间通信；[共享内存与 IPC](../README.md#middleware) |
| VSS | Vehicle Signal Specification，车辆信号规范；[车辆数据](../README.md#vehicle-data) |
| CAN / CAN FD | Controller Area Network / CAN with Flexible Data-Rate；[总线与网络](../README.md#networks) |
| UDS / DoIP | Unified Diagnostic Services / Diagnostics over Internet Protocol；[诊断](../README.md#diagnostics) |
| SIL / HIL | Software-in-the-Loop / Hardware-in-the-Loop，软件在环 / 硬件在环；[虚拟 ECU 与测试](../README.md#simulation) |
| OTA / SBOM | Over-the-Air / Software Bill of Materials，空中更新 / 软件物料清单；[更新](../README.md#ota)与[供应链](../README.md#supply-chain) |

---

由 ComfortUni（适宇科技）及贡献者整理。文档采用 [CC BY 4.0](../LICENSE)，来源与署名方式见 [ATTRIBUTION.md](../ATTRIBUTION.md)。
