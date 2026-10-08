# 阅读、检索与传播维护记录

本轮日期：2026-10-08。基线：[bc4d960](https://github.com/yzy-comfortuni/awesome-sdv/tree/bc4d96068e3d76d61bc59e7d0b73367e2cbfd943)。本轮只调整阅读入口、引用和许可；保留全部 158 个条目、24 个分类及原有锚点，不把编辑日期当成逐条技术复核日期。

## 阅读与检索

首页先给出 SDV 中英文全称、范围与整理者，再提供按任务进入的两列表格。分类目录按主题分组，完整条目继续保留在 README，方便浏览器查找与直接链接，不把正文收进折叠块或图片。

新增导读回答 SDV、AUTOSAR、DDS/SOME/IP/VSS、车载 Rust、国产工具和转载授权等问题，并附原始资料或已有分类链接。英文页提供真实的英文简介与导航，不复制一份容易失步的完整清单。条目说明继续遵循 [Awesome AI Taste](https://github.com/yzy-comfortuni/awesome-ai-taste) 中的中文技术写作原则。

## SEO 与 GEO 的处理

SEO 指搜索引擎优化；GEO 指让内容在生成式搜索中更容易被发现、理解和引用。本轮采用明确名称、可见正文、稳定章节链接、来源与署名，未加入关键词堆砌、虚假评分、隐藏提示词或虚构的使用数据。

依据 [Google Search 的 AI 功能指南](https://developers.google.com/search/docs/appearance/ai-features)，常规的可访问性、内容质量和内部链接仍然适用；Google 没有要求额外的 AI 文本文件或特殊结构化标记。`CITATION.cff` 用于提供 [GitHub 支持的引用元数据](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)，不是搜索排名指令。

这轮没有为了 GEO 单独生成 `llms.txt`、`llms-full.txt` 或平行资源库。标准 Markdown 与引用文件已经提供可读的内容及出处；它们不保证被任何搜索或 AI 产品收录、引用或正确署名。

## 仓库设置：尚未应用

实际读取的 GitHub 设置为：description 为空，topics 为空，homepage 为空，GitHub Pages 未启用。当前连接能提交文件，但未提供 description/topics 写入操作；本地也没有可用的联网 GitHub CLI。因此，[repository-metadata.json](../.github/repository-metadata.json) 保存的是待应用值，不是已经生效的配置。

在具有该仓库管理权限且已登录 GitHub CLI 的环境中，从仓库根目录执行：

```sh
python3 -c 'import json; m=json.load(open(".github/repository-metadata.json")); print(json.dumps({"description":m["description"]}))' | gh api --method PATCH repos/yzy-comfortuni/awesome-sdv --input -
python3 -c 'import json; m=json.load(open(".github/repository-metadata.json")); print(json.dumps({"names":m["topics"]}))' | gh api --method PUT repos/yzy-comfortuni/awesome-sdv/topics --input -
gh api repos/yzy-comfortuni/awesome-sdv --jq '{description, topics, homepage, has_pages}'
```

第二条命令会替换全部 Topics；执行前若已有新增主题，应合并保留。上述命令在本轮未执行；[GitHub Topics 文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) 说明了主题标签的用途。

## 独立站的边界

README 文件不能控制 `github.com` 的 HTML head、站点根路径 robots.txt、sitemap 或 canonical。不要把这些标签写进 Markdown 后宣称已经完成站点级 SEO，也不要把某个仓库中的 robots.txt 当成 GitHub 的抓取规则。

本轮没有发布 GitHub Pages 或企业官网页面。后续若部署独立阅读站，应先确认实际 URL，再配置标题、description、自引用 canonical、语言链接和 sitemap；结构化数据须与可见内容一致。不能为未部署页面填入假地址或伪造 Search Console 验证。

## 品牌与许可

使用并列署名 ComfortUni（适宇科技），链接到 [品牌官网](https://www.comfortuni.com/)；不把品牌写进每个上游项目标题。文档采用 CC BY 4.0，代码保留 MIT；许可证原文和 [署名说明](../ATTRIBUTION.md) 分开，避免变成自定义限制许可。

依据 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)、[法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.en)、[Creative Commons FAQ](https://creativecommons.org/faq/) 与 [MIT 原文](https://opensource.org/license/mit)。不要求禁止商用、禁止修改或强制展示 Logo。旧 MIT 版本和第三方材料的许可分别保留。

## 检查与后续测量

本地验证目录完整性、跨文档链接和许可引用；CITATION.cff 的 YAML 读取另记在验证结果中，不把它说成 GitHub 引用 UI 已验收。检查记录见 [validation.json](validation.json)；这不是搜索排名、访问量或 AI 引用率的测量。

评估后续效果时，分别记录搜索收录、非品牌词检索、带来源的 AI 引用和转载署名。固定查询与日期，保留未命中结果；不能用一次搜索或一个生成式回答宣称排名提升。没有建立定时监控或提交搜索收录请求。
