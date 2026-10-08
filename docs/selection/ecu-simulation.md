# ECU 开发与仿真：先问运行的是什么

[资源目录](../../README.md#simulation) · [选型笔记](README.md) · ComfortUni（适宇科技）及贡献者

资料查阅：2026-10-08。以下依据上游文档说明交付物与接入方式，建议用例尚未作为本仓库的运行结果发布。

## 不同工具接收不同材料

| 已有材料 | 进入哪条路径 |
| --- | --- |
| MCU 应用源码，需要基础组件或主机参考环境 | [OpenBSW](#openbsw) |
| AUTOSAR 配置模型，需要生成 ARXML | [Python AUTOSAR](#python-autosar) |
| 多个虚拟 ECU 或模型，需要连接网络和仿真时间 | [SIL Kit](#sil-kit) |
| 可重新编译的控制源码，需要主机测量和激励 | [OpenXilEnv](#openxilenv) |
| 目标固件或系统镜像，需要执行其机器码 | [Renode](#renode)、[QEMU](#qemu)；取决于目标机器与外设模型 |
| 外部工具交付了 FMU，需要接入或批量运行 | [FMI](#fmi) 确认接口类型，[FMPy](#fmpy) 检查与执行 |

<a id="openbsw"></a>
## OpenBSW：先跑主机参考应用，再看 MCU 适配

OpenBSW 的参考应用同时覆盖 POSIX 与 S32K148 路径。官方例子提供周期 CAN 报文以及诊断等功能；ADC、PWM 等板级例子则依赖对应硬件。这让通信与应用组织可以先在主机学习，而驱动和实时性检查留到板上。[参考应用](https://eclipse-openbsw.github.io/openbsw/sphinx_docs/executables/referenceApp/application/doc/index.html) · [Ubuntu 主机环境](https://eclipse-openbsw.github.io/openbsw/sphinx_docs/doc/dev/learning/setup/setup_env_host_ubuntu.html)

可先按参考环境检查 ID `0x558` 的周期计数报文，再换自己的应用模块。移到目标 MCU 时列出时钟、外设、引导和任务时序的差异；POSIX 上跑过的业务代码，与板级支持完成是两项不同交付。

<a id="python-autosar"></a>
## Python AUTOSAR：配置模型工具，不是 ECU 运行时

Python AUTOSAR 用 Python 创建、处理 AUTOSAR 模型并生成 ARXML，适合自动生成重复配置。当前仓库提示 v0.5 与 v0.4 的 API 不兼容，ReadTheDocs 对应旧版；新工程应按所选版本使用仓库示例，不能混用教程。它的输出是模型文件，不是可直接烧录的 RTE 或 BSW。[版本说明与示例](https://github.com/cogu/autosar)

从一个接口或数据类型生成最小 ARXML，导入团队实际使用的配置工具，再导出比较引用、命名空间和类型约束。把“XML 格式有效”与“目标工具保留了预期语义”分别验证，尤其要记录双方 AUTOSAR schema 版本。

<a id="sil-kit"></a>
## Vector SIL Kit：连接仿真参与者，而不是提供所有 ECU 模型

SIL Kit 提供虚拟网络、参与者生命周期和仿真时间协调。它把已有应用、虚拟 ECU 或仿真模型接起来；系统行为仍来自接入的参与者或网络模型。仿真时间与墙钟时间的组织方式也会影响结果解释。[仿真概念与组成](https://vectorgrp.github.io/sil-kit-docs/simulation/simulation.html) · [文档与示例](https://vectorgrp.github.io/sil-kit-docs/)

先连接两个参与者，让一个定时发送、另一个检查序号与时间；再加入实际模型。保存参与者配置、生命周期模式和步进约定，区分“收到消息”“按期完成虚拟步长”以及“满足真实时间期限”。

<a id="openxilenv"></a>
## OpenXilEnv：将可编译的控制代码接成主机进程

OpenXilEnv 当前以 SIL 为重点，外部组件可编成独立进程，通过提供的接口和主机通信。它有 GUI、命令行、变量测量、A2L/XCP 等能力；与执行目标机器码的仿真器相比，这条路径先要求源码及主机编译适配。官方仓库提供 `Samples/ExternalProcesses/ExtProc_Simple` 起步示例。[架构、示例与构建](https://github.com/eclipse-openxilenv/openxilenv)

先暴露一个输入变量和一个输出变量，再运行固定步长激励，检查变量类型与更新时间。对只能取得原始固件的第三方 ECU，这与 Renode/QEMU 的评估路径不同；浮点、整数宽度和编译器行为差异也要在主机与目标之间留对照样例。

<a id="renode"></a>
## Renode：把固件启动行为写成自动测试

Renode 在机器与外设模型上运行嵌入式固件，官方测试教程使用 Robot Framework，支持通过 `renode-test` 执行测试，并产出日志、报告和 XML 结果。串口输出、网络消息等可成为自动验收点。[自动测试教程](https://renode.readthedocs.io/en/latest/introduction/testing.html)

先确认目标板的模型，再写“启动固件 → 等待指定串口输出 → 检查一个外设行为”的最小测试。保留固件、平台描述、启动脚本与结果文件。串口测试通过能验证这条启动路径，但未建模的外设以及实际板上时间特性仍需另外处理。

<a id="qemu"></a>
## QEMU：先匹配 machine，再谈 CPU 架构

QEMU 的系统仿真运行由 CPU、内存与设备组成的目标机器。选型时，CPU 指令集只是入口，固件依赖的板级设备、启动方式和地址映射同样关键；支持某一架构并不等于已有某款车规 MCU 的完整机器模型。[系统仿真与目标机器文档](https://www.qemu.org/docs/master/system/index.html)

对已有支持的系统镜像，先验证启动日志与软件服务，再接入网络或测试流程。对 MCU 固件，先列出固件访问的外设和内存区域，判断已有模型能覆盖多少。用这条路径做软件功能回归时，不将执行速度直接当成目标芯片的 WCET。

<a id="fmi"></a>
## FMI：FMU 后缀相同，求解职责可能不同

FMI 3.0.2 区分 Model Exchange、Co-Simulation 和 Scheduled Execution：ME 由导入环境承担求解；CS 封装内部推进方式，由外部协调交换；SE 让外部调度器激活模型分区。拿到 FMU 后应先读 `modelDescription.xml`，而不是仅凭后缀选择工具。[FMI 3.0.2 规范](https://fmi-standard.org/docs/3.0.2/)

交接时确认 FMI 版本、接口类型、目标平台二进制、变量单位与步长约定。可先用恒定输入和一次阶跃生成参考输出，再做联合仿真；算法误差、耦合误差和接口使用错误应分开定位。本页使用 3.0.2 解释语义，不宣称所有收录工具都支持其全部接口。

<a id="fmpy"></a>
## FMPy：检查和运行 FMU，不负责生成原始物理模型

FMPy 提供 Python、命令行和图形入口；教程展示 `dump` 检查 FMU 信息，再用 `simulate_fmu` 运行。它适合把外部模型接进批量实验、参数扫描或回归测试，前提是模型的 FMI 接口和平台二进制被当前版本支持。[教程与 Python 示例](https://fmpy.readthedocs.io/en/latest/tutorial/)

先记录 FMU 的 hash、接口类型与变量清单，再用固定输入和结束时间运行一个短样例。比较输出时间轴、单位和事件附近的采样点；对参数扫描保存每组输入与完整配置。收到未知来源的 FMU 时，按可执行代码处理其二进制，而不将其视为纯数据文件。

---

文档采用 [CC BY 4.0](../../LICENSE)，署名与来源见 [ATTRIBUTION.md](../../ATTRIBUTION.md)。
