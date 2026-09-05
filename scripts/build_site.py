"""Build the public career blog using only the Python standard library."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
ORIGIN = 'https://xmhuangzhijun-hue.github.io/ai-product-builder-portfolio'
GH = 'https://github.com/xmhuangzhijun-hue'
HERMES = 'https://github.com/NousResearch/hermes-agent/pull/'
PAGES = {}
CONTACT = json.loads((ROOT / 'content/contact.json').read_text(encoding='utf-8'))

def contact_block(base):
    phone = CONTACT.get('phone', '')
    phone_html = f'<a href="tel:{escape(phone, quote=True)}">手机 · {escape(phone)}</a>' if phone else ''
    return f'''<section class="wrap contact-panel" id="contact"><div><p class="eyebrow">LET’S TALK</p><h2>聊聊你的 AI 产品，<br>也聊聊我能做的事。</h2><p>求职主方向：FDE（Forward Deployed Engineer）</p><p>延伸方向：AI 产品定义与应用开发</p><div class="contact-links"><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>{phone_html}<span>微信 · {CONTACT['wechat']}</span></div><p class="contact-hint">添加微信请备注公司或交流主题。</p></div><figure><img src="{base}static/wechat.jpg" alt="黄智军 的微信二维码，微信号 {CONTACT['wechat']}" width="190" height="190" loading="lazy"><figcaption>扫码添加微信<br><a href="{base}static/wechat.jpg" target="_blank" rel="noopener">查看原图 ↗</a> · <a href="{base}static/wechat.jpg" download="黄智军-WeChat.jpg">下载二维码</a></figcaption></figure></section>'''

def ext(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}<span aria-hidden="true"> ↗</span></a>'

def page(path, title, description, body, active=''):
    PAGES[path] = (title, description)
    if path == 'contributions.html':
        from engineering_portfolio import ownership_overview
        body = body.replace('<article class="contribution featured">', ownership_overview()+'<article class="contribution featured">')
    depth = path.count('/')
    base = '../' * depth or './'
    nav = ''.join(f'<a href="{base}{href}"'+((' aria-current="page"' if path == href else ' aria-current="location"') if key == active else '')+f'>{label}</a>' for key, href, label in [('home','index.html','首页'),('experience','experience.html','经历'),('projects','projects/index.html','项目'),('skills','skills.html','技能'),('notes','notes/index.html','笔记'),('contributions','contributions.html','开源'),('about','about.html','关于')])
    full = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · 黄智军</title><meta name="description" content="{escape(description, quote=True)}">
<meta name="theme-color" content="#f7f9fc"><meta property="og:type" content="{'website' if path == 'index.html' else 'article'}"><meta property="og:title" content="{escape(title, quote=True)} · 黄智军"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{ORIGIN}/{path}">
<link rel="canonical" href="{ORIGIN}/{path}"><link rel="icon" href="{base}static/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="{base}static/site.css"><link rel="stylesheet" href="{base}static/career.css"><link rel="stylesheet" href="{base}static/engineering.css"></head>
<body><a class="skip" href="#main">跳到正文</a><header class="site-header"><a class="brand" href="{base}index.html"><img src="{base}static/mark.svg" alt="" width="30" height="30"><span>黄智军<span class="brand-sub">AI 产品与应用实践</span></span></a><nav aria-label="主导航">{nav}</nav></header>
<main id="main">{body.replace('@BASE@',base)}</main>
{contact_block(base)}<footer class="site-footer"><span>© 2026 黄智军<span class="footer-sub">产品判断 · 工程实现 · 公开记录</span></span><div>{ext(GH,'GitHub')}<a href="#contact">联系我</a><a href="{base}notes/index.html">实践笔记</a></div></footer></body></html>'''
    dest = OUT/path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(full,encoding='utf-8')

projects = [
    ('data-dashboard','工作项目 · 自研业务系统','没有开放 API，怎样把网页报表做成可信看板？','授权浏览器取数、字段归一化、重复检测、分批稳定性校验与服务端数据隔离。','Python / pandas / SQLite / FastAPI · 23 项专项测试通过'),
    ('ad-platform','工作项目 · 产品与前端原型','把投放业务拆成账户、产品、指标和操作流程。','Vite + React 中台原型，复用筛选、排序、粘性列与合计行；提供固定模拟数据体验。','React / TypeScript / Tailwind · 可交互 Demo'),
    ('blog','自有开源项目 · AI 协作实现','带内容后台和持久化数据的个人博客。','独立 Hono API、PostgreSQL、租户过滤和账号登录；已部署并核对 61 篇发布文章。','Next.js / Hono / PostgreSQL · MIT'),
    ('assistant','开源二次开发 · 上游贡献','把个人助手的视觉等待和消息乱序修到处理链路。','基于 Hermes 部署和改进；1 项原始修复被上游保留署名采纳，另有公开待审提交。','Python / 异步处理 / 回归测试 · Hermes fork'),
    ('shell','自有扩展项目 · 基于上游 Harness','给 Agent 加上手机交互外壳和 LAN 登录网关。','UI 插槽接入、TLS 登录、WebSocket 代理与 Host 信任配置；不修改上游源码。','TypeScript / Node.js / TLS · 单人 LAN'),
    ('memory','自有实践与开源参考实现','把长期项目记录与可追踪执行结果分开管理。','Obsidian 接续实践；公开运行时含事件路由、权限检查、4 类终态与 5 个测试。','Python / 事件与回执 / 知识管理 · 早期参考实现'),
]
notes = [
    ('data-quality','工作实践 · 数据工程','没有开放 API 时，如何避免“抓到了，但抓错了”？','投放数据看板中的重复分页、BI 补数与两批次稳定性校验。','5 分钟'),
    ('blog-delivery','我的博客 · 上线实践','一个博客，怎样才算真的交付了？','从原博客的部署笔记出发，核对发布内容、数据库和可恢复版本。','5 分钟'),
    ('project-boundaries','我的博客 · AI 协作','用 AI 做博客时，我怎么定义“做完了”？','把开发流程笔记落到内容编辑、发布状态和前后端分工。','5 分钟'),
    ('lan-access','我的开源项目 · 工程复盘','页面打开了，为什么手机上的 Agent 还不能用？','ruoxi-shell 中的登录、TLS 与 WebSocket 接入案例。','4 分钟'),
    ('trace-evaluation','我的开源项目 · 验证','Agent 说“完成了”，我用什么来核对？','把评测笔记缩小成可检查的实验：成功、拒绝、失败与未知。','4 分钟'),
    ('vision-timeout','Agent 工程','图片超时后，为什么继续重试反而延长等待？','从一次已被上游采纳的修复，理解异常体验、重试边界和备用服务。','5 分钟'),
    ('message-order','问题定位','先发的图片，为什么可能后处理？','输入顺序与下载完成顺序不是一回事。一次同会话预处理问题的定位。','4 分钟'),
    ('memory-capture','记忆设计','后台任务的输出，应该进入用户长期记忆吗？','从自动采集边界出发，讨论来源、上下文和记忆污染。','4 分钟'),
    ('context-handoff','产品思考','让两个编码 Agent 接续，需要留下什么？','把“记住更多”拆成当前事实、判断依据与下一步能采取的行动。','4 分钟'),
]

ROLES = {
 'data-dashboard': ('数据链路 + 指标口径 + 交付验收', '让运营少踩重复取数和同名指标口径混用的坑。'),
 'ad-platform': ('业务建模 + 页面流程 + 前端组件', '在接入真实数据前，把操作方式做成可讨论的原型。'),
 'blog': ('内容模型 + 发布流程 + 部署验收', '更新文章与联系方式，不再每次都要修改页面代码。'),
 'assistant': ('问题复现 + 修复边界 + 上游提交', '减少图片超时后的重复等待，保护同一会话的消息顺序。'),
 'shell': ('交互外壳 + 登录网关 + 连接验证', '解决手机看得到页面、却接不上实时会话的问题。'),
 'memory': ('接续规则 + 来源分层 + 回执设计', '让下一个 Agent 有据可接，避免把旧摘要当成当前事实。'),
}

def project_cards():
    return ''.join(f'<a class="project-card" href="@BASE@projects/{slug}.html"><div class="card-label">{name}<span aria-hidden="true">↗</span></div><h3>{title}</h3><p>{ROLES[slug][1]}</p><p class="role-tag">我的主责：{ROLES[slug][0]}</p><div class="card-bottom">{tags}</div></a>' for slug,name,title,desc,tags in projects)


def note_list():
    return ''.join(f'<a class="note-row" href="@BASE@notes/{slug}.html"><span class="note-category">{cat}</span><div><h3>{title}</h3><p>{desc}</p></div><span class="note-time">约 {length}<span aria-hidden="true"> ↗</span></span></a>' for slug,cat,title,desc,length in notes)

page('index.html','FDE 求职作品集与工程实践','黄智军 的 AI 求职作品集与个人博客：项目案例、实践笔记，以及可核验的 Hermes Agent 开源贡献。',f'''
<section class="hero wrap"><div class="hero-copy"><p class="eyebrow"><span class="dot"></span> FDE / Forward Deployed Engineer</p><h1>走进业务现场，<br>把<span class="accent">数据和 AI</span><br>接进实际工作。</h1><p class="hero-lead">我是 黄智军，主攻业务现场的系统集成与可维护交付，也做 AI 产品定义与应用开发。从投放中台的业务建模，到网页取数、数据校验与云端看板，再到 Agent 应用和开源修复：我负责理解问题，借助 AI 推进实现，并检查交付结果。</p><div class="hero-actions"><a class="button primary" href="experience.html">看我的工作项目 <span aria-hidden="true">↗</span></a><a class="button" href="#contact">联系我 ↗</a></div><p class="hero-contact"><a href="mailto:xmhuangzhijun@gmail.com">xmhuangzhijun@gmail.com</a><span>微信：xmhuangzhijun</span></p></div>
<aside class="proof-card"><div class="proof-top"><span>一项公开贡献</span><span class="badge">已合入上游</span></div><p class="proof-project">HERMES AGENT</p><h2>让图片超时之后，<br>少一次无效等待。</h2><p>提交视觉请求重试修复，原始贡献由维护者保留作者署名，整合后进入主分支。</p><a class="proof-link" href="notes/vision-timeout.html">读这次改进的来龙去脉 <span aria-hidden="true">↗</span></a><div class="proof-footer">原始贡献 #97572 <span>→</span> 合入 #101570</div></aside></section>
<section class="wrap capability-strip" aria-label="能力与作品"><div><strong>产品定义</strong><span>需求 → 可用流程 → 验收标准</span></div><div><strong>AI 协作开发</strong><span>Web / API / 数据库 / 部署</span></div><div><strong>Agent 改进</strong><span>实际问题 → 测试 → 上游贡献</span></div></section><section class="wrap section" id="projects"><div class="section-head"><div><p class="eyebrow">SELECTED WORK</p><h2>用作品说明，我能做什么。</h2></div><p>每个案例都有具体场景、我的工作、<br>当前结果和可检查的材料。</p></div><div class="project-grid">{project_cards()}</div></section>
<section class="wrap proof-band"><div><p class="eyebrow">OPEN SOURCE / 第三方可核验</p><h2>一项原始修复，被 Hermes 上游采纳。</h2><p>我提交 #97572 → 维护者保留署名整合 → #101570 合入主分支。</p></div><div><a class="button primary" href="notes/vision-timeout.html">阅读修复复盘 ↗</a><a class="text-link" href="contributions.html">原始 PR、合入记录与待审提交 →</a></div></section>
<section class="wrap section notes-section"><div class="section-head"><div><p class="eyebrow">FIELD NOTES</p><h2>把实践写清楚。</h2></div><a class="text-link" href="notes/index.html">全部笔记 →</a></div>{note_list()}</section>
<section class="wrap about-strip"><p>关注真实场景，愿意动手实现，也认真对待失败。</p><a class="text-link" href="about.html">认识我 →</a></section>''','home')

def article(path, kind, title, lead, body, active='notes', aside=''):
    if path.startswith('projects/'):
        from engineering_portfolio import project_evidence
        body = project_evidence(Path(path).stem) + body
    case_map = {
        'vision-timeout': ('个人 AI 助手 / Hermes', 'assistant', '原始修复 #97572 → 上游整合 #101570', HERMES+'101570', '上游已采纳'),
        'message-order': ('个人 AI 助手 / 微信通道', 'assistant', '我提交的同会话预处理修复 #97743', HERMES+'97743', '公开 PR · 尚未合并'),
        'memory-capture': ('个人 AI 助手 / 长期记忆', 'memory', '我提交的自动捕获边界修复 #97156', HERMES+'97156', '公开 PR · 尚未合并'),
        'context-handoff': ('我的 Obsidian 项目记录与 Agent 接续', 'memory', '个人实践案例与设计边界', GH+'/ai-product-builder-portfolio/blob/main/docs/agent-shared-memory.md', '个人实践 · 案例说明'),
        'blog-delivery': ('我自己的博客 / XMHUA Card', 'blog', '部署步骤与真实功能验收标准', GH+'/xmhua-card/blob/master/docs/DEPLOYMENT.md', '已部署项目 · 本次只读核验'),
        'project-boundaries': ('我自己的博客 / XMHUA Card', 'blog', '内容读取、发布过滤和持久化源码', GH+'/xmhua-card/blob/master/api/src/services/content.ts', '已部署项目 · 公开源码'),
        'lan-access': ('我的 Agent 交互外壳 / ruoxi-shell', 'shell', '接入结果与复现文档', GH+'/ruoxi-shell#verified-behaviour', '早期开源实现 · 已记录实验'),
        'trace-evaluation': ('我的 Agent 参考运行时', 'memory', '5 个可独立运行的边界测试', GH+'/organic-agent-os/blob/main/tests/test_runtime.py', '最小实验 · 非完整评测平台'),
    }
    slug = Path(path).stem
    if active == 'notes' and slug in case_map:
        project, link, evidence, url, stage = case_map[slug]
        body = f'<section class="case-anchor"><span class="badge neutral">{stage}</span><h2>这篇笔记对应我的哪项实践？</h2><p><a href="../projects/{link}.html">{project} →</a></p><p>{ext(url,evidence)}</p></section>' + body
    page(path,title,lead,f'''<div class="wrap article-shell"><a class="back" href="@BASE@{'notes/index.html' if active=='notes' else 'index.html#projects'}">← {'全部笔记' if active=='notes' else '所有项目'}</a><header class="article-header"><p class="eyebrow">{kind}</p><h1>{title}</h1><p class="article-lead">{lead}</p><div class="article-meta">黄智军 <span>·</span> 整理于 2026 年 9 月 5 日</div></header><div class="article-grid"><article class="prose">{body}</article><aside class="article-aside">{aside or '<p class="eyebrow">阅读提示</p><p>这是结合公开变更与项目实践整理的复盘。源码与讨论链接位于正文中。</p>'}<div class="aside-nav"><a href="@BASE@contributions.html">开源贡献 ↗</a><a href="@BASE@about.html">关于作者 →</a></div></aside></div></div>''',active)

article('projects/assistant.html','PROJECT · AI AGENT','个人 AI 助手：从输入到结果','围绕个人任务，连接自然语言、相关信息与可执行工具。',f'''
<h2>要解决的问题</h2><p>对话顺畅只是入口。真正使用助手时，我还需要它知道当前任务、在授权范围内调用工具，并在动作之后说明结果是否生效。图片处理卡住、重复消息或上下文错位，都会直接影响这条使用路径。</p>
<h2>我负责的工作</h2><p>我定义产品目标与完成标准，设计任务状态、权限和结果反馈；借助 AI 推进开源运行时的集成、部署、调试和复盘。底层以 Hermes 等已有能力为基础，我的工作集中在应用落地及实际使用问题的改进。</p>
<div class="flow" aria-label="任务流程"><span>用户表达需求</span><b>→</b><span>理解与取上下文</span><b>→</b><span>调用授权工具</span><b>→</b><span>确认结果</span></div>
<h2>关键取舍：把判断和执行分清楚</h2><p>模型适合理解意图、组织信息和选择下一步。权限检查、状态记录和外部动作是否成功，则需要明确的系统结果支撑。界面和回复也要保留这种区别：接到任务不等于已经完成。</p>
<h2>从体验问题进入工程细节</h2><p>视觉请求超时后，重复等待同一服务可能继续阻塞会话；媒体消息并发下载时，后发消息可能先进入后续处理。这些问题让我沿用户入口追到内部处理路径，并将改进整理成公开修复。</p><ul><li><a href="../notes/vision-timeout.html">视觉超时：避免再耗尽一个完整等待窗口</a></li><li><a href="../notes/message-order.html">同会话消息：保持预处理顺序</a></li></ul>
<h2>公开结果与边界</h2><p>视觉超时修复已通过后续 PR 合入上游；消息顺序修复目前仍为 Open。这里展示应用实践与特定修复，不提供私人助手的公开账号，也不把部分工具通过测试等同于所有自然任务均已完成验收。</p><div class="source-box"><strong>可核验资料</strong>{ext(HERMES+'101570','已合入的修复')}{ext(GH+'/hermes-agent','个人 fork')}{ext(GH+'/ai-product-builder-portfolio/blob/main/docs/qinghe-agent.md','原始公开项目说明')}</div>''','projects','<p class="eyebrow">我的工作</p><p>需求与完成标准<br>任务与反馈设计<br>开源能力集成<br>部署、调试与验证</p><p class="eyebrow">关键词</p><p>Agent · Hermes · MCP<br>权限 · 状态 · 回执</p>')

article('projects/memory.html','PROJECT · CONTEXT & KNOWLEDGE','Agent 记忆：让下一次工作有据可接','处理跨工具、跨会话中的上下文丢失与旧信息误用。',f'''
<h2>问题从哪里来</h2><p>项目持续迭代时，新的 AI 会话很容易不知道当前版本，重新尝试已经失败的方案，或者把历史记录当成今天的事实。简单地追加一份越来越长的记忆文件，无法自动解决这些问题。</p>
<h2>我如何拆解</h2><p>我把来源、项目现状、执行记录和候选经验分开考虑。项目代码与当前状态负责说明现在是什么；历史记录帮助理解为什么走到这里；新观察在验证前保留为候选，不能直接覆盖共同事实。</p><div class="flow"><span>明确本次问题</span><b>→</b><span>检索相关依据</span><b>→</b><span>核对当前状态</span><b>→</b><span>执行并记录</span></div>
<h2>一个自己的使用案例：接续博客项目</h2><p>我用 Obsidian 保存项目状态与变更记录，让 Codex、Claude Code 等工具接续工作。接手原博客时，旧记录说明曾经发布 57 篇文章；但这次查询实际部署的内容 API，已发布数量是 61。历史帮助找到项目，当前运行结果决定今天能写什么。不能直接把旧摘要当成当前事实。</p><p>同样，已经修改的本地文件不一定已提交，提交的代码也不一定已部署。我要求接续时分别确认这些状态，并保留其他任务正在进行的改动。</p><h2>产品判断：记忆要帮助行动</h2><p>我的关注点是下一次任务能否少一次重复交代、避开一条已被否定的路径，并清楚知道还有什么没有完成。内容是否被保存，只能证明存储发生过；能否改善后续行为，才是这套机制需要检验的结果。</p>
<h2>两种公开材料，各自说明什么</h2><p>项目案例文档说明本地实践中的分层与工作方式。另一个公开架构仓库提供早期规范和最小参考实现，供他人审阅设计。它尚不能作为完整本地系统已经全部开源的证明，也不代表成熟商用平台。</p>
<h2>从个人工作方式到公开实验</h2><p>我公开的 Python 参考运行时把事件、权限检查和终态回执做成了最小实验，测试覆盖成功、拒绝、异常和未知。它提供可运行的检查入口，但尚未实现完整的持久记忆治理和跨 Agent 编排。</p><div class="source-box"><strong>可核验资料</strong>{ext(GH+'/ai-product-builder-portfolio/blob/main/docs/agent-shared-memory.md','公开案例说明')}{ext(GH+'/organic-agent-os','早期架构与参考实现')}<a href="../notes/context-handoff.html">阅读上下文接续笔记 →</a><a href="../notes/trace-evaluation.html">阅读运行时实验与测试 →</a></div>''','projects','<p class="eyebrow">我的工作</p><p>问题与场景拆解<br>记忆分层与来源设计<br>候选更新和校验<br>跨工具协作实践</p><p class="eyebrow">公开范围</p><p>案例文档与早期参考实现；私人知识库不公开。</p>')

article('projects/builder.html','PROJECT · PRODUCT FOUNDATION','Agent 创建平台：从想法到发布流程','面向非技术使用者，探索角色、知识、测试与发布的完整产品流程。',f'''
<h2>用户要完成什么</h2><p>一个人有了助手的想法，还需要定义角色、接入资料、选择使用入口、检查回答并发布。配置项分散在不同工具中时，用户很难判断自己做到哪一步，也不容易知道哪里出了问题。</p>
<h2>我的产品方案</h2><p>将创建过程拆成连续的用户任务：描述需求、添加知识、选择入口、检查、发布、使用。每一步都应有明确的输入、当前状态和可以继续采取的行动。</p><div class="flow"><span>描述需求</span><b>→</b><span>添加知识</span><b>→</b><span>测试与检查</span><b>→</b><span>发布版本</span></div>
<h2>实现关注点</h2><p>公开案例记录的本地底座涉及 Web 界面、API、数据存储和身份边界。我重点关注机器人身份、草稿版本、并发修改保护、资料来源与处理回执，让“保存”和“发布”具有可检查的含义。</p>
<h2>为什么要保留版本与状态</h2><p>用户修改知识或角色后，需要知道访客实际使用哪一版。资料提交成功也不意味着处理完成，更不意味着它已经参与回答。把这些状态分清楚，可以让产品反馈与系统事实一致。</p>
<h2>当前展示边界</h2><p>这是产品架构与本地实现案例。公开材料没有提供完整的外部用户验收闭环，因此不将其描述为已上线的成熟 SaaS，也不提供无法工作的“立即体验”入口。</p><div class="source-box"><strong>公开材料</strong>{ext(GH+'/ai-product-builder-portfolio/blob/main/docs/organic-console.md','阅读产品底座与实现边界')}</div>''','projects','<p class="eyebrow">我的工作</p><p>创建与发布流程<br>知识处理状态<br>版本与租户边界<br>AI 协作实现</p><p class="eyebrow">阶段</p><p>产品底座 / 本地实现</p>')

page('notes/index.html','实践笔记','AI 产品判断、Agent 工程和开源问题复盘。',f'<section class="wrap listing"><p class="eyebrow">FIELD NOTES</p><h1>实践笔记</h1><p class="listing-lead">把问题、判断与结果写下来。<br>每篇都从一个具体的工作场景出发。</p><div class="notes-section">{note_list()}</div></section>','notes')

article('notes/vision-timeout.html','AGENT 工程 · 开源复盘','图片超时后，为什么继续重试反而延长等待？','一次被 Hermes 上游采纳的视觉请求重试修复。',f'''
<h2>先看用户的等待</h2><p>图片分析迟迟没有结果，会影响同一会话后续消息。重试能挽救短暂故障，但如果一次请求已经耗尽完整超时预算，再向同一个服务商等待一遍，就可能延迟备用服务接手。</p>
<h2>我提交的改动</h2><p>我提交的 <a href="{HERMES}97572">#97572</a> 针对视觉请求满预算超时调整重试边界，并增加行为测试。目标是让这类请求进入后备路径，同时维持其他任务的既有重试行为。</p>
<h2>从提交到上游整合</h2><p>后续主分支发生变化，维护者在 <a href="{HERMES}101570">#101570</a> 保留作者署名接纳原始提交，并补充同步、异步路径的处理与共同判断逻辑。该整合 PR 已合入，原始 PR 因此关闭。</p>
<h2>这次经历里的产品判断</h2><p>“再试一次”是否合理，要结合用户正在做的事。对交互任务而言，等待本身就是体验成本。需要判断当前错误更像短暂波动，还是已经充分等待后的失败，再决定重试或转交备用方案。</p><p>我也需要把个人贡献与维护者后续工作分别说明：原始修复被采用，不意味着最终整合中的每一处变化都由我完成。</p>
<h2>结果怎样表述才准确</h2><p>可以确认的是修复进入了上游主分支。维护者提供过模拟网络基准，但这不等同于我对真实用户线上时延的测量，因此这里不把它转换成自己的性能收益百分比。</p><div class="source-box"><strong>源码与讨论</strong>{ext(HERMES+'97572','原始提交与讨论')}{ext(HERMES+'101570','已合入 PR 与作者来源')}</div>''')

article('notes/message-order.html','问题定位 · 开源复盘','先发的图片，为什么可能后处理？','输入顺序正确，并不保证后续处理顺序正确。',f'''
<h2>顺序在哪里发生变化</h2><p>用户先后发送两张图片，轮询拿到的消息也是有序的。但每条消息被独立处理后，第一张下载较慢、第二张下载较快，后发图片就可能先进入会话处理。</p>
<h2>为什么已有会话排队还不够</h2><p>会话层只能排列已经到达的任务。如果顺序在媒体预处理阶段就变了，后续排队无法还原原始顺序。这让我把问题定位到媒体下载之前的处理边界。</p>
<h2>修复应该作用到哪里</h2><p>我在 <a href="{HERMES}97743">#97743</a> 提交同会话预处理顺序保护，并保留不同会话之间的并发。测试关注顺序、跨会话并行，以及前一个处理失败后后续任务能否继续。</p>
<h2>我的取舍</h2><p>保护顺序会影响同会话媒体处理的并发程度。我认为这里需要围绕对话语义作取舍，同时避免把一个会话的等待扩展到所有用户。修复的范围应与问题发生的边界一致。</p>
<h2>当前状态</h2><p>截至本次整理，PR 仍为 Open。这篇记录的是问题分析和已提交方案，不能视为上游已经合并的成果。</p><div class="source-box"><strong>公开证据</strong>{ext(HERMES+'97743','查看修复、测试与讨论')}</div>''')

article('notes/memory-capture.html','记忆设计 · 开源复盘','后台任务的输出，应该进入用户长期记忆吗？','保存之前，先问这条信息来自谁、发生在什么上下文。',f'''
<h2>自动采集的边界</h2><p>长期记忆希望帮助助手理解用户。但后台定时任务、整理过程与子任务输出，未必代表用户自己说过的话。如果它们沿同一条自动采集路径进入用户记忆，就可能混淆来源。</p>
<h2>我关注的修复方向</h2><p>在 <a href="{HERMES}97156">#97156</a> 中，我提交了特定机器驱动上下文的自动采集边界修复。问题的重点是执行上下文和写入资格，而不是给内容多做一次文字总结。</p>
<h2>对产品设计的启发</h2><p>记忆产品需要分别回答：信息来自用户表达、工具结果，还是系统自己生成；适用于当前任务还是长期；未经核对时应该暂存还是成为事实。不同答案应影响后续使用方式。</p>
<h2>我采用的原则</h2><p>保留来源，区分事实与候选，让当前项目状态能够校正旧记录。这样，下一次任务读取记忆时，才有条件判断该相信什么、还需要核实什么。</p>
<h2>当前状态</h2><p>截至本次整理，原始 PR 仍为 Open。这里展示公开问题与提交方案，不将其标记为已合入上游。</p><div class="source-box"><strong>公开证据</strong>{ext(HERMES+'97156','查看自动采集边界修复')}</div>''')

article('notes/context-handoff.html','产品思考 · 项目实践','让两个编码 Agent 接续，需要留下什么？','接续上下文的目的，是帮助下一步行动。',f'''
<h2>先明确接续要解决的问题</h2><p>新会话需要知道的不只是之前聊过什么，还包括当前项目到哪一步、哪些判断仍有效、什么方案已尝试，以及现在可以安全做什么。完整聊天记录不一定能直接回答这些问题。</p>
<h2>我如何组织信息</h2><p>我把项目当前状态、行动记录、判断依据与候选经验分开。接手先围绕本次问题取相关材料，再核对代码或当前状态；历史解释原因，当前证据决定下一步。</p>
<h2>我自己的使用案例</h2><p>接续个人博客时，历史记录写着曾公开 57 篇笔记，本地还有尚未发布的改动。如果直接从历史摘要写求职介绍，就会混淆过去的状态和现在的产品。我的处理方式是：用项目记录定位内容服务，再只读查询已部署 API。本次实际读到 61 篇已发布文章和微信入口，因此展示当前数据，同时保留原记录作为历史。</p><p>这个案例体现的是接续时如何使用依据，而不是一个效率提升的量化实验。私人项目日志不对外提供；博客的公开内容接口与存储代码可在下方仓库检查。</p>
<h2>一份有用的接续记录</h2><ul><li>任务目标与当前完成状态。</li><li>已经检查到的事实及来源。</li><li>做过的尝试、失败原因和适用条件。</li><li>仍然存在的不确定性与下一步。</li><li>不能修改的范围和需要保留的并发工作。</li></ul>
<h2>避免把推断升级成事实</h2><p>模型新写下的解释并不天然具有更高权威。需要保留其来源和验证状态，避免一次概括覆盖了原始证据。另一个 Agent 再次读取时，也应该知道它是确认过的结论，还是等待检验的候选。</p>
<h2>怎样判断有没有帮助</h2><p>我更关注下一次工作是否减少了重复调查，能否避开已知失败路径，而不只是记忆库又增加多少字。评估应回到真实接续任务，也应诚实记录尚未测量的改进。</p><div class="source-box"><strong>相关项目</strong><a href="../projects/memory.html">Agent 记忆与知识管理 →</a>{ext(GH+'/ai-product-builder-portfolio/blob/main/docs/agent-shared-memory.md','公开案例说明')}{ext(GH+'/xmhua-card/blob/master/api/src/routes/public.ts','本例对应的公开内容接口源码')}</div>''')

page('contributions.html','开源贡献','Hermes Agent 的公开修复、作者记录与合入状态。',f'''<section class="wrap listing"><p class="eyebrow">OPEN SOURCE</p><h1>公开贡献，<br>让工作可以被检查。</h1><p class="listing-lead">从实际使用中的问题出发，提交可以讨论、测试与审阅的改进。</p>
<article class="contribution featured"><div><span class="badge">已被上游采纳</span><h2>视觉请求满预算超时后的重试修复</h2><p>避免在同一服务商上再次耗尽完整等待窗口后，才进入备用路径。原始提交由维护者保留作者署名，经后续 PR 整合并合入主分支。</p></div><div class="contribution-links">{ext(HERMES+'97572','我的原始 PR #97572')}{ext(HERMES+'101570','已合入 PR #101570')}<a href="notes/vision-timeout.html">阅读复盘 →</a></div></article>
<article class="contribution"><div><span class="badge neutral">Open · 尚未合并</span><h2>同会话消息预处理顺序</h2><p>处理媒体下载速度差异造成的消息顺序变化，保护同会话顺序，保留跨会话并发。</p></div><div class="contribution-links">{ext(HERMES+'97743','查看 PR #97743')}<a href="notes/message-order.html">阅读复盘 →</a></div></article>
<article class="contribution"><div><span class="badge neutral">Open · 尚未合并</span><h2>长期记忆自动采集的上下文边界</h2><p>避免特定后台任务和子任务的内容沿自动采集路径混入用户记忆。</p></div><div class="contribution-links">{ext(HERMES+'97156','查看 PR #97156')}<a href="notes/memory-capture.html">阅读复盘 →</a></div></article>
<p class="updated">状态核对：2026-09-05。后续变化以 GitHub 对应页面为准。</p></section>''','contributions')

page('about.html','关于我','黄智军：面向 AI 产品与 AI 应用开发岗位，展示需求判断、AI 协作实现与开源实践。',f'''<section class="wrap about-page"><p class="eyebrow">ABOUT 黄智军</p><h1>关注问题，<br>也把想法<span class="accent">做出来。</span></h1><p class="about-intro">我关注 AI 产品、Agent 应用与知识系统。习惯从具体使用场景出发，先理解问题，再借助 AI 推进产品设计、实现、调试与验证。</p>
<div class="about-columns"><div><h2>我希望做的工作</h2><p>AI 产品经理、AI 应用开发，以及需要产品理解与动手实现能力的 Agent 相关岗位。</p><h2>我如何参与项目</h2><p>需求与关键取舍由我负责，调研、代码和测试过程中使用 AI 协作。开源项目、他人工作与我的改动分别说明，结果按照公开证据呈现。</p></div><div><h2>你可以从哪里了解我</h2><p>先读项目案例了解场景和职责，再通过实践笔记查看具体判断。开源贡献页提供原始提交、讨论和合入记录。</p><h2>联系与进一步交流</h2><p>你可以通过简历上的联系方式联系我，也可以从公开 GitHub 主页了解持续更新的工作。</p>{ext(GH,'查看我的 GitHub 主页')}</div></div>
<div class="about-end"><a class="button primary" href="index.html#projects">浏览项目</a><a class="button" href="notes/index.html">阅读笔记</a></div></section>''','about')

page('404.html','页面不存在','这个地址没有对应页面。','<section class="wrap listing"><p class="eyebrow">404</p><h1>这篇内容不在这里。</h1><p class="listing-lead">可以回到首页，继续浏览项目与笔记。</p><a class="button primary" href="index.html">返回首页</a></section>')
(OUT/'.nojekyll').write_text('',encoding='utf-8')
from portfolio_details import render
render(page, article, ext, GH, HERMES, note_list)
from engineering_portfolio import render_engineering
render_engineering(page, article, ext, GH)

page('projects/index.html','项目与我的职责','工作项目、自有开源与上游二次开发，附具体职责、源码或脱敏验证材料。',f'<section class="wrap listing"><p class="eyebrow">SELECTED WORK</p><h1>项目，和我负责的部分。</h1><p class="listing-lead">从业务问题、实现取舍到结果；每个案例注明归属与证据范围。</p><div class="project-grid">{project_cards()}</div></section>','projects')
from seo import finalize
finalize(OUT, PAGES)

print(f'Built {len(list(OUT.rglob("*.html")))} HTML pages.')
