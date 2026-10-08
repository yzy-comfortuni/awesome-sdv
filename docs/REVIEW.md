# 来源与补充记录

审阅日期：2026-10-08。基线为 [fe7a070](https://github.com/yzy-comfortuni/awesome-sdv/tree/fe7a070ddb5da924efe95e33474a21133081179a)，包含 101 个条目、19 个分类。本轮针对 Rust、DDS、国产工具和开发验证工具的遗漏补充，并重写 README。

## 改了什么

主清单现有 **158 个条目、24 个分类**，净增 **57 个条目**。商业产品移入各自工程分类，不再集中到文末。原来的 `commercial` 锚点保留，指向标签与授权说明；其余原有分类锚点继续保留。

新增内容按下表归入正文。README 每条的主链接同时是其功能说明的上游入口；表中补充了授权或背景依据。

| 方向 | 本轮补充 | 主要来源与处理 |
| --- | --- | --- |
| Rust | Embedded Rust Book、embedded-hal、Embassy、RTIC、probe-rs、defmt、CXX、Ferrocene、HighTec、Safety-Critical Rust Coding Guidelines | 官方书籍和各项目仓库；[Ferrocene](https://ferrocene.dev/) 区分源代码与鉴定发行包，[HighTec](https://hightec-rt.com/rust) 标为商业工具链 |
| DDS | OMG DDS、RTI Connext Drive、OpenDDS、RustDDS、Dust DDS、Micro XRCE-DDS、RTI Perftest | [RTI 产品页](https://www.rti.com/products/connext-drive) 与各项目 README；不把开源 Perftest 的许可扩大到所依赖的 Connext 库 |
| 总线工具 | TSMaster、ZXDoc、INTEWORK-VBA、BUSMASTER、SavvyCAN、Wireshark | [同星产品页](https://www.tosunai.com/product/tsmaster/) 和 [Professional 授权说明](https://www.tosunai.com/product/tsmaster-professional/)、[致远产品页](https://www.zlg.cn/carbustools/carbustools/product/id/382.html)、[恒润公告](https://www.hirain.com/news_detail/478.html)；不将免费下载写成开源 |
| 国产基础软件 | RT-Thread、EasyXMen、NeuSAR、INTEWORK-EAS-CP/AP、ORIENTAIS | [EasyXMen 代码仓库](https://atomgit.com/easyxmen/XMen) 标明 LGPL-2.1 和例外条款；[NeuSAR](https://www.neusar.com/) 与 [普华产品目录](https://www.i-soft.com.cn/product/vehicle.html) 提供商业产品说明 |
| 建模与代码生成 | Capella、PREEvision、Simulink、Embedded Coder、OpenModelica、MWORKS.Sysplorer、APP4MC | 官方产品和项目资料；分别列出模型环境、代码生成和系统架构工具 |
| 标定与测试 | CANape、INCA、SCALEXIO、VeriStand、INTEWORK-TAE | 厂商产品页；与现有诊断库、VEOS 和 SIL Kit 放在对应分类 |
| 调试与分析 | TRACE32、VectorCAST、Polyspace、CBMC、Frama-C、Kani、TA Tool Suite | 产品页和项目仓库；测试、静态分析、形式化验证与时序分析不混写为同一能力 |
| 系统与交付 | QNX SDP、iceoryx、MCUboot、OP-TEE、Buildroot、CycloneDX、OSS Review Toolkit、MISRA | 官方文档与项目入口；保留已有 iceoryx2，两者是独立代码项目 |
| 相关清单 | Awesome Embedded Rust | 与原有汽车、嵌入式和总线清单交叉检查分类，不整表搬运 |

## 参考清单与写作指南

本轮回读了 [Marcin214/awesome-automotive](https://github.com/Marcin214/awesome-automotive)、[ajay-bhojani/Awesome-Automotive](https://github.com/ajay-bhojani/Awesome-Automotive)、[awesome-canbus](https://github.com/iDoka/awesome-canbus) 和 [Awesome Embedded Rust](https://github.com/rust-embedded/awesome-embedded-rust)。前者的建模、开发和验证分类提示了首版只偏重运行时组件的问题。其余首版参考清单继续保留在 README。

文字参考用户指定的 [Awesome AI Taste](https://github.com/yzy-comfortuni/awesome-ai-taste)，并实际阅读 [Humanizer-zh](https://github.com/op7418/Humanizer-zh/blob/main/SKILL.md) 与 [中文技术文档写作规范：文本](https://github.com/ruanyf/document-style-guide/blob/master/docs/text.md)。删除空泛用途、重复提醒和宣传语，保留会改变选型判断的功能、架构与授权差异。贡献指南加入了条目修改示例。

## 链接修正与访问限制

| 情况 | 处理 |
| --- | --- |
| Embedded Rust Book 旧地址跳转 | 使用 `docs.rust-embedded.org/book/` |
| RustDDS 旧个人仓库入口未能读取 | 已读取当前 `Atostek/RustDDS`，使用维护方仓库 |
| Rust 安全关键指南迁移到 Safety-Critical-Rust-Consortium | 使用当前组织地址，不保留旧重定向入口 |
| APP4MC、MCUboot、NI VeriStand 页面重定向 | 使用本轮实际返回的项目或产品地址 |
| 经纬恒润页面直接抓取返回 403 或失败 | 使用检索返回的厂商页面摘要确认产品定位，仅写摘要支持的功能；没有声称读取完整手册 |
| MWORKS 产品页为动态页面 | 功能说明来自检索返回的同元官方产品页内容；不声称已下载或运行工具 |
| MISRA 首页直接抓取失败 | 保留官方域名，依据官方检索摘要收录，不写未经核对的最新版本或条文 |
| 同星 API 的候选 GitHub 地址未读到可核验内容，文档站为动态页面 | 不把猜测的仓库地址写入清单；TSMaster 的脚本能力依据厂商产品说明与培训资料 |
| Eclipse SommR 的候选资料包含开发计划及 IP 等待说明 | 本轮未作为可直接使用的成熟实现收录，避免把计划当交付物 |

## 检查范围

本地复原的检查脚本与原测试文件已通过 Git blob SHA-1 对照，确认与基线一致。运行 README 离线检查及 21 项原有回归测试，结果见 [validation.json](validation.json) 和 [unit-tests.txt](unit-tests.txt)。测试验证文档检查器，不验证所收录的 SDV 软件。

没有运行全量外部 HTTP 扫描，没有逐一编译上游项目，也没有进行许可法律审查、性能、互操作、台架或实车测试。新条目的来源阅读与原有条目的文字修订分开记录，不能据本次日期推断旧条目已全部重新审计。远端文件的写入结果另以 Git 提交和回读对象为准。

## 仍需专题补充

中国汽车标准及 UNECE R155/R156 的现行正文入口、AUTOSAR 之外的车规芯片 SDK 与 HSM 交付物、需求追踪与软件发布管理、车身/底盘/热管理的可运行控制样例，以及总线和虚拟化方案的真实互操作记录，仍值得继续整理。本轮未将这些方向计入已收录条目。
