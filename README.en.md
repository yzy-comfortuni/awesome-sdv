# Awesome SDV — Software-Defined Vehicle Resources

A curated guide to open-source projects, commercial tools, standards and technical documentation for software-defined vehicles. It covers AUTOSAR, automotive Rust, DDS, SOME/IP, CAN tools, virtual ECUs, SIL/HIL, software updates and vehicle software delivery.

Initiated and maintained by [ComfortUni（适宇科技）](https://www.comfortuni.com/) with community contributions.

[完整中文目录](README.md) · [Getting started, in Chinese](docs/START_HERE.md) · [Attribution and reuse](ATTRIBUTION.md)

## Find resources by task

| Task | Catalog sections |
| --- | --- |
| Understand the software stack | [Ecosystems](README.md#ecosystem), [vehicle operating systems](README.md#platforms), [vehicle data and APIs](README.md#vehicle-data) |
| Develop MCU or zonal-controller software | [Real-time systems](README.md#mcu), [Rust](README.md#rust), [AUTOSAR](README.md#autosar), [virtualization](README.md#virtualization) |
| Compare communication components | [DDS, including RTI Connext Drive](README.md#dds), [SOME/IP and IPC](README.md#middleware), [CAN, Ethernet and time synchronization](README.md#networks) |
| Find Chinese automotive engineering tools | [TSMaster, ZXDoc and INTEWORK-VBA](README.md#bus-tools), [basic software](README.md#autosar), [modeling tools](README.md#modeling) |
| Build a development and test workflow | [Diagnostics and calibration](README.md#diagnostics), [virtual ECUs and SIL/HIL](README.md#simulation), [debugging and verification](README.md#verification) |
| Deliver and update vehicle software | [Orchestration](README.md#orchestration), [OTA](README.md#ota), [secure boot](README.md#secure-boot), [software supply chain](README.md#supply-chain) |

Other sections cover [functional safety and development practices](README.md#safety), [HMI](README.md#hmi), [autonomous-driving simulation](README.md#adas), [batteries and charging](README.md#ev), and [related awesome lists](README.md#related).

## How the catalog is organized

The complete catalog lives in the Chinese README; this page is an English navigation guide, not a separate translated catalog. Each resource has an official link, a short description and a type label. Open-source and commercial tools appear in the same engineering category, with their status identified explicitly.

| Label | Meaning |
| --- | --- |
| 开源 | Open-source code project |
| 商业 | Product licensed under vendor terms, including free editions |
| 标准 | Standard or specification |
| 文档 | Technical documentation |
| 生态 | Organization or project collection |
| 清单 | Related resource list |

The catalog is a discovery aid, not a benchmark or a production qualification. Platform support, product editions and licensing should be checked with the upstream project. The [source-review log](docs/REVIEW.md) distinguishes reviewed material from access limitations.

## Reuse and attribution

Documentation is available under [CC BY 4.0](LICENSE); scripts and test code are under [MIT](LICENSE-CODE). Commercial use and adaptations are welcome. When sharing licensed documentation, retain the supplied attribution, source and license information, and identify modifications as required by CC BY 4.0.

Suggested credit:

> Awesome SDV — Software-Defined Vehicle Resources, curated by ComfortUni（适宇科技）and contributors. Source: [yzy-comfortuni/awesome-sdv](https://github.com/yzy-comfortuni/awesome-sdv). Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reproduced without changes.

For translations or adaptations, replace the last sentence with an accurate description of the changes. See [ATTRIBUTION.md](ATTRIBUTION.md) for scope, historical MIT grants and trademark information. [CITATION.cff](CITATION.cff) supplies structured citation metadata.
