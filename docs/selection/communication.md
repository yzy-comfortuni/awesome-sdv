# 车辆通信：DDS、SOME/IP、共享内存与信号服务

[资源目录](../../README.md#dds) · [选型笔记](README.md) · ComfortUni（适宇科技）及贡献者

资料查阅：2026-10-08。产品特性附官方来源；建议的测试步骤尚未作为本仓库实测执行。

## 先确定通信发生在哪里

| 需求 | 比较对象 |
| --- | --- |
| 接入已有 SOME/IP 服务与服务发现配置 | [vsomeip](#vsomeip) |
| 跨进程、跨主机发布订阅，并约定 QoS | [Connext Drive](#rti)、[Cyclone DDS](#cyclone)、[Fast DDS](#fast-dds) |
| Rust 原生应用接 DDS | [RustDDS](#rustdds)、[Dust DDS](#dust-dds)；逐项比较 API、类型生成和所需 QoS |
| 资源受限设备接入 DDS 网络 | [Micro XRCE-DDS](#micro-xrce)；将 Agent 部署也计入设计 |
| 同机大块数据传递 | [iceoryx2](#iceoryx2)，或评估 DDS 的同机通路；不要把共享内存当成跨主机协议 |
| 应用按车辆信号名称访问数据 | [VSS](#vss) 定义模型，[Kuksa](#kuksa) 提供服务；仍需底层采集适配 |

<a id="vsomeip"></a>
## vsomeip：接服务通信，不替你定义业务数据

vsomeip 分别提供 SOME/IP、配置、服务发现与 E2E 相关库。与 DDS 比较前，应先确认对端是否已经固定 SOME/IP 的服务、实例和方法标识；已有协议合同往往比中间件偏好更重要。CommonAPI 的接口生成与绑定另有项目，不能仅安装 vsomeip 就得到完整业务接口。[上游 README](https://github.com/COVESA/vsomeip) · [CommonAPI SOME/IP 运行时](https://github.com/COVESA/capicxx-someip-runtime)

先让一对客户端与服务端完成服务发现和一次请求响应，再换成真实网络与对端类型定义。分别检查标识、网络配置、载荷编码及服务端重启后的恢复。源码编译成功只能排除构建问题，不能替代这些协议层检查。

<a id="iceoryx2"></a>
## iceoryx2：关注样本所有权和慢消费者

iceoryx2 的共享内存 API 允许借出样本、写入后发送，再由订阅者接收。它适合评估同一主机上的数据复制成本；跨主机通信应另行设计。选型时应看样本生命周期、队列和发送策略，而不是只摘录“零拷贝”的性能宣传。[API、示例与配置](https://docs.rs/iceoryx2/latest/iceoryx2/)

先用发布订阅示例传固定大小的数据，然后故意减慢一个订阅者，检查可借用样本耗尽时的行为以及内存上限。部署在容器中时，也要核对进程实际能否访问同一组共享内存对象。与 DDS 的比较应限定为同机数据通路，不把两者全部功能混成一个吞吐量排名。

<a id="rti"></a>
## RTI Connext Drive：看汽车集成包，不只看 DDS 核心

Connext Drive 提供面向汽车开发的 DDS 产品及 AUTOSAR 等集成支持。需要供应商承担平台适配或提供对应材料时，应把集成代码、目标支持和支持服务作为交付物检查，而不是只比较一次 HelloWorld。[产品范围](https://www.rti.com/products/connext-drive)

评估先取得适用版本，再让目标设备与既有对端按实际类型和 QoS 通信。采购清单应明确开发席位、目标发行、所需集成组件与材料；没有对应交付证据时，不给“量产级”或认证范围打分。性能另用 [Perftest](#perftest) 建立同条件基线，不能拿厂商另一套硬件的数字直接横比。

<a id="cyclone"></a>
## Cyclone DDS：把类型定义和通信链先跑清楚

Cyclone DDS 的官方 HelloWorld 从类型定义、发布者和订阅者展开，适合建立一套较小的 DDS 功能验证起点。它与 Fast DDS 的比较首先应覆盖相同数据类型、QoS 和网络条件，而不是 README 长度或 Star 数。[HelloWorld 教程](https://cyclonedds.io/docs/cyclonedds/latest/getting_started/helloworld/helloworld.html)

先运行同版本教程，再做两台主机之间的数据交换。之后逐项加入真实报文尺寸、订阅者数量和重启情景；每次只改变一个条件，保存类型文件及配置。单机自动发现正常后，仍可能在多网卡、路由或受限组播网络上遇到另一类问题。

<a id="fast-dds"></a>
## Fast DDS：三种“少复制”路径要分开

Fast DDS 的 Shared Memory Transport 与 Data-sharing 不相同：前者仍涉及 history 与传输层之间的复制，后者共享数据历史；应用与中间件之间的复制还需另看 Zero-Copy API。当前 Data-sharing 文档列出共享内存可达、有界且无 key 的类型、特定内存模式以及不启用安全插件等约束。[Data-sharing 原理与约束](https://fast-dds.docs.eprosima.com/en/latest/fastdds/transport/datasharing.html)

评估同机大数据时，先固定 topic 类型与历史深度，再分别测试普通传输、共享内存传输和 Data-sharing。记录实际启用的通路、内存占用及慢消费者下的写入行为。类型含无界字段、key 或需要安全插件时，不能沿用另一种配置的零拷贝结论。

<a id="rustdds"></a>
## RustDDS：采用 Rust 风格 API，ROS 2 另有入口

RustDDS 追求功能兼容，同时采用更符合 Rust 的 API，不照搬 DDS 的对象接口。官方说明：接 ROS 2 应使用单独的 `ros2-client`，不要继续使用库中旧的 `ros2` 模块。这是会直接影响新项目依赖选择的信息。[RustDDS API 与 ROS 2 说明](https://docs.rs/rustdds/latest/rustdds/index.html)

先判断项目需要裸 DDS，还是 ROS 2 节点能力，再选择对应例子。拿一个真实消息类型与既有对端测试发现、可靠性、历史深度和大消息；不要从“能够与 ROS 2 通信”推导全部 DDS QoS、语言映射或安全扩展都已覆盖。

<a id="dust-dds"></a>
## Dust DDS：关心标准接口与 IDL 到 Rust 的路径

Dust DDS 文档提供同步与异步 API、IDL 类型生成和 Shapes 示例。与 RustDDS 相比，值得直接检查的是团队更偏好哪种 API、现有 IDL 能否导入、对端类型与 QoS 能否配合；两个项目都用 Rust 不是足够的选型依据。[API、IDL 与 Shapes](https://docs.rs/dust_dds/latest/dust_dds/)

先用官方 Shapes 示例观察发现和数据交换，再换成自己的 IDL；包含 key、嵌套类型或可变长度数据时单独留样。不要把演示通过写成全部 DDS 规范一致性验证，也不要把同步与异步两个 API 当成两种不同线协议。

<a id="micro-xrce"></a>
## Micro XRCE-DDS：小客户端加 Agent，不是 MCU 上直接塞完整 DDS

Micro XRCE-DDS 由资源受限端的 Client 和另一端的 Agent 配合，Agent 代表客户端与 DDS 网络交互。这样拆分了部署位置，也引入会话、连接恢复和 Agent 的资源管理问题。[官方架构与教程入口](https://micro-xrce-dds.docs.eprosima.com/en/latest/)

先确定 Agent 在哪台设备运行，再评估客户端传输、缓冲区和可靠性配置。起步测试除正常收发外，还应包括 Agent 重启、客户端重连和链路中断后恢复。不要把 Client 的资源占用单独当作整个方案成本，也不要直接套用完整 DDS 节点的发现模型。

<a id="perftest"></a>
## RTI Perftest：先读清楚延迟的定义

Perftest 同时测量吞吐和给定负载下的延迟。发布端周期性请求回显，以往返时间 RTT 计算 `RTT/2` 作为单向延迟估计；这不是两端同步时钟下直接测得的单向链路时间。它可针对 Connext 的不同产品构建，并不是所有 DDS 实现直接共享的一套可执行程序。[测试方法与构建对象](https://community.rti.com/static/documentation/perftest/current/introduction.html)

比较时保存样本尺寸、速率、可靠性、history、batching、传输方式、线程配置及原始输出。将空载 ping-pong 与带吞吐负载的延迟分开看。链路不对称时，`RTT/2` 不能揭示哪个方向更慢；需要直接单向测量时，应另外设计时钟与时间戳方案。

<a id="vss"></a>
## VSS：统一信号语义，不提供采集和传输

VSS 组织信号名称、树结构、类型与语义。它解决应用侧“这个值叫什么、表示什么”的问题，不负责从 CAN 取数，也不决定如何写到执行器。适合多个应用或车型需要共同信号模型的场景。[VSS 文档](https://covesa.github.io/vehicle_signal_specification/) · [Kuksa 对模型与采集职责的说明](https://github.com/eclipse-kuksa/kuksa-databroker)

先选一个已有信号，把 DBC 中的原始值、比例、偏移和单位映射到所选 VSS 版本，再与 ECU 实际值对照。映射规则和定制扩展应随版本保存。改了名字却没有核对物理意义，仍然会让应用读到错误的数。

<a id="kuksa"></a>
## Kuksa Databroker：信号服务与总线适配分开部署

Databroker 为 VSS 信号提供 gRPC 访问，Provider 在 ECU 通信和高层信号之间做转换。当前上游同时描述 VAL v2 与已弃用的 v1，而其 README 中的部分 CLI 示例仍走 v1；服务端启动成功不代表随手选一个客户端就能调用相同 API。[架构、API 与示例](https://github.com/eclipse-kuksa/kuksa-databroker) · [用户指南](https://github.com/eclipse-kuksa/kuksa-databroker/blob/main/doc/user_guide.md)

先对齐服务端、客户端和 `.proto` 版本，在隔离环境中完成一个信号的写入与订阅，再接 Provider。官方快速示例关闭了 TLS 和访问控制，接入共享网络前应按用户指南配置。执行器目标值的写入也应与实际反馈值分别验证，不能把数据库更新视为执行器已动作。

---

文档采用 [CC BY 4.0](../../LICENSE)，署名与来源见 [ATTRIBUTION.md](../../ATTRIBUTION.md)。
