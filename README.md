# Awesome SDV · 软件定义汽车资源指南

软件定义汽车（Software-Defined Vehicle，SDV）的开源项目、商业工具、标准和技术资料。覆盖 AUTOSAR、车载 Rust、DDS / SOME/IP、CAN 工具、虚拟 ECU、SIL/HIL 与 OTA。

由 [ComfortUni（适宇科技）](https://www.comfortuni.com/) 发起和维护，欢迎社区共同整理。按工程用途查找资源，每条提供中文说明和上游链接。

[English](README.en.md) · [入门与术语](docs/START_HERE.md) · [选型笔记](docs/selection/README.md) · [分类目录](#contents) · [转载与署名](ATTRIBUTION.md)

<a id="start"></a>
## 你要找什么？

| 正在做的事 | 从这里进入 |
| --- | --- |
| 初次了解 SDV，梳理技术栈 | [SDV 入门](docs/START_HERE.md) → [架构与生态](#ecosystem) → [车载操作系统](#platforms) |
| 开发 MCU、区域控制器或车载 Rust | [MCU 与实时系统](#mcu) · [Rust 工具链](#rust) · [AUTOSAR](#autosar) · [隔离与虚拟化](#virtualization) |
| 查找 RTI DDS、SOME/IP 或车辆信号接口 | [DDS 实现与工具](#dds) · [SOME/IP 与 IPC](#middleware) · [VSS 与车辆数据](#vehicle-data) |
| 查找同星、致远、恒润等国产工具 | [TSMaster、ZXDoc、INTEWORK-VBA](#bus-tools) · [国产基础软件](#autosar) · [建模与代码生成](#modeling) |
| 建立诊断、标定和软件测试环境 | [UDS、DoIP、XCP 与测量](#diagnostics) · [虚拟 ECU 与 SIL/HIL](#simulation) · [调试与代码分析](#verification) |
| 组织车端部署、更新与软件交付 | [编排与车云协同](#orchestration) · [OTA](#ota) · [安全启动](#secure-boot) · [软件供应链](#supply-chain) |

<a id="contents"></a>
## 分类目录

**系统平台：** [架构与生态](#ecosystem) · [车载操作系统](#platforms) · [MCU 与实时系统](#mcu) · [隔离与虚拟化](#virtualization)

**语言与应用：** [Rust 与嵌入式开发](#rust) · [AUTOSAR 与基础软件](#autosar) · [车辆数据与应用接口](#vehicle-data) · [座舱与 HMI](#hmi)

**网络与通信：** [SOME/IP 与 IPC](#middleware) · [DDS 与配套工具](#dds) · [CAN、以太网与时间同步](#networks) · [总线分析与测试工具](#bus-tools)

**开发与验证：** [诊断、测量与标定](#diagnostics) · [建模与代码生成](#modeling) · [虚拟 ECU 与 SIL/HIL](#simulation) · [调试、代码分析与时序验证](#verification)

**部署与交付：** [OTA 与软件更新](#ota) · [安全启动与可信执行](#secure-boot) · [车端编排与车云协同](#orchestration) · [构建与软件供应链](#supply-chain) · [功能安全与开发规范](#safety)

**相邻专题：** [自动驾驶与场景仿真](#adas) · [电池与充电](#ev) · [相关清单](#related)

<a id="commercial"></a>
**标签：** 开源 / 商业 / 标准 / 文档 / 生态 / 清单。

来源与访问限制见 [补充记录](docs/REVIEW.md)。

<!-- catalog:start -->

<a id="ecosystem"></a>
## 架构与生态

- [Eclipse SDV](https://eclipsesdv.org/projects/) — **生态**。汽车软件项目目录，包含运行时、车辆服务、开发工具和集成示例。
- [SOAFEE](https://www.soafee.io/) — **生态**。连接云端开发与车端部署的汽车软件架构协作项目。
- [Eclipse SDV Blueprints](https://github.com/eclipse-sdv-blueprints/blueprints) — **开源**。按应用场景组织的集成示例，展示多个 SDV 项目如何配合。
- [ASAM Standards](https://www.asam.net/standards/) — **标准**。测量、标定、诊断和仿真规范目录，包括 XCP、MDF、ODX、XIL 与 OpenX 系列。

<a id="platforms"></a>
## 车载操作系统与集成平台

- [Eclipse S-CORE](https://github.com/eclipse-score/score) — **开源**。面向车载高性能 ECU 的基础软件栈，包含平台组件、集成方式和安全工程资料。
- [Eclipse Leda](https://github.com/eclipse-leda/leda) — **开源**。集成车辆应用和管理组件的嵌入式 Linux 发行版。
- [Automotive Grade Linux](https://docs.automotivelinux.org/) — **文档**。AGL 的系统构建、平台配置和应用开发文档。
- [Android Automotive OS：SDV](https://source.android.com/docs/automotive/sdv) — **文档**。AOSP 的车辆服务、虚拟化与多节点架构资料。AAOS 是车载系统，不是手机投屏的 Android Auto。
- [EWAOL](https://meta-ewaol.docs.soafee.io/en/latest/introduction.html) — **文档**。SOAFEE 的边缘工作负载参考环境，介绍 Yocto、容器编排和虚拟化的集成。
- [Eclipse Automotive Integration for AutoSD](https://projects.eclipse.org/projects/automotive.autosd) — **开源**。在 AutoSD 镜像中集成和测试 Eclipse SDV 组件与 Blueprints。
- [QNX Software Development Platform](https://qnx.software/en/software/products-and-solutions/qnx-software-development-platform) — **商业**。QNX 操作系统及开发工具。非商业使用计划与量产授权采用不同条款。

<a id="mcu"></a>
## MCU 与实时系统

- [Eclipse OpenBSW](https://github.com/eclipse-openbsw/openbsw) — **开源**。MCU C++ 基础软件，提供 POSIX 与 S32K148 参考应用。可先在主机运行通信例子，再接板级驱动；ADC/PWM 等演示依赖相应硬件。[选型笔记](docs/selection/ecu-simulation.md#openbsw)
- [FreeRTOS](https://github.com/FreeRTOS/FreeRTOS) — **开源**。MCU 实时内核及示例；与采用独立许可和认证材料的安全产品分开看待。
- [Zephyr](https://github.com/zephyrproject-rtos/zephyr) — **开源**。嵌入式操作系统，包含内核、驱动、协议栈和构建配置体系。
- [Eclipse ThreadX](https://github.com/eclipse-threadx/threadx) — **开源**。实时内核，提供线程调度、同步、消息队列和内存管理。
- [Trampoline RTOS](https://github.com/TrampolineRTOS/trampoline) — **开源**。静态配置的实时操作系统，API 对齐 OSEK/VDX 和 AUTOSAR OS。
- [RT-Thread](https://github.com/RT-Thread/rt-thread) — **开源**。国产嵌入式操作系统，提供实时内核、设备驱动框架和软件包体系。
- [开源小满 EasyXMen](https://atomgit.com/easyxmen/XMen) — **开源**。车控基础软件 BSW 代码及配套工程，采用 LGPL-2.1 并附例外条款；配置工具另核许可。

<a id="rust"></a>
## Rust 与嵌入式开发

语言与工具链、任务调度、硬件访问和调试分开列出。Rust 编写的通信组件另见 [DDS](#dds) 和 [进程间通信](#middleware)。

- [The Embedded Rust Book](https://docs.rust-embedded.org/book/) — **文档**。从裸机程序、外设访问和中断入手，介绍嵌入式 Rust 开发。
- [embedded-hal](https://github.com/rust-embedded/embedded-hal) — **开源**。SPI、I²C、GPIO 等 Rust 硬件接口 traits，让驱动与芯片 HAL 解耦。1.0 主 crate 为阻塞接口，异步、CAN 和字节流接口分属配套 crate。[选型笔记](docs/selection/rust.md#embedded-hal)
- [Embassy](https://github.com/embassy-rs/embassy) — **开源**。用静态分配的异步任务组织外设等待与通信。同一执行器内任务协作运行，也可用不同优先级执行器实现抢占；适合先按外设示例核对芯片支持。[选型笔记](docs/selection/rust.md#embassy)
- [RTIC](https://github.com/rtic-rs/rtic) — **开源**。借助中断优先级与 SRP 管理任务和共享资源；v2 也支持异步软件任务。与 Embassy 应比较资源模型和调度方式，而不是“是否异步”。[选型笔记](docs/selection/rust.md#rtic)
- [probe-rs](https://github.com/probe-rs/probe-rs) — **开源**。通过调试探针烧录、设置断点、访问内存并读取 RTT 日志，也能用于 C 固件。官方概览列出 Arm、RISC-V，具体芯片与探针需查目标支持。[选型笔记](docs/selection/rust.md#probe-rs)
- [defmt](https://github.com/knurling-rs/defmt) — **开源**。设备发送格式字典索引与参数，主机还原日志，降低字符串传输量。需配套传输与解码器；归档日志时保留对应 ELF 和构建标识。[选型笔记](docs/selection/rust.md#defmt)
- [CXX](https://github.com/dtolnay/cxx) — **开源**。从类型化桥接声明生成 Rust/C++ 接口，减少手写 FFI，适合逐步接入既有 C++ 模块。检查边界类型，不验证 C++ 函数体内部行为。[选型笔记](docs/selection/rust.md#cxx)
- [Ferrocene](https://github.com/ferrocene/ferrocene) — **开源**。面向安全关键开发的 Rust 工具链，公开源码及配套文档。选型须将发行版本、目标、运行库和资格材料对应；公开 main 文档是开发预览。[选型笔记](docs/selection/rust.md#ferrocene)
- [HighTec Rust Development Platform](https://hightec-rt.com/products/rust-development-platform) — **商业**。面向 AURIX、Stellar 的 Rust 工具链，强调与既有 C/C++ 混合开发。适合从目标芯片、ABI、链接与厂商交付范围开始评估。[选型笔记](docs/selection/rust.md#hightec)
- [Safety-Critical Rust Coding Guidelines](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines) — **文档**。安全关键 Rust 编码指南，讨论语言特性、规则和示例；工具链鉴定不等于应用已获认证。

<a id="autosar"></a>
## AUTOSAR 与基础软件

- [AUTOSAR Classic Platform](https://www.autosar.org/standards/classic-platform) — **标准**。嵌入式 ECU 的应用、运行时环境 RTE 和基础软件 BSW 架构规范。
- [AUTOSAR Adaptive Platform](https://www.autosar.org/standards/adaptive-platform) — **标准**。高性能 ECU 的服务与功能簇规范，可与 Classic 平台共同部署。
- [Python AUTOSAR](https://github.com/cogu/autosar) — **开源**。用 Python 创建和处理 AUTOSAR 模型、生成 ARXML，不提供 ECU 运行时。v0.5 与 v0.4 API 不兼容，旧 ReadTheDocs 教程需与所用版本区分。[选型笔记](docs/selection/ecu-simulation.md#python-autosar)
- [ETAS RTA-CAR / RTA-HVR](https://www.etas.com/ww/en/products-services/vehicle-software-platform/autosar-classic-profile-rta-car/rta-car-details-integration/) — **商业**。AUTOSAR Classic 基础软件与集成方案；RTA-HVR 为支持硬件虚拟化的 MCU 提供软件分区。
- [Vector MICROSAR Classic](https://www.vector.com/en/product/microsar-classic/) — **商业**。AUTOSAR Classic 基础软件及配置、集成工具链。
- [Elektrobit EB tresos](https://www.elektrobit.com/products/ecu/eb-tresos/) — **商业**。ECU 基础软件和配置工具，覆盖 AUTOSAR Classic 工程开发。
- [NeuSAR（东软睿驰）](https://www.neusar.com/) — **商业**。提供 cCore、aCore、服务框架和 DevKit，覆盖 Classic、Adaptive 与车辆软件开发。
- [INTEWORK-EAS-CP（经纬恒润）](https://en.hirain.com/product/480.html) — **商业**。AUTOSAR Classic 基础软件产品，用于 ECU 软件开发与集成。
- [INTEWORK-EAS-AP（经纬恒润）](https://en.hirain.com/product/484.html) — **商业**。基于 C++ 与 POSIX 操作系统的 AUTOSAR Adaptive 实现。
- [ORIENTAIS（普华基础软件）](https://www.i-soft.com.cn/product/vehicle.html) — **商业**。AUTOSAR 基础软件及设计、配置、集成和测试工具；与 EasyXMen 开源代码分列。

<a id="virtualization"></a>
## 隔离与虚拟化

MCU 的 MPU/Guard 分区与 SoC 的 MMU/IOMMU 虚拟化采用不同硬件机制。RTA-HVR 见 [AUTOSAR](#autosar)。

- [Xen Project](https://xenproject.org/) — **开源**。虚拟机监控器，支持多个操作系统共享计算平台。
- [seL4](https://sel4.systems/) — **开源**。具有形式化验证成果的微内核；证明覆盖范围取决于平台和配置。
- [Bao Hypervisor](https://github.com/bao-project/bao-hypervisor) — **开源**。以静态分区划分处理器、内存和设备的嵌入式虚拟机监控器。
- [ACRN](https://github.com/projectacrn/acrn-hypervisor) — **开源**。主要面向 x86 嵌入式平台的虚拟化软件。
- [Vector MICROSAR Hypervisor](https://www.vector.com/en/product/microsar-hypervisor/) — **商业**。面向汽车 MCU 的隔离与虚拟化软件，按目标硬件配置分区。
- [QNX Hypervisor / Hypervisor for Safety](https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety) — **商业**。多操作系统整合产品，分为普通版和带相应安全材料的版本。

<a id="middleware"></a>
## SOME/IP 与进程间通信

- [vsomeip](https://github.com/COVESA/vsomeip) — **开源**。SOME/IP 通信实现，包含配置、服务发现和 E2E 相关库；业务类型生成另接 CommonAPI 等工具。接入从服务标识、载荷编码及对端配置开始。[选型笔记](docs/selection/communication.md#vsomeip)
- [CommonAPI C++ SOME/IP Runtime](https://github.com/COVESA/capicxx-someip-runtime) — **开源**。CommonAPI C++ 的 SOME/IP 运行时绑定，与接口代码生成工具配合使用。
- [Eclipse iceoryx](https://github.com/eclipse-iceoryx/iceoryx) — **开源**。以共享内存传递数据的 C++ 进程间通信框架，避免复制消息载荷。
- [Eclipse iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2) — **开源**。Rust 实现的共享内存通信框架，通过借用和传递样本减少同机载荷复制。评估重点是样本生命周期、内存上限及慢消费者行为。[选型笔记](docs/selection/communication.md#iceoryx2)
- [Eclipse Zenoh](https://github.com/eclipse-zenoh/zenoh) — **开源**。以 Rust 实现的数据通信系统，结合发布订阅、查询和存储。
- [Eclipse uProtocol Specifications](https://github.com/eclipse-uprotocol/up-spec) — **标准**。跨设备与部署环境的通信协议规范，将接口与底层传输分开。
- [Eclipse eCAL](https://github.com/eclipse-ecal/ecal) — **开源**。本机及分布式通信中间件，配有监视、记录和回放工具。

<a id="dds"></a>
## DDS 与配套工具

DDS 定义数据分发模型和 QoS；RTPS 定义线上的互操作协议。实现、语言绑定和测试工具分开比较。

- [OMG DDS](https://www.omg.org/spec/DDS/) — **标准**。数据分发服务的官方规范，定义主题、发布订阅和服务质量策略。
- [RTI Connext Drive](https://www.rti.com/products/connext-drive) — **商业**。面向汽车的 Connext DDS 产品及 AUTOSAR 等集成支持。除通信 API 外，比较目标发行、集成组件与支持材料；性能测试另看 Perftest。[选型笔记](docs/selection/communication.md#rti)
- [Eclipse Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds) — **开源**。DDS/RTPS 实现，官方 HelloWorld 从 IDL、发布者与订阅者展开。可先建立跨主机功能基线，再按相同类型、QoS 与网络条件比较实现。[选型笔记](docs/selection/communication.md#cyclone)
- [Fast DDS](https://github.com/eProsima/Fast-DDS) — **开源**。DDS/RTPS 实现，提供共享内存传输与 Data-sharing 等同机通路。二者不等同于应用端到端零拷贝；Data-sharing 对类型、内存模式和安全插件有约束。[选型笔记](docs/selection/communication.md#fast-dds)
- [OpenDDS](https://opendds.org/) — **开源**。以 C++ 实现的 DDS 中间件，另提供 Java 绑定。
- [RustDDS](https://github.com/Atostek/RustDDS) — **开源**。采用 Rust 风格同步、异步 API 的 DDS 实现。接 ROS 2 时使用独立 ros2-client，而非旧 ros2 模块；先区分需要裸 DDS 还是 ROS 2 节点能力。[选型笔记](docs/selection/communication.md#rustdds)
- [Dust DDS](https://github.com/s2e-systems/dust-dds) — **开源**。Rust 原生 DDS 实现，提供同步/异步 API、IDL 类型生成与 Shapes 示例。适合拿已有 IDL 检查类型映射、对端互通及所需 QoS。[选型笔记](docs/selection/communication.md#dust-dds)
- [Micro XRCE-DDS](https://github.com/eProsima/Micro-XRCE-DDS) — **开源**。资源受限端运行 Client，由 Agent 代理接入 DDS 网络。客户端占用、Agent 部署与链路恢复应一起评估，不等同于在 MCU 上运行完整 DDS 节点。[选型笔记](docs/selection/communication.md#micro-xrce)
- [RTI Perftest](https://github.com/rticommunity/rtiperftest) — **开源**。测量 Connext 吞吐与负载下延迟的程序，构建依赖对应 Connext 库。单向延迟以 RTT/2 估算，不是同步时钟下直接测得的单向时间。[选型笔记](docs/selection/communication.md#perftest)

<a id="vehicle-data"></a>
## 车辆数据与应用接口

- [COVESA Vehicle Signal Specification（VSS）](https://github.com/COVESA/vehicle_signal_specification) — **标准**。定义车辆信号名称、层次、类型与语义，不规定采集或传输方式。接 CAN 时还需 DBC 到 VSS 的映射及 Provider，服务访问可另看 Kuksa。[选型笔记](docs/selection/communication.md#vss)
- [VSS Tools](https://github.com/COVESA/vss-tools) — **开源**。校验、转换 VSS 描述，并生成不同格式的数据表示。
- [Eclipse Kuksa Databroker](https://github.com/eclipse-kuksa/kuksa-databroker) — **开源**。以 gRPC 提供 VSS 信号读写与订阅，底层通过 Provider 连接 CAN 等接口。当前文档区分 VAL v2 与已弃用 v1，示例 CLI 的 API 支持也需配对。[选型笔记](docs/selection/communication.md#kuksa)
- [Eclipse Kuksa CAN Provider](https://github.com/eclipse-kuksa/kuksa-can-provider) — **开源**。将 CAN 信号映射到 Kuksa 数据服务。
- [Eclipse Velocitas](https://github.com/eclipse-velocitas) — **开源**。车辆应用 SDK、项目模板和开发工具集合。
- [Eclipse Autowrx](https://github.com/eclipse-autowrx) — **开源**。用于车辆功能原型开发和体验验证的 digital.auto 相关工具。

<a id="networks"></a>
## CAN、以太网与时间同步

- [can-utils](https://github.com/linux-can/can-utils) — **开源**。Linux SocketCAN 命令行工具，支持报文收发、记录和回放。
- [python-can](https://github.com/hardbyte/python-can) — **开源**。以统一 Python API 连接多种 CAN 后端，负责编程收发与记录。VirtualBus 可测软件逻辑，但不模拟速率限制或 CAN ID 仲裁；信号编解码另接 cantools。[选型笔记](docs/selection/measurement.md#python-can)
- [cantools](https://github.com/cantools/cantools) — **开源**。读取 DBC 等数据库，编解码信号并生成 C 消息结构与 pack/unpack 函数。生成物是数据编解码层，不包含 CAN 驱动或任务调度。[选型笔记](docs/selection/measurement.md#cantools)
- [canmatrix](https://github.com/ebroecker/canmatrix) — **开源**。比较、编辑和转换 CAN 通信矩阵。
- [Linux PTP](https://www.linuxptp.org/) — **开源**。Linux PTP 时间同步工具，支持硬件与软件时间戳。
- [IEEE 802.1 TSN Task Group](https://1.ieee802.org/tsn/) — **标准**。时间敏感网络的标准化入口，包含时间同步、流量调度等机制。
- [OPEN Alliance](https://opensig.org/) — **生态**。车载以太网技术规范、互操作和测试协作组织。

<a id="bus-tools"></a>
## 总线分析与测试工具

这一节包含上位机软件及与其配套的接口生态；诊断库和标定软件见 [下一节](#diagnostics)。

- [TSMaster（同星智能）](https://www.tosunai.com/product/tsmaster/) — **商业**。总线分析、仿真与测试软件，可导入 DBC/LDF、用 C/Python 扩展，并记录回放 BLF。试用时按真实数据库、接口卡和诊断/标定授权选件验证。[选型笔记](docs/selection/measurement.md#tsmaster)
- [ZXDoc（致远电子）](https://www.zlg.cn/carbustools/carbustools/product/id/382.html) — **商业**。配合致远硬件的总线分析软件，提供 Python/API 扩展及 ASC、BLF、MAT、MF4 记录。基于 DBC 信号的 ARXML 需先转成 DBC，迁移时核对语义保留情况。[选型笔记](docs/selection/measurement.md#zxdoc)
- [INTEWORK-VBA（经纬恒润）](https://intework.hirain.com/) — **商业**。总线分析、诊断与标定工具，配合 TestBase VCI。官方站提供以太网标定、故障定位和 ECUTest 调用教程，可直接评估既有台架的自动化接入。[选型笔记](docs/selection/measurement.md#vba)
- [Vector CANoe](https://www.vector.com/en/product/canoe/) — **商业**。将网络仿真、刺激、诊断和自动化测试组织在一个环境中。已有工程与测试资产可作为选型起点；纯软件测试另有 CANoe4SW 产品范围。[选型笔记](docs/selection/measurement.md#canoe)
- [BUSMASTER](https://github.com/rbei-etas/busmaster) — **开源**。Windows 上的车辆总线仿真、分析和测试软件。
- [SavvyCAN](https://github.com/collin80/SavvyCAN) — **开源**。基于 Qt 的跨平台 CAN 分析工具，支持报文记录、可视化和 DBC 解码。
- [Wireshark](https://www.wireshark.org/) — **开源**。网络抓包与协议分析工具，可用于排查车载以太网通信问题。

<a id="diagnostics"></a>
## 诊断、测量与标定

- [udsoncan](https://github.com/pylessard/python-udsoncan) — **开源**。Python UDS 客户端，通过 connection 接入传输层，DID 编解码由 ECU 数据定义配置。适合从一个只读 DID 验证服务、codec 与超时行为。[选型笔记](docs/selection/measurement.md#udsoncan)
- [python-doipclient](https://github.com/jacobschaer/python-doipclient) — **开源**。处理 DoIP 发现、连接与路由激活，可通过适配器接 udsoncan。除 IP 外还需 ECU/客户端逻辑地址；当前 TCP 自动重连选项默认关闭。[选型笔记](docs/selection/measurement.md#doip)
- [odxtools](https://github.com/mercedes-benz/odxtools) — **开源**。读取和处理 ODX 诊断描述，提供诊断数据查询与编解码工具。
- [asammdf](https://github.com/danielhrisca/asammdf) — **开源**。读取、筛选、裁剪、重采样与导出 MDF 测量记录，用于采集后的批处理。跨采样率合并时应明确插值方式，并保留原始时间轴与转换参数。[选型笔记](docs/selection/measurement.md#asammdf)
- [XCPlite](https://github.com/vectorgrp/XCPlite) — **开源**。轻量 XCP 实现，为应用增加测量与标定接口。
- [COVESA DLT Daemon](https://github.com/COVESA/dlt-daemon) — **开源**。车载 Diagnostic Log and Trace 日志服务。
- [Eclipse OpenSOVD](https://projects.eclipse.org/projects/automotive.opensovd) — **开源**。服务化车辆诊断 SOVD 的实现项目。
- [Vector CANape](https://www.vector.com/en/product/canape/) — **商业**。ECU 测量、参数标定和数据记录软件。
- [ETAS INCA](https://www.etas.com/ww/en/products-services/data-acquisition-processing-tools/software-products/inca-software-products/) — **商业**。用于实车、台架和仿真环境的测量、ECU 标定及诊断工具。

<a id="modeling"></a>
## 建模与代码生成

- [Eclipse Capella](https://mbse-capella.org/) — **开源**。基于 Arcadia 方法的系统建模工具，描述功能、逻辑架构和物理架构。
- [Vector PREEvision](https://www.vector.com/en/product/preevision/) — **商业**。汽车 E/E 架构建模工具，连接需求、软件、网络和硬件设计。
- [Simulink](https://www.mathworks.com/products/simulink.html) — **商业**。基于框图的动态系统建模与仿真环境，用于控制算法设计和模型级测试。
- [Embedded Coder](https://www.mathworks.com/products/embedded-coder.html) — **商业**。从 MATLAB、Simulink 等模型生成面向嵌入式目标的 C/C++ 代码。
- [OpenModelica](https://openmodelica.org/) — **开源**。Modelica 建模与仿真环境，可建立车辆热、流体、电气和机械系统模型。
- [MWORKS.Sysplorer（同元软控）](https://en.tongyuan.cc/product/detail/?id=sysplorer) — **商业**。多领域系统建模与仿真环境，支持 Modelica 和 FMI。
- [Eclipse APP4MC](https://eclipse.dev/app4mc/) — **开源**。多核系统建模与分析工具，描述软件任务、硬件资源及其映射。

<a id="simulation"></a>
## 虚拟 ECU 与 SIL/HIL

- [Vector SIL Kit](https://github.com/vectorgrp/sil-kit) — **开源**。连接虚拟 ECU、网络与模型的通信和仿真协调库，提供生命周期及时间协调。接入的 ECU/物理模型仍需另行提供。[选型笔记](docs/selection/ecu-simulation.md#sil-kit)
- [Eclipse OpenXilEnv](https://github.com/eclipse-openxilenv/openxilenv) — **开源**。以 SIL 为重点，将控制代码编成主机外部进程，提供变量测量、激励及 A2L/XCP 接口。与执行目标固件机器码的仿真器是不同路径。[选型笔记](docs/selection/ecu-simulation.md#openxilenv)
- [Eclipse openDuT](https://github.com/eclipse-opendut/opendut) — **开源**。组织分布式测试设备与网络环境，连接不同地点的 ECU 台架。
- [Renode](https://github.com/renode/renode) — **开源**。在机器与外设模型上运行嵌入式固件，可用 Robot Framework 自动检查串口、网络等行为。先确认目标模型，再从最小启动测试接入回归。[选型笔记](docs/selection/ecu-simulation.md#renode)
- [QEMU](https://www.qemu.org/) — **开源**。运行由 CPU、内存和设备组成的目标系统。选型先匹配 machine 与板级设备；支持某一 CPU 架构不等于支持任意同架构 MCU。[选型笔记](docs/selection/ecu-simulation.md#qemu)
- [Functional Mock-up Interface（FMI）](https://fmi-standard.org/) — **标准**。以 FMU 交换模型的接口规范。ME、CS 与 SE 的求解和调度职责不同；接入前核对 FMI 版本、接口类型及平台二进制。[选型笔记](docs/selection/ecu-simulation.md#fmi)
- [FMPy](https://github.com/CATIA-Systems/FMPy) — **开源**。用 Python、命令行或 GUI 检查与运行 FMU，适合批量实验和回归。先用 dump 查看接口与变量，再以固定输入运行；原始物理模型需由其他工具提供。[选型笔记](docs/selection/ecu-simulation.md#fmpy)
- [dSPACE VEOS](https://www.dspace.com/en/inc/home/products/sw/simulation_software/veos.cfm) — **商业**。在 PC 上集成模型、虚拟 ECU 和网络通信的仿真平台。
- [dSPACE SCALEXIO](https://www.dspace.com/en/inc/home/products/hw/simulator_hardware/scalexio.cfm) — **商业**。由实时计算与 I/O 构成的 HIL 平台，用于 ECU 闭环测试。
- [NI VeriStand](https://www.ni.com/en-us/shop/product/veristand.html) — **商业**。配置实时测试系统、接入模型与 I/O，并组织 HIL 测试。
- [INTEWORK-TAE（经纬恒润）](https://en.hirain.com/product/573.html) — **商业**。通用测试用例执行软件，可对接不同仿真系统。

<a id="verification"></a>
## 调试、代码分析与时序验证

- [Lauterbach TRACE32](https://www.lauterbach.com/) — **商业**。嵌入式调试与指令跟踪工具，配合目标平台及调试硬件使用。
- [VectorCAST](https://www.vector.com/en/product/vectorcast/) — **商业**。嵌入式软件单元测试、集成测试和覆盖率分析工具。
- [Polyspace](https://www.mathworks.com/products/polyspace.html) — **商业**。代码缺陷检测、编码规则检查和形式化分析工具族。
- [CBMC](https://github.com/diffblue/cbmc) — **开源**。C/C++ 有界模型检查器，可验证断言、内存访问和其他程序性质。
- [Frama-C](https://www.frama-c.com/) — **开源**。C 程序分析框架，通过插件进行值分析、规约检查和演绎验证。
- [Kani](https://github.com/model-checking/kani) — **开源**。Rust 模型检查器，检查断言、panic 和内存安全相关性质。
- [Vector TA Tool Suite](https://www.vector.com/en/product/ta-tool-suite/) — **商业**。分析 ECU 任务调度、执行时间和多核时序，支持设计与运行记录对照。

<a id="ota"></a>
## OTA 与软件更新

- [Uptane](https://uptane.org/) — **标准**。以仓库角色、元数据与 ECU 验证规则组织车辆更新的信任关系。解决哪些更新可被信任，下载、Flash 写入和启动切换由具体实现承担。[选型笔记](docs/selection/updates.md#uptane)
- [python-tuf](https://github.com/theupdateframework/python-tuf) — **开源**。The Update Framework 的 Python 实现，提供安全更新元数据处理。
- [RAUC](https://github.com/rauc/rauc) — **开源**。围绕签名 bundle、slot 和引导程序集成组织 Linux 更新。安装完成后仍需应用健康确认，回退由引导与确认策略共同实现。[选型笔记](docs/selection/updates.md#rauc)
- [SWUpdate](https://github.com/sbabic/swupdate) — **开源**。用 sw-description 和 handler 描述、执行多类安装任务，适合定制更新流程。签名、硬件兼容与中断恢复需落实到实际构建和配置。[选型笔记](docs/selection/updates.md#swupdate)
- [Eclipse hawkBit](https://github.com/eclipse-hawkbit/hawkbit) — **开源**。设备更新包分发与更新管理后端。

<a id="secure-boot"></a>
## 安全启动与可信执行

- [MCUboot](https://www.trustedfirmware.org/projects/mcuboot/index.html) — **开源**。MCU 镜像验证与更新引导程序，按模式管理 Flash 槽位。支持试启动的交换流程需应用确认；覆盖式等模式不能笼统视为自动 A/B 回退。[选型笔记](docs/selection/updates.md#mcuboot)
- [OP-TEE](https://www.trustedfirmware.org/projects/op-tee/) — **开源**。基于 Arm TrustZone 的可信执行环境，将可信应用与普通操作系统分隔。

<a id="orchestration"></a>
## 车端编排与车云协同

- [Eclipse Ankaios](https://github.com/eclipse-ankaios/ankaios) — **开源**。嵌入式工作负载管理器，管理跨节点应用的启动、停止和配置。
- [Eclipse BlueChi](https://github.com/eclipse-bluechi/bluechi) — **开源**。通过 systemd 与 D-Bus 控制多节点服务。
- [Eclipse Kanto](https://github.com/eclipse-kanto) — **开源**。嵌入式设备的容器管理、设备管理和云连接组件集合。
- [Eclipse Symphony](https://github.com/eclipse-symphony/symphony) — **开源**。分布式应用编排框架，管理部署目标与应用期望状态。

<a id="supply-chain"></a>
## 构建与软件供应链

- [Yocto Project](https://www.yoctoproject.org/) — **生态**。定制嵌入式 Linux 的构建工具与协作项目，组织 BSP、软件包和系统镜像。
- [Buildroot](https://buildroot.org/) — **开源**。交叉编译嵌入式 Linux 工具链、根文件系统、内核及引导程序。
- [Syft](https://github.com/anchore/syft) — **开源**。从镜像和文件系统生成软件物料清单 SBOM。
- [SPDX](https://spdx.dev/) — **标准**。交换软件组件、许可和供应链信息的标准。
- [CycloneDX](https://cyclonedx.org/) — **标准**。描述软件组件、依赖与安全相关信息的物料清单标准。
- [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort) — **开源**。自动分析依赖、扫描许可并生成软件合规报告。

<a id="safety"></a>
## 功能安全与开发规范

- [ISO 26262：Part 1 入口](https://www.iso.org/standard/68383.html) — **标准**。道路车辆功能安全系列；本链接为术语部分，可沿官方页面查找其他部分。
- [ISO/SAE 21434](https://www.iso.org/standard/70918.html) — **标准**。道路车辆全生命周期的网络安全工程要求。
- [ISO 21448（SOTIF）](https://www.iso.org/standard/77490.html) — **标准**。预期功能安全，关注功能不足和可合理预见的误用产生的风险。
- [Automotive SPICE](https://vda-qmc.de/en/automotive-spice/) — **标准**。汽车软件与系统开发过程评估模型。
- [MISRA](https://misra.org.uk/) — **标准**。安全相关软件的 C/C++ 编码指南及配套资料，正文按权利方条款取得。
- [Eclipse Trustable Software Framework](https://projects.eclipse.org/projects/technology.tsf) — **开源**。组织软件工程中的风险、论证与证据，支持结论追溯。

<a id="hmi"></a>
## 座舱与 HMI

- [Android Automotive Vehicle HAL](https://source.android.com/docs/automotive/vhal) — **文档**。Android 车辆属性的读取、写入与订阅接口。
- [LVGL](https://github.com/lvgl/lvgl) — **开源**。面向嵌入式设备的图形库，可用于仪表、小屏和控制面板。
- [Qt for MCUs](https://doc.qt.io/QtForMCUs/) — **商业**。面向 MCU 的图形界面开发产品；授权方式与其他 Qt 模块分开核对。

<a id="adas"></a>
## 自动驾驶与场景仿真

- [Autoware](https://github.com/autowarefoundation/autoware) — **开源**。自动驾驶软件栈，包含车辆应用、传感器数据处理和系统集成组件。
- [Apollo](https://github.com/ApolloAuto/apollo) — **开源**。自动驾驶平台，提供感知、规划、控制等模块及工程工具。
- [CARLA](https://github.com/carla-simulator/carla) — **开源**。自动驾驶研究仿真器，生成道路环境、交通参与者和传感器数据。
- [esmini](https://github.com/esmini/esmini) — **开源**。轻量 OpenSCENARIO 场景执行工具。
- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo) — **开源**。交通流仿真系统，用于车辆与道路交通交互实验。
- [Open Simulation Interface（OSI）](https://github.com/OpenSimulationInterface/open-simulation-interface) — **标准**。仿真环境与自动驾驶功能之间的传感器和环境数据接口。

<a id="ev"></a>
## 电池与充电

- [foxBMS 2](https://github.com/foxBMS/foxbms-2) — **开源**。电池管理系统研发平台，提供硬件、基础软件和控制功能参考。
- [EVerest](https://github.com/EVerest/EVerest) — **开源**。充电设施侧的软件框架，包含充电控制及与车辆、后台通信的组件。

<a id="related"></a>
## 相关清单

- [awesome-automotive · Marcin214](https://github.com/Marcin214/awesome-automotive) — **清单**。汽车嵌入式、AUTOSAR、总线、诊断和开发工具资源。
- [Awesome-Automotive · ajay-bhojani](https://github.com/ajay-bhojani/Awesome-Automotive) — **清单**。汽车工程学习路线及技术资料。
- [awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) — **清单**。车辆安全研究、协议和授权测试资源。
- [Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded) — **清单**。嵌入式操作系统、工具链和开发资料。
- [Awesome Embedded Rust](https://github.com/rust-embedded/awesome-embedded-rust) — **清单**。嵌入式 Rust 的芯片支持、驱动、工具和学习资源。
- [awesome-canbus](https://github.com/iDoka/awesome-canbus) — **清单**。CAN 总线软件、设备和技术资料。
- [awesome-linbus](https://github.com/iDoka/awesome-linbus) — **清单**。LIN 总线工具与边缘节点开发资源。
- [awesome-autonomous-vehicles](https://github.com/manfreddiaz/awesome-autonomous-vehicles) — **清单**。自动驾驶软件、仿真和数据资源。
- [awesome-ros2](https://github.com/fkromer/awesome-ros2) — **清单**。ROS 2 中间件、开发工具与应用项目。
- [Awesome](https://github.com/sindresorhus/awesome) — **清单**。Awesome 清单的总目录及组织规范。

<!-- catalog:end -->

<a id="contributing"></a>
## 参与维护

欢迎补充资源，或修正链接、分类和描述。请提供官方来源，说明它解决什么问题。参见 [贡献指南](CONTRIBUTING.md)、[维护说明](docs/MAINTENANCE.md) 与 [本轮编辑记录](docs/PUBLISHING.md)。

<a id="attribution"></a>
## 转载与引用

本项目由 **ComfortUni（适宇科技）** 发起和维护，与贡献者共同整理。

文档采用 [CC BY 4.0](LICENSE)，允许复制、翻译、改编和商业使用；公开传播时按许可保留署名、来源、许可信息并标明改动。维护脚本与测试代码继续采用 [MIT](LICENSE-CODE)。上游代码、标准和产品另遵循各自许可。

> 转载自 [Awesome SDV · 软件定义汽车资源指南](https://github.com/yzy-comfortuni/awesome-sdv)，由 ComfortUni（适宇科技）及贡献者整理，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可使用。内容按原样转载。

改编或翻译时将最后一句换成实际改动说明。其他署名格式、商标边界和历史 MIT 授权见 [ATTRIBUTION.md](ATTRIBUTION.md)。机器可读引用见 [CITATION.cff](CITATION.cff)。
