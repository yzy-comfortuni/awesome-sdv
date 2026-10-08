# Awesome SDV · 软件定义汽车

软件定义汽车的开源项目、商业工具、标准和技术资料。覆盖 MCU、区域控制器、中央计算，以及车载软件的开发、测试和更新。

按工程用途分类，保留英文名称，提供中文说明。商业产品与开源项目放在同一主题下，用标签区分。

[贡献指南](CONTRIBUTING.md) · [来源与补充记录](docs/REVIEW.md) · [维护说明](docs/MAINTENANCE.md)

## 目录

| 平台与开发 | 通信与数据 | 工程与交付 |
| --- | --- | --- |
| [架构与生态](#ecosystem) | [SOME/IP 与进程间通信](#middleware) | [总线分析与测试工具](#bus-tools) |
| [车载操作系统与集成平台](#platforms) | [DDS 与配套工具](#dds) | [诊断、测量与标定](#diagnostics) |
| [MCU 与实时系统](#mcu) | [车辆数据与应用接口](#vehicle-data) | [建模与代码生成](#modeling) |
| [Rust 与嵌入式开发](#rust) | [CAN、以太网与时间同步](#networks) | [虚拟 ECU 与 SIL/HIL](#simulation) |
| [AUTOSAR 与基础软件](#autosar) | [车端编排与车云协同](#orchestration) | [调试、代码分析与时序验证](#verification) |
| [隔离与虚拟化](#virtualization) | [OTA 与软件更新](#ota) | [构建与软件供应链](#supply-chain) |
| [座舱与 HMI](#hmi) | [安全启动与可信执行](#secure-boot) | [功能安全与开发规范](#safety) |

[自动驾驶与场景仿真](#adas) · [电池与充电](#ev) · [相关清单](#related)

<a id="commercial"></a>
标签说明：**开源**为代码项目，**商业**为需按厂商条款取得授权的产品，**标准**为规范，**文档**为技术资料，**生态**为组织或项目集合，**清单**为其他资源目录。免费下载不等于开源；开源代码的商业支持、配置工具和认证材料可能另行授权。

选型时请核对具体版本、目标硬件和许可。这里的收录不代表已完成互操作、性能或安全认证验证；通用嵌入式工具也不必然支持某款车规 MCU。

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

- [Eclipse OpenBSW](https://github.com/eclipse-openbsw/openbsw) — **开源**。面向 MCU 的 C++ 基础软件，提供生命周期管理、通信组件和参考工程。
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
- [embedded-hal](https://github.com/rust-embedded/embedded-hal) — **开源**。用 Rust traits 定义硬件抽象接口，让外设驱动与具体芯片解耦。
- [Embassy](https://github.com/embassy-rs/embassy) — **开源**。嵌入式异步开发框架，提供执行器、定时器、同步原语和多种芯片 HAL。
- [RTIC](https://github.com/rtic-rs/rtic) — **开源**。以中断和任务优先级组织并发的实时框架，管理任务之间的共享资源。
- [probe-rs](https://github.com/probe-rs/probe-rs) — **开源**。嵌入式烧录与调试工具集，可通过调试探针访问受支持的目标芯片。
- [defmt](https://github.com/knurling-rs/defmt) — **开源**。面向嵌入式设备的紧凑日志框架，将格式化工作移到主机端。
- [CXX](https://github.com/dtolnay/cxx) — **开源**。生成 Rust 与 C++ 之间的类型化接口，便于接入已有 C++ 组件。
- [Ferrocene](https://github.com/ferrocene/ferrocene) — **开源**。面向安全关键开发的 Rust 工具链；经鉴定的发行包、支持服务和材料见 [Ferrocene](https://ferrocene.dev/)。
- [HighTec Rust Development Platform](https://hightec-rt.com/rust) — **商业**。车载嵌入式 Rust 编译工具链，可与 C/C++ 工程结合使用；目标架构按产品版本选择。
- [Safety-Critical Rust Coding Guidelines](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines) — **文档**。安全关键 Rust 编码指南，讨论语言特性、规则和示例；工具链鉴定不等于应用已获认证。

<a id="autosar"></a>
## AUTOSAR 与基础软件

- [AUTOSAR Classic Platform](https://www.autosar.org/standards/classic-platform) — **标准**。嵌入式 ECU 的应用、运行时环境 RTE 和基础软件 BSW 架构规范。
- [AUTOSAR Adaptive Platform](https://www.autosar.org/standards/adaptive-platform) — **标准**。高性能 ECU 的服务与功能簇规范，可与 Classic 平台共同部署。
- [Python AUTOSAR](https://github.com/cogu/autosar) — **开源**。用 Python 创建和处理 AUTOSAR 模型与 ARXML 文件，不提供 ECU 运行时。
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

- [vsomeip](https://github.com/COVESA/vsomeip) — **开源**。SOME/IP 实现，支持服务发现、请求响应和事件通信。
- [CommonAPI C++ SOME/IP Runtime](https://github.com/COVESA/capicxx-someip-runtime) — **开源**。CommonAPI C++ 的 SOME/IP 运行时绑定，与接口代码生成工具配合使用。
- [Eclipse iceoryx](https://github.com/eclipse-iceoryx/iceoryx) — **开源**。以共享内存传递数据的 C++ 进程间通信框架，避免复制消息载荷。
- [Eclipse iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2) — **开源**。Rust 实现的共享内存通信框架，提供零拷贝 IPC 及其他语言绑定。
- [Eclipse Zenoh](https://github.com/eclipse-zenoh/zenoh) — **开源**。以 Rust 实现的数据通信系统，结合发布订阅、查询和存储。
- [Eclipse uProtocol Specifications](https://github.com/eclipse-uprotocol/up-spec) — **标准**。跨设备与部署环境的通信协议规范，将接口与底层传输分开。
- [Eclipse eCAL](https://github.com/eclipse-ecal/ecal) — **开源**。本机及分布式通信中间件，配有监视、记录和回放工具。

<a id="dds"></a>
## DDS 与配套工具

DDS 定义数据分发模型和 QoS；RTPS 定义线上的互操作协议。实现、语言绑定和测试工具分开比较。

- [OMG DDS](https://www.omg.org/spec/DDS/) — **标准**。数据分发服务的官方规范，定义主题、发布订阅和服务质量策略。
- [RTI Connext Drive](https://www.rti.com/products/connext-drive) — **商业**。面向汽车的 Connext DDS 产品，提供 AUTOSAR Classic、Adaptive 等集成支持。
- [Eclipse Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds) — **开源**。DDS/RTPS 实现，用于分布式数据发布订阅。
- [Fast DDS](https://github.com/eProsima/Fast-DDS) — **开源**。eProsima 的 DDS/RTPS 实现，提供数据分发与 QoS 配置。
- [OpenDDS](https://opendds.org/) — **开源**。以 C++ 实现的 DDS 中间件，另提供 Java 绑定。
- [RustDDS](https://github.com/Atostek/RustDDS) — **开源**。Atostek 的 Rust DDS 实现，提供同步、异步接口及 ROS 2 通信示例。
- [Dust DDS](https://github.com/s2e-systems/dust-dds) — **开源**。Rust 原生 DDS 实现，提供类型支持、IDL 代码生成和互操作测试。
- [Micro XRCE-DDS](https://github.com/eProsima/Micro-XRCE-DDS) — **开源**。通过客户端与 Agent 让资源受限设备接入 DDS 网络，采用 DDS-XRCE 协议。
- [RTI Perftest](https://github.com/rticommunity/rtiperftest) — **开源**。测量 Connext 通信延迟和吞吐量的命令行程序；构建时需要相应 Connext 库。

<a id="vehicle-data"></a>
## 车辆数据与应用接口

- [COVESA Vehicle Signal Specification（VSS）](https://github.com/COVESA/vehicle_signal_specification) — **标准**。车辆信号的名称、层次和语义模型，不规定总线传输方式。
- [VSS Tools](https://github.com/COVESA/vss-tools) — **开源**。校验、转换 VSS 描述，并生成不同格式的数据表示。
- [Eclipse Kuksa Databroker](https://github.com/eclipse-kuksa/kuksa-databroker) — **开源**。基于 VSS 的车辆信号服务，为应用提供统一的数据访问接口。
- [Eclipse Kuksa CAN Provider](https://github.com/eclipse-kuksa/kuksa-can-provider) — **开源**。将 CAN 信号映射到 Kuksa 数据服务。
- [Eclipse Velocitas](https://github.com/eclipse-velocitas) — **开源**。车辆应用 SDK、项目模板和开发工具集合。
- [Eclipse Autowrx](https://github.com/eclipse-autowrx) — **开源**。用于车辆功能原型开发和体验验证的 digital.auto 相关工具。

<a id="networks"></a>
## CAN、以太网与时间同步

- [can-utils](https://github.com/linux-can/can-utils) — **开源**。Linux SocketCAN 命令行工具，支持报文收发、记录和回放。
- [python-can](https://github.com/hardbyte/python-can) — **开源**。通过统一 Python API 访问多种 CAN 接口，编写采集与测试脚本。
- [cantools](https://github.com/cantools/cantools) — **开源**。解析 CAN 数据库，编解码报文并生成代码。
- [canmatrix](https://github.com/ebroecker/canmatrix) — **开源**。比较、编辑和转换 CAN 通信矩阵。
- [Linux PTP](https://www.linuxptp.org/) — **开源**。Linux PTP 时间同步工具，支持硬件与软件时间戳。
- [IEEE 802.1 TSN Task Group](https://1.ieee802.org/tsn/) — **标准**。时间敏感网络的标准化入口，包含时间同步、流量调度等机制。
- [OPEN Alliance](https://opensig.org/) — **生态**。车载以太网技术规范、互操作和测试协作组织。

<a id="bus-tools"></a>
## 总线分析与测试工具

这一节包含上位机软件及与其配套的接口生态；诊断库和标定软件见 [下一节](#diagnostics)。

- [TSMaster（同星智能）](https://www.tosunai.com/product/tsmaster/) — **商业**。汽车总线分析、仿真和测试软件，支持诊断、刷写、标定与脚本扩展。基础功能可免费下载，专业功能按版本授权。
- [ZXDoc（致远电子）](https://www.zlg.cn/carbustools/carbustools/product/id/382.html) — **商业**。支持 CAN、CAN FD、LIN 和车载以太网的分析软件，提供 UDS、SOME/IP、XCP/CCP 与 Python 扩展。
- [INTEWORK-VBA（经纬恒润）](https://www.hirain.com/news_detail/478.html) — **商业**。车辆总线分析工具，覆盖监测、仿真、诊断和标定。
- [Vector CANoe](https://www.vector.com/en/product/canoe/) — **商业**。网络、ECU 和分布式软件的开发与测试环境，支持仿真和自动化测试。
- [BUSMASTER](https://github.com/rbei-etas/busmaster) — **开源**。Windows 上的车辆总线仿真、分析和测试软件。
- [SavvyCAN](https://github.com/collin80/SavvyCAN) — **开源**。基于 Qt 的跨平台 CAN 分析工具，支持报文记录、可视化和 DBC 解码。
- [Wireshark](https://www.wireshark.org/) — **开源**。网络抓包与协议分析工具，可用于排查车载以太网通信问题。

<a id="diagnostics"></a>
## 诊断、测量与标定

- [udsoncan](https://github.com/pylessard/python-udsoncan) — **开源**。Python UDS 客户端库，用于诊断服务调用和自动化测试。
- [python-doipclient](https://github.com/jacobschaer/python-doipclient) — **开源**。DoIP 客户端，可与 UDS 库组合使用。
- [odxtools](https://github.com/mercedes-benz/odxtools) — **开源**。读取和处理 ODX 诊断描述，提供诊断数据查询与编解码工具。
- [asammdf](https://github.com/danielhrisca/asammdf) — **开源**。读取、分析和转换 MDF 测量文件。
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

- [Vector SIL Kit](https://github.com/vectorgrp/sil-kit) — **开源**。连接虚拟 ECU、网络和仿真参与者的通信与协同库。
- [Eclipse OpenXilEnv](https://github.com/eclipse-openxilenv/openxilenv) — **开源**。在 PC 上运行、测量和测试嵌入式功能的 SIL/HIL 环境。
- [Eclipse openDuT](https://github.com/eclipse-opendut/opendut) — **开源**。组织分布式测试设备与网络环境，连接不同地点的 ECU 台架。
- [Renode](https://github.com/renode/renode) — **开源**。基于芯片与外设模型运行嵌入式软件，支持自动化测试。
- [QEMU](https://www.qemu.org/) — **开源**。系统仿真与虚拟化工具，用于启动和测试目标平台软件；不默认提供周期精确仿真。
- [Functional Mock-up Interface（FMI）](https://fmi-standard.org/) — **标准**。模型交换与联合仿真接口，以 FMU 封装可交换的模型。
- [FMPy](https://github.com/CATIA-Systems/FMPy) — **开源**。使用 Python 检查和运行 FMU，支持批量仿真。
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

- [Uptane](https://uptane.org/) — **标准**。车辆软件更新的安全框架，定义更新元数据与信任关系。
- [python-tuf](https://github.com/theupdateframework/python-tuf) — **开源**。The Update Framework 的 Python 实现，提供安全更新元数据处理。
- [RAUC](https://github.com/rauc/rauc) — **开源**。嵌入式 Linux 更新框架，管理签名更新包和系统安装。
- [SWUpdate](https://github.com/sbabic/swupdate) — **开源**。可配置的嵌入式更新框架，支持不同存储布局与安装处理器。
- [Eclipse hawkBit](https://github.com/eclipse-hawkbit/hawkbit) — **开源**。设备更新包分发与更新管理后端。

<a id="secure-boot"></a>
## 安全启动与可信执行

- [MCUboot](https://www.trustedfirmware.org/projects/mcuboot/index.html) — **开源**。MCU 安全引导程序，提供固件验证与升级支持。
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

## 参与维护

欢迎补充有明确用途的资源，或修正链接与描述。请提供官方来源，并说明它解决什么问题。格式和写作要求见 [贡献指南](CONTRIBUTING.md)。

本仓库原创文字与脚本采用 [MIT License](LICENSE)；上游代码、标准和产品保留各自许可。
