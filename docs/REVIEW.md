# 来源与核验说明

整理日期：2026-10-08。范围：首次建立 Awesome SDV，不是完整行业普查或可采购产品评测。

## 本轮如何整理

先从相关 Awesome Lists 发现分类和候选资源，再阅读项目官方 README、项目网站、标准组织或厂商页面。主清单中每个条目的链接同时也是该条简短说明的上游依据。中文描述重新撰写，没有复制其他清单的完整段落。

本轮形成 **101 个条目、19 个分类**。其中 9 个条目是相关清单，8 个是单独列出的商业资源；其余 84 个为开源项目、标准、文档与生态入口。数量是维护统计，不是覆盖率或质量排名。

## 参考清单

| 来源 | 参考用途 |
| --- | --- |
| [Marcin214/awesome-automotive](https://github.com/Marcin214/awesome-automotive) | 汽车嵌入式、AUTOSAR、网络、诊断与工程工具分类 |
| [ajay-bhojani/Awesome-Automotive](https://github.com/ajay-bhojani/Awesome-Automotive) | 汽车工程学习路线与相邻领域查漏 |
| [jaredthecoder/awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) | 车辆安全研究与授权测试资源 |
| [nhivp/Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded) | MCU、RTOS 与嵌入式工具链 |
| [iDoka/awesome-canbus](https://github.com/iDoka/awesome-canbus) | CAN 工具与工程资料 |
| [iDoka/awesome-linbus](https://github.com/iDoka/awesome-linbus) | LIN 与边缘节点通信 |
| [manfreddiaz/awesome-autonomous-vehicles](https://github.com/manfreddiaz/awesome-autonomous-vehicles) | 自动驾驶与仿真相邻专题 |
| [fkromer/awesome-ros2](https://github.com/fkromer/awesome-ros2) | ROS 2 中间件和集成生态 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 清单组织和贡献方式；不表示本仓库已被总目录接收 |

这些清单负责提供发现线索，不替代一手来源。没有机械合并它们的所有链接，也没有复制或镜像其内容。

## 重要的一手入口

[Eclipse SDV 官方项目目录](https://eclipsesdv.org/projects/)用于确认项目归属及集成、运行时、诊断和测试等分工；具体能力尽量回到各自项目文档。

[AOSP SDV](https://source.android.com/docs/automotive/sdv)与[VHAL 文档](https://source.android.com/docs/automotive/vhal)用于区分平台架构和车辆属性接口。[SOAFEE](https://www.soafee.io/)及[EWAOL 参考文档](https://meta-ewaol.docs.soafee.io/en/latest/introduction.html)用于理解云端开发与车端部署路径。

[COVESA VSS](https://github.com/COVESA/vehicle_signal_specification)、[uProtocol 规范](https://github.com/eclipse-uprotocol/up-spec)、[Uptane](https://uptane.org/)和[FMI](https://fmi-standard.org/)按规范或框架收录，未误标成完整应用实现。

[ISO 26262 Part 1](https://www.iso.org/standard/68383.html)、[ISO/SAE 21434](https://www.iso.org/standard/70918.html)、[ISO 21448](https://www.iso.org/standard/77490.html)及[VDA QMC Automotive SPICE](https://vda-qmc.de/en/automotive-spice/)使用权利方页面；未下载、复制或分发收费标准正文。

## 链接迁移与访问限制

| 情况 | 本轮处理 |
| --- | --- |
| EVerest 的 `EVerest/everest-core` 入口跳转到 `EVerest/EVerest` | README 使用实际跳转后的[仓库地址](https://github.com/EVerest/EVerest) |
| QNX 的旧 `blackberry.qnx.com` 产品链接跳转到 `qnx.software` | README 使用[新的 Hypervisor 产品页](https://qnx.software/en/software/products-and-solutions/qnx-hypervisor-and-hypervisor-for-safety) |
| AUTOSAR Classic / Adaptive 官方页面在直接抓取时超时 | 保留官方链接，依据已检索到的官方页面内容描述；不把超时判断为失效，也不标注 HTTP 全量检查通过 |
| AutoSD 的部分文档域名未能成功读取 | 使用已成功读取的[Eclipse AutoSD 集成项目页](https://projects.eclipse.org/projects/automotive.autosd)，未把未读内容当证据 |
| UNECE、MISRA 的部分候选入口未成功读取 | 未补写未经本轮核对的版本、适用日期或条文内容，留待后续补充 |

## 核验边界

**已做：** 阅读候选来源，按用途分类，区分代码、规范、文档和商业产品，核对上述迁移，检查 README 格式与重复资源，并测试维护脚本。机器可复核的离线结果见 [validation.json](validation.json)。

**未做：** 对所有上游仓库逐版本进行许可证法律审查、持续维护状态审计、编译、性能测试、互操作测试、台架或实车验证。也没有运行全量外部 HTTP 探测，不能据此声称所有链接始终可访问。

“开源”标签依据上游项目公开定位，不代表其全部依赖、数据或商业配套已完成许可清查。若官方宣传与可取得的交付物存在差异，应在采用前进一步核查。

## 后续补充方向

以下只是待研究的覆盖缺口，不计入已收录资源：

| 方向 | 补充前需要确认 |
| --- | --- |
| UNECE R155/R156 与相关中国标准 | 官方正文入口、修订状态、适用范围，避免混用标准与法规 |
| 安全启动、HSM 固件、密钥与证书生命周期 | 目标平台、可用代码、许可及威胁模型 |
| 中央计算与区域架构的模型驱动设计 | 可取得的工具、接口及完整示例，而非只有架构宣传图 |
| AUTOSAR Adaptive 商业实现与国产基础软件 | 可核实产品资料、平台支持和授权边界 |
| TSN、车载以太网与 MCU 虚拟化的实测资料 | 原始配置、测试方法、硬件条件与失败结果 |
| 热管理、车身、底盘等控制应用 | 可用参考实现、合法数据、实时性和安全边界 |

没有设定每日凑数更新、自动收录或自动同步上游源码的任务。
