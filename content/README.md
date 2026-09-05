# 内容维护

公开网站：https://xmhuangzhijun-hue.github.io/ai-product-builder-portfolio/

`contact.json` 只保存作者明确授权公开的联系方式。微信与二维码沿用原博客已发布内容，邮箱由作者指定。手机号未提供时不显示。

页面由 `scripts/build_site.py`、`scripts/portfolio_details.py` 与 `scripts/engineering_portfolio.py` 生成。运行 `python scripts/build_site.py` 后，提交对应源码与 `docs/` 产物，GitHub Pages 从 `main /docs` 发布。

求职方向包含 FDE、AI 产品经理和 AI 应用开发。投放中台（模拟数据原型）与投放数据看板（业务数据链路）分开描述，工作经历只公开框架、职责和脱敏验证，不填未核实的正式职称或任职日期。

`docs/demo/iaa/` 沿用作者公开的 `xmhuangzhijun-hue/xmhua-card/public/demo/iaa/` 静态演示产物，将入口资源路径改成相对路径以兼容 GitHub Pages，并增加持续可见的模拟数据/占位说明与返回链接。固定模拟数据，不连接生产系统；演示登录不是鉴权实现的证据。重新构建该 Demo 需使用其原始 Vite 工程；博客生成器保留这个已发布产物。

## 本版文章与证据

| 文章 | 对应个人实践 | 公开材料 |
| --- | --- | --- |
| 没有开放 API 时，如何避免抓错数据 | 工作中的数据看板 | 脱敏工程案例与 23 项本地测试摘要；公司源码不公开 |
| 一个博客，怎样才算真的交付了 | 原博客部署与发布数据核对 | xmhua-card 部署说明、公开 API |
| 用 AI 做博客时，我怎么定义做完了 | 原博客内容后台与产品迭代 | xmhua-card 内容服务、数据模型 |
| 页面打开了，为什么手机上的 Agent 还不能用 | ruoxi-shell 局域网接入 | README 实验记录、gateway 源码 |
| Agent 说完成了，我用什么核对 | Organic Agent OS 最小运行时 | runtime.py、test_runtime.py |
| 图片超时后，为什么继续重试反而延长等待 | Hermes 原始贡献 #97572 | 上游整合 #101570 |
| 先发的图片，为什么可能后处理 | Hermes 微信消息预处理 | PR #97743，尚未合并 |
| 后台任务的输出应该进入长期记忆吗 | Hermes 自动记忆边界 | PR #97156，尚未合并 |
| 让两个编码 Agent 接续，需要留下什么 | Obsidian 项目记录与博客接续 | 公开案例说明、博客内容接口 |

前三篇学习主题中的博客交付、开发边界和运行时评测，分别重新整理自作者原博客的 `vibe-coding-2`、`vibe-coding`、`agent-golden-tasks`。其余原博客文章未整体迁入本求职版。没有个人应用证据的外部框架分析，不写成已经采用的项目成果。

2026-09-05 通过原博客已部署的只读内容 API 核对到 PostgreSQL 来源、61 篇已发布文章和微信入口。此次只读核对不等于重新完成编辑保存、整机恢复或手机语音验收。原始数据副本、私人日志和内部部署地址不进入公开仓库。
