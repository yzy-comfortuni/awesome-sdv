# Awesome SDV · 软件定义汽车

面向软件定义汽车（Software-Defined Vehicle）的项目、标准与工程资料清单。以开源为主，商业产品单独列出。

关注从 **MCU 与区域控制器，到车载高性能计算平台，再到车辆全生命周期的软件开发、部署和验证**。自动驾驶、座舱和充电是相关应用，不代表 SDV 的全部。

中文说明，保留英文项目名与技术术语，方便检索原文。首次整理：**2026-10-08**。

[贡献指南](CONTRIBUTING.md) · [来源与核验说明](docs/REVIEW.md) · [维护与检查](docs/MAINTENANCE.md)

## 从哪里开始

| 你正在做什么 | 建议先看 |
| --- | --- |
| 建立整体认识 | [架构与生态](#ecosystem) → [整车软件平台](#platforms) → [车辆数据与应用](#vehicle-data) |
| 做 MCU、区域控制器或混合关键性系统 | [MCU 与实时系统](#mcu) → [AUTOSAR](#autosar) → [隔离与虚拟化](#virtualization) → [安全与过程](#safety) |
| 做一个可运行的软件原型 | SDV Blueprints、Leda、Kuksa、Velocitas；先跟随各项目示例，再确认版本和接口能否配合 |
| 建立开发、测试与发布链 | [虚拟 ECU 与仿真](#simulation) → [诊断与标定](#diagnostics) → [OTA](#ota) → [构建与供应链](#supply-chain) |

以上是阅读路线，不是已经完成互操作验证的整车技术栈。

## 如何读这份清单

条目用 **开源 / 标准 / 文档 / 生态 / 商业 / 清单** 区分资源性质。`开源`表示上游以开源项目提供，不表示所有依赖、模型、数据、工具和认证材料都使用相同许可；采用前仍需检查具体版本的 LICENSE。

**收录不等于量产推荐或安全认证。** 平台适配、最坏执行时间、故障隔离、网络时序、更新回退和安全论证，需要在自己的硬件与配置上验证。标准正文可能需要购买或会员资格，本仓库不分发未授权副本。

## 目录

- [架构与生态](#ecosystem)
- [整车软件平台与车载 Linux](#platforms)
- [MCU、区域控制器与实时系统](#mcu)
- [AUTOSAR 与接口建模](#autosar)
- [隔离、虚拟化与混合关键性](#virtualization)
- [服务通信与进程间通信](#middleware)
- [车辆数据、API 与应用开发](#vehicle-data)
- [CAN、以太网与时间同步](#networks)
- [诊断、日志、测量与标定](#diagnostics)
- [OTA 与软件更新安全](#ota)
- [车端编排与车云协同](#orchestration)
- [虚拟 ECU、SIL/HIL 与联合仿真](#simulation)
- [构建、软件物料清单与供应链](#supply-chain)
- [功能安全、网络安全与开发过程](#safety)
- [座舱接口与嵌入式 HMI](#hmi)
- [相邻领域：自动驾驶与场景仿真](#adas)
- [相邻领域：电池与充电](#ev)
- [商业平台与工程工具](#commercial)
- [相关 Awesome Lists 与致谢](#related)

<!-- catalog:start -->

<a id="ecosystem"></a>
## 架构与生态

- [Eclipse SDV 项目目录](https://eclipsesdv.org/projects/) — **生态**。查找 Eclipse 汽车软件项目的官方入口，覆盖车端、云端、工具链和基础组件；项目被列入目录不代表成熟度相同。
- [SOAFEE](https://www.soafee.io/) — **生态**。面向汽车的可扩展开放架构协作，关注云原生开发方式与车端部署之间的衔接。
- [Eclipse SDV Blueprints](https://github.com/eclipse-sdv-blueprints/blueprints) — **开源**。用具体场景组织多个 SDV 项目的集成示例，适合从“有哪些组件”走向“它们如何配合”。
- [ASAM Standards](https://www.asam.net/standards/) — **标准**。集中查找测量、标定、诊断、测试和仿真接口规范；XCP、MDF、ODX、XIL、OpenX 等应按各自用途选择。

<a id="platforms"></a>
## 整车软件平台与车载 Linux

- [Eclipse S-CORE](https://github.com/eclipse-score/score) — **开源**。面向车载高性能 ECU 的基础软件栈，适合研究模块划分、平台集成和安全工程材料；不要把项目目标等同于任意组合已经通过认证。
- [Eclipse Leda](https://github.com/eclipse-leda/leda) — **开源**。围绕嵌入式 Linux 组织 SDV 软件组件与集成环境，可作为研究车端应用部署的起点。
- [Automotive Grade Linux 文档](https://docs.automotivelinux.org/) — **文档**。AGL 的构建、平台和应用开发资料，适合了解车载 Linux 发行版的工程组织方式。
- [Android Automotive OS：Software-defined vehicle](https://source.android.com/docs/automotive/sdv) — **文档**。AOSP 的 SDV 架构入口，包含车载服务、虚拟化和多节点相关设计。AAOS 与手机投屏的 Android Auto 不是同一产品。
- [EWAOL](https://meta-ewaol.docs.soafee.io/en/latest/introduction.html) — **文档**。SOAFEE 的 Edge Workload Abstraction and Orchestration Layer 参考实现资料，涉及 Yocto、容器、编排与虚拟化；用于架构验证，不是完整量产交付。
- [Eclipse Automotive Integration for AutoSD](https://projects.eclipse.org/projects/automotive.autosd) — **开源**。围绕 AutoSD 镜像集成、运行和测试 Eclipse SDV 项目与 Blueprints，适合与其他集成发行版对照。

<a id="mcu"></a>
## MCU、区域控制器与实时系统

这部分保留 MCU 侧的基础软件、静态配置和实时调度，不默认所有控制功能都迁移到 Linux 或容器。

- [Eclipse OpenBSW](https://github.com/eclipse-openbsw/openbsw) — **开源**。面向 MCU 的 C++ 基础软件，包含生命周期、通信等组件与参考环境；不是完整 AUTOSAR Classic BSW 的替代声明。
- [FreeRTOS](https://github.com/FreeRTOS/FreeRTOS) — **开源**。MCU 实时内核与示例的入口，适合控制任务和平台原型；不能把 FreeRTOS 与单独的安全产品或认证包混为一谈。
- [Zephyr](https://github.com/zephyrproject-rtos/zephyr) — **开源**。具有驱动、协议栈和构建配置体系的嵌入式操作系统，可用于研究边缘节点的软件复用；目标芯片支持须逐项核对。
- [Eclipse ThreadX](https://github.com/eclipse-threadx/threadx) — **开源**。实时操作系统内核及其生态入口；安全相关采用需核对实际版本、目标平台和认证材料适用范围。
- [Trampoline RTOS](https://github.com/TrampolineRTOS/trampoline) — **开源**。采用静态配置、API 与 OSEK/VDX 及 AUTOSAR OS 对齐的 RTOS，适合学习汽车实时系统；不包含完整 AUTOSAR 基础软件栈。

<a id="autosar"></a>
## AUTOSAR 与接口建模

- [AUTOSAR Classic Platform](https://www.autosar.org/standards/classic-platform) — **标准**。传统深度嵌入式 ECU 的应用、RTE 与基础软件架构入口；公开规范与供应商交付的软件实现应分开理解。
- [AUTOSAR Adaptive Platform](https://www.autosar.org/standards/adaptive-platform) — **标准**。面向高性能计算 ECU 的服务和功能簇规范入口；不是 Classic 的简单升级版，二者可以在整车中共存。
- [Python AUTOSAR](https://github.com/cogu/autosar) — **开源**。用 Python 处理 AUTOSAR 模型和 ARXML 的工具，适合配置生成与自动化；不是 AUTOSAR OS、RTE 或通信栈。

<a id="virtualization"></a>
## 隔离、虚拟化与混合关键性

MCU 的 MPU/Guard、SoC 的 MMU/IOMMU、静态分区与时间调度是不同问题。以下项目不能据名称直接视为互换方案；MCU 商业方案见[商业平台](#commercial)。

- [Xen Project](https://xenproject.org/) — **开源**。虚拟机监控器与相关工程资料，适合研究多操作系统整合、设备隔离和嵌入式虚拟化。
- [seL4](https://sel4.systems/) — **开源**。具有形式化验证成果的微内核与系统构建生态；证明覆盖范围取决于平台和配置，不自动延伸到全部驱动与应用。
- [Bao Hypervisor](https://github.com/bao-project/bao-hypervisor) — **开源**。以静态分区为核心的轻量虚拟机监控器，适合研究嵌入式系统中的资源划分与隔离。
- [ACRN](https://github.com/projectacrn/acrn-hypervisor) — **开源**。面向嵌入式场景的虚拟化项目，主要围绕 x86 平台；移植性与设备模型需要单独评估。

<a id="middleware"></a>
## 服务通信与进程间通信

SOME/IP、DDS、共享内存 IPC 和跨车云协议不在同一个抽象层。选型应先确定通信范围、数据大小、实时约束和故障模型，再比较实现。

- [vsomeip](https://github.com/COVESA/vsomeip) — **开源**。SOME/IP 通信实现，适合研究车载服务发现、请求响应与事件通信。
- [CommonAPI C++ SOME/IP Runtime](https://github.com/COVESA/capicxx-someip-runtime) — **开源**。CommonAPI C++ 的 SOME/IP 运行时绑定，用于把接口层与底层通信实现衔接；还需配套生成工具。
- [Eclipse Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds) — **开源**。DDS 实现，适合数据分发与 QoS 相关工程实验；协议兼容不等于不同配置自动互通。
- [Fast DDS](https://github.com/eProsima/Fast-DDS) — **开源**。DDS/RTPS 实现，可用于分布式实时数据通信与相关工具链集成。
- [Eclipse iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2) — **开源**。以共享内存和零拷贝为重点的进程间通信框架；需核对所有权、内存生命周期和平台限制。
- [Eclipse Zenoh](https://github.com/eclipse-zenoh/zenoh) — **开源**。结合发布订阅、查询等机制的数据通信系统，可用于端侧到分布式系统的数据连接。
- [Eclipse uProtocol Specifications](https://github.com/eclipse-uprotocol/up-spec) — **标准**。与传输、设备和部署方式解耦的分层通信协议设计；这是规范仓库，不是某一种语言的完整运行时。
- [Eclipse eCAL](https://github.com/eclipse-ecal/ecal) — **开源**。面向本机与分布式系统的通信中间件，提供数据通信及监视、记录等配套能力。

<a id="vehicle-data"></a>
## 车辆数据、API 与应用开发

- [COVESA Vehicle Signal Specification（VSS）](https://github.com/COVESA/vehicle_signal_specification) — **标准**。统一车辆信号名称、层次和数据语义；VSS 是数据模型，不是总线协议，也不是整车访问权限方案。
- [VSS Tools](https://github.com/COVESA/vss-tools) — **开源**。校验、转换和生成 VSS 相关表示的工具，适合把信号模型接入工程流程。
- [Eclipse Kuksa Databroker](https://github.com/eclipse-kuksa/kuksa-databroker) — **开源**。围绕 VSS 组织车辆信号访问的数据服务，适合应用与底层信号之间的解耦实验。
- [Eclipse Kuksa CAN Provider](https://github.com/eclipse-kuksa/kuksa-can-provider) — **开源**。连接 CAN 信号与 Kuksa 数据服务的适配组件；DBC、映射和物理单位需要自行核对。
- [Eclipse Velocitas](https://github.com/eclipse-velocitas) — **开源**。车辆应用 SDK、模板和开发工具链的官方仓库集合，可作为信号驱动车辆应用的起点。
- [Eclipse Autowrx](https://github.com/eclipse-autowrx) — **开源**。digital.auto 相关的车辆功能原型开发与体验验证工具，适合在硬件完备前探索应用行为。

<a id="networks"></a>
## CAN、以太网与时间同步

- [can-utils](https://github.com/linux-can/can-utils) — **开源**。Linux SocketCAN 用户态工具，适合 CAN 报文收发、回放和台架调试。
- [python-can](https://github.com/hardbyte/python-can) — **开源**。统一多种 CAN 接口的 Python 库，便于自动化测试、采集和工具适配。
- [cantools](https://github.com/cantools/cantools) — **开源**。CAN 数据库解析、编解码与代码生成工具，适合从 DBC 等描述进入信号级测试。
- [canmatrix](https://github.com/ebroecker/canmatrix) — **开源**。处理、比较与转换 CAN 通信矩阵，适合不同工具之间的数据交接。
- [Linux PTP](https://www.linuxptp.org/) — **开源**。Linux 上的 PTP 时间同步工具；实际精度依赖硬件时间戳、时钟、网络拓扑和配置。
- [IEEE 802.1 TSN Task Group](https://1.ieee802.org/tsn/) — **标准**。时间敏感网络的官方标准化入口；“支持 TSN”必须细化到具体机制和设备能力。
- [OPEN Alliance](https://opensig.org/) — **生态**。车载以太网相关规范、互操作与测试工作入口，可与 IEEE 网络标准配合阅读。

<a id="diagnostics"></a>
## 诊断、日志、测量与标定

- [udsoncan](https://github.com/pylessard/python-udsoncan) — **开源**。Python UDS 协议库，适合诊断客户端与台架脚本；传输层和 ECU 服务行为需另行配置。
- [python-doipclient](https://github.com/jacobschaer/python-doipclient) — **开源**。DoIP 客户端，可与 UDS 工具衔接，用于以太网上的诊断通信实验。
- [odxtools](https://github.com/mercedes-benz/odxtools) — **开源**。处理 ODX 诊断描述的 Python 工具，适合把诊断数据转化为可查询、可调用的工程对象。
- [asammdf](https://github.com/danielhrisca/asammdf) — **开源**。读取、处理与转换 MDF 测量文件，适合采集数据分析和测试结果归档。
- [XCPlite](https://github.com/vectorgrp/XCPlite) — **开源**。轻量 XCP 实现，适合为应用增加测量和标定接口；不同传输与集成功能以项目文档为准。
- [COVESA DLT Daemon](https://github.com/COVESA/dlt-daemon) — **开源**。Diagnostic Log and Trace 日志服务，可用于车载软件日志汇集与分析链。
- [Eclipse OpenSOVD](https://projects.eclipse.org/projects/automotive.opensovd) — **开源**。面向服务化车辆诊断的 SOVD 实现项目入口，可与传统 UDS/DoIP 路径对照研究。

<a id="ota"></a>
## OTA 与软件更新安全

更新包分发、安装、签名验证、密钥管理、回退和多 ECU 一致性是不同职责。以下组件不应直接拼成“完整整车 OTA 已就绪”的结论。

- [Uptane](https://uptane.org/) — **标准**。面向车辆软件更新的安全框架与规范，重点是更新信任关系与攻击防护；不是可直接安装的 OTA 客户端。
- [python-tuf](https://github.com/theupdateframework/python-tuf) — **开源**。The Update Framework 的 Python 实现，可用于理解安全更新元数据与信任机制；不等同于完整 Uptane 实现。
- [RAUC](https://github.com/rauc/rauc) — **开源**。嵌入式 Linux 更新框架，围绕签名更新包和系统安装流程组织能力。
- [SWUpdate](https://github.com/sbabic/swupdate) — **开源**。可配置的嵌入式软件更新框架，适合不同存储布局和安装方式的工程集成。
- [Eclipse hawkBit](https://github.com/eclipse-hawkbit/hawkbit) — **开源**。软件更新分发与设备更新管理后端；车辆端的安全安装策略仍需独立设计。

<a id="orchestration"></a>
## 车端编排与车云协同

- [Eclipse Ankaios](https://github.com/eclipse-ankaios/ankaios) — **开源**。面向嵌入式环境的工作负载管理，适合研究跨节点应用启动、停止和配置。
- [Eclipse BlueChi](https://github.com/eclipse-bluechi/bluechi) — **开源**。通过 systemd/D-Bus 管理多节点服务；它首先是服务控制器，不应直接等同于容器运行时。
- [Eclipse Kanto](https://github.com/eclipse-kanto) — **开源**。嵌入式与边缘设备的容器、设备管理和云连接组件集合。
- [Eclipse Symphony](https://github.com/eclipse-symphony/symphony) — **开源**。分布式与边缘场景的应用编排框架，可用于研究期望状态、部署和多环境管理。

<a id="simulation"></a>
## 虚拟 ECU、SIL/HIL 与联合仿真

- [Vector SIL Kit](https://github.com/vectorgrp/sil-kit) — **开源**。连接虚拟 ECU、网络和仿真参与者的库；它是仿真通信与协同基础，不是车辆物理模型本身。
- [Eclipse OpenXilEnv](https://github.com/eclipse-openxilenv/openxilenv) — **开源**。支持在 PC 上运行和测试嵌入式功能的 SIL/HIL 环境，可用于早期控制软件验证。
- [Eclipse openDuT](https://github.com/eclipse-opendut/opendut) — **开源**。面向分布式测试设备和网络环境的测试基础设施，适合组织跨地点 ECU 台架。
- [Renode](https://github.com/renode/renode) — **开源**。嵌入式系统仿真与自动化测试工具；外设和芯片支持依赖具体模型。
- [QEMU](https://www.qemu.org/) — **开源**。系统仿真与虚拟化工具，可用于软件启动、平台实验和自动化；功能仿真不等于周期精确仿真。
- [Functional Mock-up Interface（FMI）](https://fmi-standard.org/) — **标准**。模型交换与联合仿真的接口规范，是连接不同仿真工具的重要入口。
- [FMPy](https://github.com/CATIA-Systems/FMPy) — **开源**。使用 Python 检查和运行 FMU，适合把联合仿真接入批量实验与回归测试。

<a id="supply-chain"></a>
## 构建、软件物料清单与供应链

- [Yocto Project](https://www.yoctoproject.org/) — **生态**。构建定制嵌入式 Linux 发行版的工具与协作项目，适合理解车载镜像、BSP 和软件包集成。
- [Syft](https://github.com/anchore/syft) — **开源**。从容器镜像和文件系统生成软件物料清单（SBOM），可用于发布归档与依赖清点；不是安全认证工具。
- [SPDX](https://spdx.dev/) — **标准**。软件物料清单、许可与供应链信息的交换标准及生态，适合在供应商交付中使用统一表示。

<a id="safety"></a>
## 功能安全、网络安全与开发过程

只链接权利方或标准组织的公开入口。项目采用时，应确认适用版本、法规辖区与具体交付要求，不以这份清单替代合规审查。

- [ISO 26262 系列入口：Part 1](https://www.iso.org/standard/68383.html) — **标准**。道路车辆功能安全；此链接为术语部分，可沿官方页面进入其他部分，不应只读 Part 1 代替完整安全生命周期要求。
- [ISO/SAE 21434](https://www.iso.org/standard/70918.html) — **标准**。道路车辆网络安全工程，关注全生命周期的网络安全风险管理。
- [ISO 21448（SOTIF）](https://www.iso.org/standard/77490.html) — **标准**。预期功能安全，适合与功能失效导致的风险区分研究，尤其涉及感知与驾驶辅助时。
- [Automotive SPICE](https://vda-qmc.de/en/automotive-spice/) — **标准**。汽车软件与系统开发过程评估的官方入口；过程能力评价不是整车功能安全认证。
- [Eclipse Trustable Software Framework](https://projects.eclipse.org/projects/technology.tsf) — **开源**。组织可信软件工程实践、风险与证据的框架，适合研究如何让工程结论可追溯；不是 ISO 26262 的替代规范。

<a id="hmi"></a>
## 座舱接口与嵌入式 HMI

- [Android Automotive Vehicle HAL](https://source.android.com/docs/automotive/vhal) — **文档**。车辆属性的读取、写入和订阅接口，适合理解 Android 侧应用与车辆能力之间的边界；属性接口不代替底层控制安全设计。
- [LVGL](https://github.com/lvgl/lvgl) — **开源**。面向嵌入式设备的图形库，可用于小屏、仪表或控制面板原型；安全显示链与商业工具需分别评估。

<a id="adas"></a>
## 相邻领域：自动驾驶与场景仿真

只保留与车辆软件集成、数据通信和测试关系较近的入口，不在这里复制一整份感知论文或数据集大全。

- [Autoware](https://github.com/autowarefoundation/autoware) — **开源**。自动驾驶软件栈，可作为复杂车载应用集成、传感器数据链和中间件使用的研究对象。
- [Apollo](https://github.com/ApolloAuto/apollo) — **开源**。自动驾驶平台，包含相关应用模块和工程工具；采用时需分别核对代码、数据及硬件条件。
- [CARLA](https://github.com/carla-simulator/carla) — **开源**。自动驾驶研究仿真器，适合传感器与驾驶场景实验，不代替实车安全验证。
- [esmini](https://github.com/esmini/esmini) — **开源**。轻量 OpenSCENARIO 场景执行工具，适合场景文件检查与批量测试；支持范围以项目说明为准。
- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo) — **开源**。交通流仿真系统，适合研究车辆与交通环境交互，而非 ECU 指令级仿真。
- [Open Simulation Interface（OSI）](https://github.com/OpenSimulationInterface/open-simulation-interface) — **标准**。仿真环境与自动驾驶功能之间的数据接口，适合传感器和环境信息交换。

<a id="ev"></a>
## 相邻领域：电池与充电

- [foxBMS 2](https://github.com/foxBMS/foxbms-2) — **开源**。电池管理系统研发平台，可用于研究 BMS 硬件、基础软件与控制功能；高压实验需独立安全措施。
- [EVerest](https://github.com/EVerest/EVerest) — **开源**。电动汽车充电软件生态，重点在充电设施侧；与车端通信相关，但不是车载操作系统。

<a id="commercial"></a>
## 商业平台与工程工具

以下条目用于了解可采购方案及其与开源组件的边界，**不列入纯开源实现**。免费试用、公开示例或可见部分源码，不等于整个产品开源。价格、目标芯片、许可方式、认证版本与可交付材料，以厂商实际合同和文档为准。

- [ETAS RTA-CAR / RTA-HVR](https://www.etas.com/ww/en/products-services/vehicle-software-platform/autosar-classic-profile-rta-car/rta-car-details-integration/) — **商业**。AUTOSAR Classic 基础软件与集成方案；其中 RTA-HVR 面向具备硬件虚拟化支持的 MCU，提供 ECU 分区能力。
- [Vector MICROSAR Classic](https://www.vector.com/en/product/microsar-classic/) — **商业**。AUTOSAR Classic 基础软件与配置集成方案，可用于对照开源工具和实际量产 BSW 交付的差别。
- [Vector MICROSAR Hypervisor](https://www.vector.com/en/product/microsar-hypervisor/) — **商业**。面向汽车 MCU 的软件隔离与虚拟化方案；具体硬件支持、分区方式与安全要求需逐项确认。
- [Elektrobit EB tresos](https://www.elektrobit.com/products/ecu/eb-tresos/) — **商业**。汽车 ECU 基础软件、实时系统与配置工具产品族，适合研究 Classic 平台的工程工作流。
- [QNX Hypervisor / Hypervisor for Safety](https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety) — **商业**。面向多操作系统整合的嵌入式虚拟化产品；普通版、安全版及其认证适用范围应分别核对。
- [Vector CANoe](https://www.vector.com/en/product/canoe/) — **商业**。网络、ECU 和分布式软件的开发与测试工具，支持 SIL/HIL 等工作流；功能取决于具体版本与选件。
- [dSPACE VEOS](https://www.dspace.com/en/inc/home/products/sw/simulation_software/veos.cfm) — **商业**。在 PC 上集成模型、虚拟 ECU 和网络通信的仿真平台，适合早期软件验证与联合仿真。
- [Qt for MCUs](https://doc.qt.io/QtForMCUs/) — **商业**。面向 MCU 的图形界面开发产品与文档；不要套用其他 Qt 模块的开源许可来推断其授权方式。

<a id="related"></a>
## 相关 Awesome Lists 与致谢

以下清单用于发现候选项目和校对分类。本仓库重新组织为 SDV 工程视角，中文说明独立撰写；不整表搬运，也不把旧清单当作项目仍在维护的证明。

- [awesome-automotive · Marcin214](https://github.com/Marcin214/awesome-automotive) — **清单**。汽车嵌入式、AUTOSAR、通信、诊断、安全与工程工具的综合入口，是本仓库基础分类的重要参考。
- [Awesome-Automotive · ajay-bhojani](https://github.com/ajay-bhojani/Awesome-Automotive) — **清单**。覆盖面较广的汽车工程学习路线，用于检查 SDV 与相邻领域之间的遗漏。
- [awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) — **清单**。车辆安全研究、协议和测试资源；实验应限定在自有或获得授权的隔离环境。
- [Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded) — **清单**。嵌入式操作系统、工具链与开发资料，用于补充 MCU 和实时软件基础。
- [awesome-canbus](https://github.com/iDoka/awesome-canbus) — **清单**。CAN 总线工具、设备与学习资源，适合进一步查找台架调试方案。
- [awesome-linbus](https://github.com/iDoka/awesome-linbus) — **清单**。LIN 总线相关资源，补充区域控制器与边缘执行器网络的阅读入口。
- [awesome-autonomous-vehicles](https://github.com/manfreddiaz/awesome-autonomous-vehicles) — **清单**。自动驾驶软件、仿真与数据资源；作为相邻专题引用，不在本仓库重复铺开。
- [awesome-ros2](https://github.com/fkromer/awesome-ros2) — **清单**。ROS 2 生态资源，用于扩展中间件、机器人及自动驾驶集成方向。
- [Awesome](https://github.com/sindresorhus/awesome) — **清单**。Awesome 清单的组织与贡献规范参考。本仓库未声称已被该总目录收录。

<!-- catalog:end -->

## 参与维护

欢迎提交有明确用途的项目、标准入口、失效链接修正与分类改进。每次贡献应说明“解决什么问题”“为什么与 SDV 相关”，并给出上游依据。详情见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本轮的核验范围、已发现的链接迁移和仍待补充的主题见 [docs/REVIEW.md](docs/REVIEW.md)。检查脚本只帮助发现格式、重复和链接问题，不替代人工阅读或工程验证。

## 许可

本仓库原创说明与维护脚本采用 [MIT License](LICENSE)。链接指向的代码、标准、文档、商标与其他材料仍遵循各自许可；这里的许可不改变上游权利。
