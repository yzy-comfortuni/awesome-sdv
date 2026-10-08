# 总线、诊断与测量：工具之间怎样分工

[资源目录](../../README.md#bus-tools) · [选型笔记](README.md) · ComfortUni（适宇科技）及贡献者

资料查阅：2026-10-08。功能说明链接到官方资料；下文的试用流程是评估建议，未在这些商业软件或真实 ECU 上执行。

## 先看输入和输出

| 手头材料与目标 | 对应工具 |
| --- | --- |
| 接口卡、通信数据库，需要交互分析、仿真和测试 | [TSMaster](#tsmaster)、[ZXDoc](#zxdoc)、[INTEWORK-VBA](#vba)、[CANoe](#canoe) |
| 用 Python 收发原始 CAN 帧 | [python-can](#python-can)；信号解释交给 [cantools](#cantools) |
| 从 DBC 得到信号值或 C 编解码函数 | [cantools](#cantools) |
| 已有 MDF/MF4 记录，需要裁剪、对齐和导出 | [asammdf](#asammdf) |
| 按 ECU 的 DID 定义读取诊断数据 | [udsoncan](#udsoncan)；以太网传输可接 [python-doipclient](#doip) |

<a id="tsmaster"></a>
## TSMaster：把数据库、脚本和功能授权一起试

TSMaster 可导入 DBC、LDF 等数据库，用 C/Python 扩展仿真与测试；官方资料提供 BLF 记录、回放及 ASC/MAT 转换。它还列出多家接口厂商的支持，已有设备的团队可先检查驱动与具体型号，减少为了换软件而重买接口卡的风险。[产品功能](https://www.tosunai.com/product/tsmaster/) · [文档站](https://docs.tosunai.com/)

试用时带一份真实数据库、一段记录和一个现有测试脚本，依次完成信号解析、定时发送、记录回读。随后逐项询价诊断、刷写、CCP/XCP 和脚本发布所需的版本与选件。官网有基础、Standard、Professional 等资料，免费下载范围不能代替所需功能的授权清单。[Standard](https://www.tosunai.com/product/tsmaster-standard/) · [Professional](https://www.tosunai.com/product/tsmaster-professional/)

<a id="zxdoc"></a>
## ZXDoc：留意数据库转换和记录交接

ZXDoc 与致远接口硬件配套，支持 CAN/CAN FD、LIN 和车载以太网，提供 Python 扩展与外部 API。对于基于 DBC 信号的 ARXML，官方页面要求先转换成 DBC 再解析；SOME/IP 的 ARXML 导入另列。已有 AUTOSAR 数据库时，需要按这两条路径分别试验，不能只看“支持 ARXML”标签。记录格式包括 ASC、BLF、MAT、MF4。[数据库、记录与二次开发说明](https://www.zlg.cn/carbustools/carbustools/product/id/382.html)

选取包含复用信号、不同字节序和缩放的数据库做转换，检查信号名称、单位与数值是否保留，再将导出记录交给下一环节读取。转换格式与原生保留全部模型语义不是一回事，迁移成本应由实际工程文件决定。

<a id="vba"></a>
## INTEWORK-VBA：从配置教程进入，比读新闻页有效

INTEWORK-VBA 的官方站点提供 TestBase VCI 介绍、以太网标定配置、标定故障定位，以及 ECUTest 调用 VBA 的操作资料。对已有自动化台架，外部测试系统如何调用软件、如何取得结果，往往比界面功能数量更有用。本清单因此改用文档站取代旧新闻页。[官方入口](https://intework.hirain.com/)

从自己的硬件通道和数据库开始，先完成记录，再按教程建立一次外部调用。保存调用参数、返回值和原始记录，检查接口关闭后是否还残留发送任务。基础版的免费取得与具体协议、硬件及自动化功能授权应分别确认。

<a id="canoe"></a>
## CANoe：比较现有测试资产能否继续使用

CANoe 将网络仿真、刺激、诊断和自动化测试组织在一个环境中。团队已有工程、数据库和测试模块时，保留这些资产的成本应纳入比较。面向纯软件功能测试的 CANoe4SW 另有产品范围，不能用其中一页的功能说明推定所有 CANoe 版本都包含相同能力。[CANoe](https://www.vector.com/en/product/canoe/) · [CANoe4SW](https://www.vector.com/en/product/canoe4sw/)

评估替换工具时，选一条日常回归用例完整迁移：准备环境、仿真对端、执行断言、导出结果、退出并释放硬件。记录需要重写的接口、运行环境和授权依赖；“能打开 DBC”只覆盖其中很小一部分。

<a id="python-can"></a>
## python-can：统一收发 API，虚拟总线不模拟仲裁

python-can 用统一 API 连接不同 CAN 后端，适合将采集或测试逻辑与接口厂商解耦。`VirtualBus` 可让同一 Python 进程中的实例交换报文，但官方明确说明它不模拟总线速率限制或按 CAN ID 仲裁；可靠、有序的软件传递不等于真实高负载总线行为。[VirtualBus 的范围](https://python-can.readthedocs.io/en/stable/interfaces/virtual.html)

先用虚拟后端验证过滤、队列和超时逻辑，再切换真实接口检查时间戳、丢帧、CAN FD 配置与接收负载。应用若只需要报文收发，可以从这里起步；需要信号语义时，增加数据库编解码层，而不是把 bit 位解释写进每条测试。

<a id="cantools"></a>
## cantools：DBC 到信号值，也能生成 C 编解码函数

cantools 可载入数据库，将 CAN ID 与载荷转换成信号，或反向编码报文；`generate_c_source` 生成消息结构、pack/unpack 及信号转换函数。生成物属于数据编解码层，不包含接口驱动、任务调度或完整 ECU 通信栈。[Python API、命令行与 C 生成说明](https://cantools.readthedocs.io/en/latest/)

以一条报文建立三组固定样例：原始字节、期望物理值、重新编码结果。至少覆盖符号位、字节序、缩放和复用分支。生成的 C 与 Python 解码器使用同一组样例交叉比较，这样能查出数据库理解或接入错误，而不只是检查文件是否生成。

<a id="asammdf"></a>
## asammdf：处理测量文件，保留原始时间轴

asammdf 读取、处理和转换 MDF 测量记录，提供筛选、裁剪、重采样及数据导出。它位于采集之后，与实时总线接口库分工不同。[官方功能与示例入口](https://asammdf.readthedocs.io/en/latest/)

从短记录选择几个已知通道，核对单位、采样时间和通道组，再执行批处理。不同采样率统一成一张表时，应明确插值或保持方式；状态量跳变不宜未经判断直接线性插值。保留原文件与转换参数，便于把分析结果追溯到原始采样点。

<a id="udsoncan"></a>
## udsoncan：UDS 服务调用与 DID 编解码分开配置

udsoncan 的 Client 通过 connection 对象收发 UDS 数据，DID 的字节解释由 `data_identifiers` 中的 codec 等配置决定。库知道服务结构，并不因此知道某个 ECU 的厂商自定义数据格式。CAN 上还需 ISO-TP，DoIP 可通过连接适配器接入。[连接与 DID codec 示例](https://udsoncan.readthedocs.io/en/latest/udsoncan/examples.html)

在自有模拟端或隔离台架，从一个只读 DID 入手，对照原始响应、长度和解码值；然后检查负响应、响应等待和超时的分支。先保持 UDS 请求不变再更换传输层，能把业务编码错误与链路错误区分开。

<a id="doip"></a>
## python-doipclient：IP 地址之外还要配置逻辑地址

python-doipclient 负责 DoIP 发现、连接和路由激活，并通过 `DoIPClientUDSConnector` 对接 udsoncan。配置包括 ECU IP、ECU 与客户端逻辑地址、激活类型；当前 API 的 `auto_reconnect_tcp` 默认关闭。端口连通、路由激活成功和 UDS 服务应答是不同阶段。[API 与连接示例](https://python-doipclient.readthedocs.io/en/latest/)

在模拟端验证一个只读诊断请求，再检查对端断开后能否按预定策略恢复。日志分别记录 TCP、DoIP 确认与 UDS 响应，避免把所有失败都归为“诊断超时”。

## 用同一份小工程试四款总线工具

准备可公开或内部授权使用的数据库、原始记录、期望信号值与一条只读诊断用例。每款工具都完成“导入 → 解码 → 记录导出 → 外部脚本调用 → 结果比对”。保存原文件、转换参数、软件版本、接口驱动和授权选件。

这组材料能比较数据库保真、数据交接和自动化接入成本。吞吐、时间戳精度与故障注入能力另用相同硬件条件测试，不从这条功能流程推出性能排名。

---

文档采用 [CC BY 4.0](../../LICENSE)，署名与来源见 [ATTRIBUTION.md](../../ATTRIBUTION.md)。
