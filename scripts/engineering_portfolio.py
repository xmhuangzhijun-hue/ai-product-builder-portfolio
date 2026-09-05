"""Sanitized engineering evidence and explicit project ownership."""

def ownership_overview():
    return '''<section class="ownership"><h2>项目归属与我的贡献</h2><div class="table-scroll"><table><thead><tr><th>类别</th><th>项目</th><th>我的工作</th></tr></thead><tbody><tr><td>工作项目</td><td>投放数据看板 / 投放中台</td><td>业务与技术方案、AI 协作实现和验收；公司资料脱敏，生产源码不公开</td></tr><tr><td>自有开源项目</td><td>XMHUA Card</td><td>个人博客产品与内容发布系统；MIT，公开完整应用源码</td></tr><tr><td>自有扩展项目</td><td>ruoxi-shell</td><td>UI 外壳和 LAN 网关；底层模型、会话和工具来自 DeepSeek Harness，不修改上游源码</td></tr><tr><td>开源 Fork / 二次开发</td><td>Hermes Agent</td><td>个人部署与特定修复；不是框架原创作者，公开 fork 用于开发和提交</td></tr><tr><td>自有早期参考实现</td><td>Organic Agent OS</td><td>架构规范、事件/权限/回执最小运行时；不宣称完整 Agent 平台</td></tr></tbody></table></div><p>以下单列向他人维护的上游仓库提交的贡献。自建仓库、Fork 和已合入上游的修复分别计，不用仓库数量替代贡献成果。</p></section>'''

def project_evidence(slug):
    facts = {
      'blog': ('自有开源项目 · AI 协作实现', [
        ('解决的问题','让站点主人自己维护文章、项目与联系入口，减少每次更新都要改页面代码的依赖。'),
        ('我负责的模块','产品需求、内容对象与发布流程、读写边界和验收；代码、调试及部署使用 AI 协作。'),
        ('工程实现','Next.js 页面 + 独立 Hono API；Drizzle/PostgreSQL；异步读取内容；按 tenantId 约束查询；scrypt 密码哈希与服务端会话。'),
        ('部署约束','服务器构建资源不足，改为本地 Linux 构建、上传产物；前后端 systemd 独立进程，Nginx 同源反代。'),
        ('可验证结果','内容后台、草稿/发布过滤、多租户数据模型及查询隔离均有公开源码；本次读取 61 篇已发布文章。单站自用不代表已有多个付费租户。')]),
      'assistant': ('基于 Hermes 的二次开发 · 上游贡献', [
        ('解决的问题','图片分析已耗尽超时预算却继续等待同一服务；媒体下载耗时差异导致同会话消息预处理乱序。'),
        ('我负责的模块','个人使用场景与部署、问题复现和边界判断、AI 协作修复与上游提交。Agent 运行时、工具框架与通道底座来自 Hermes。'),
        ('工程实现','Python 辅助模型客户端重试边界；同会话预处理锁与生命周期清理；不同会话保留并发；cron/flush/subagent 自动记忆捕获过滤。'),
        ('关键取舍','满预算超时转后备路径，快速失败仍可重试；只串行化同会话的相关预处理，避免全局锁阻塞所有用户。'),
        ('可验证结果','原始 #97572 经维护者 #101570 保留作者署名采纳；#97743、#97156 仍待合并。贡献是特定修复，不是独立实现 Hermes。')]),
      'shell': ('自有扩展项目 · 复用 DeepSeek Harness', [
        ('解决的问题','手机打开页面后，仍可能无法建立实时会话；可执行工具的界面需要受控登录入口。'),
        ('我负责的模块','交互外壳、UI 插槽/配置接入、LAN TLS 登录网关与连接验收，均以 AI 协作推进。模型、会话和工具运行能力复用上游。'),
        ('工程实现','TypeScript UI 包 + Node.js 网关；TLS、本地证书、登录保护、WebSocket 代理与 Host 信任配置。'),
        ('约束与难点','页面加载成功与 WebSocket 连接成功是两个条件；局域网 Host 未获上游信任时，登录后仍会被拒绝。'),
        ('可验证结果','公开实验区分未登录 401、Host 未获信任 403、连接成功 101；支持单人 LAN 接入，未宣称完整多租户服务。')]),
      'memory': ('自有工作流 · 自有开源参考实现', [
        ('解决的问题','编码 Agent 切换会话后丢失项目状态、重复尝试失败方案，或者把旧摘要当成当前事实。'),
        ('我负责的模块','Obsidian 项目记录、检索与接续规则、事实/候选分层；公开参考运行时中的事件、权限与回执边界，AI 协作实现。'),
        ('工程实现','本地 Markdown 与项目日志保留来源；Python 参考运行时提供 Event/Receipt、trace_id、Handler 路由及权限准入。'),
        ('约束与难点','长期保存不等于事实永远有效；接续时必须校准代码、部署和历史状态，模型生成的候选不能直接覆盖事实。'),
        ('可验证结果','参考仓包含 4 类终态和 5 个单元测试；完整持久记忆治理与编排仍未全部开源，不把最小运行时当成完整长记忆平台。')]),
      'builder': ('自有产品探索 · 本地底座', [
        ('解决的问题','非技术用户创建 Agent 时，角色、知识、测试和发布状态分散，难以判断实际生效版本。'),
        ('我负责的模块','创建流程、知识处理状态、草稿与发布版本设计，借助 AI 推进本地底座。'),
        ('工程实现','公开案例记录 Next.js、FastAPI、PostgreSQL、Redis、Docker 及身份接入设计；草稿版本冲突保护和来源/chunk 状态。'),
        ('可验证结果','目前以设计和本地底座案例为证据；向量/Provider 完整闭环与第二用户验收未完成，不列为已上线 SaaS。')]),
    }
    if slug not in facts: return ''
    label, rows = facts[slug]
    return '<section class="engineering-summary"><span class="badge">'+label+'</span><h2>工程成果速览</h2><dl>'+''.join('<dt>'+k+'</dt><dd>'+v+'</dd>' for k,v in rows)+'</dl></section>'

def render_engineering(page, article, ext, gh):
    article('projects/data-dashboard.html','WORK · 数据工程与业务交付','投放数据看板：把网页报表接成可信的数据链路','工作项目，企业与数据均已脱敏。重点展示无现成开放 API / CLI / MCP 时的数据接入、准确性控制与工程交付。','''
<section class="engineering-summary"><span class="badge">工作项目 · 自研业务系统 · 非开源框架 Fork</span><h2>成果速览</h2><div class="result-grid"><div><strong>2 类平台</strong><span>同一分析入口，来源口径分别保留</span></div><div><strong>5 类作用域</strong><span>渠道 / 代理 / 运营 / 产品 / 账户</span></div><div><strong>23 项</strong><span>本次本地专项测试通过</span></div></div><p>工程规模与本地验证结果；不代表业务收益提升或最新线上全链路验收。</p></section>
<h2>1. 真实问题：运营拿到的数，未必能直接比较</h2><p>投放数据分散在网页 BI、媒体报表和 Excel。人工导出后再整理，既重复劳动，也容易把不同时间范围、不同来源的同名指标混在一起。运营需要快速定位到产品、账户和时段，且不同人员只能看到自己的数据。</p>
<h2>2. 我的职责：从业务问题到采集、分析和交付</h2><p>我从投放运营需求出发，负责业务对象、字段和指标口径，设计采集、数据校验、分析页面、权限与报表流程，并借助 AI 推进编码、调试、部署与验收。负责范围覆盖数据接入适配、清洗归一化、数据库更新、看板/下钻、定时报表和权限边界。</p><p>我的主责是需求、指标口径、架构取舍、模块拆分与结果验收；编码和调试使用 AI 协作。数据处理、界面和 API 分别复用 pandas、Streamlit、FastAPI 等成熟组件。</p>
<h2>3. 没有现成接口，怎么取数？</h2><p>早期没有可直接调用的官方开放 API、CLI 或 MCP，但网页本身会请求结构化数据。我通过已有授权浏览器会话，使用 Chrome CDP 观察报表请求与响应，识别字段映射、日期条件和真实返回行，再把结构化数据交给清洗与入库流程。Excel 导出和本地 JSON 快照保留为导入/复现路径。</p><p>这使用的是网页内部数据请求，不把它包装成官方开放 API。登录态失效、页面字段变化或结果无法证明完整时，应中止该批数据更新；后期有官方授权的指标独立接入 OAuth/OpenAPI，和 BI 原始口径分别保存。</p>
<div class="pipeline" aria-label="数据流"><span>授权网页 / Excel</span><b>→</b><span>字段、日期、重复校验</span><b>→</b><span>SQLite 按日更新</span><b>→</b><span>权限过滤 / 指标聚合</span><b>→</b><span>看板、下钻、时报</span></div>
<h2>4. 我怎样降低“抓到了，但抓错了”的风险</h2><div class="table-scroll"><table><thead><tr><th>问题</th><th>实现措施</th><th>对业务的意义</th></tr></thead><tbody>
<tr><td>分页参数被忽略，重复抓第一页</td><td>核对实际返回总页数和唯一行；调整有效返回量参数后仍多页则停止入库</td><td>避免数据看起来很多，实际只是重复记录</td></tr>
<tr><td>字段变化或采到错误报表</td><td>恢复字段显示名，按 Profile 归一化；平台识别失败或空明细拒绝导入</td><td>避免错把另一路数据套进当前指标口径</td></tr>
<tr><td>刷新时读到半成品或重复导入</td><td>下载锁、按日替换、去重、行哈希与批次时间；数据库配置 WAL 与写入等待</td><td>让“这一天哪一批数据”可以追踪，控制并发刷新</td></tr>
<tr><td>BI 会补数，固定延时仍不稳定</td><td>只比较已结束小时；两个不同刷新批次的报表字段指纹一致才放行，超时停止推送</td><td>防止未稳定的数据被当作正式时报</td></tr>
<tr><td>ROI 与同比口径错位</td><td>先汇总基础值再计算比率；对齐目标日与对比日的完整时段；来源缺失不冒充 0</td><td>减少错误比较引发的运营判断偏差</td></tr>
<tr><td>权限只藏按钮，导出仍泄露</td><td>服务端统一过滤数据，作用域取交集；无显式范围返回空集，敏感指标单独投影</td><td>筛选、明细、汇总、下钻和导出沿用相同边界</td></tr></tbody></table></div>
<h2>5. 为什么选择这套技术栈</h2><div class="table-scroll"><table><thead><tr><th>层</th><th>已用技术</th><th>与约束的匹配</th></tr></thead><tbody>
<tr><td>接入</td><td>Python / requests / Chrome CDP / WebSocket</td><td>复用已授权网页数据和现有 Python 管道，减少对界面位置与 OCR 的依赖</td></tr>
<tr><td>处理</td><td>pandas / openpyxl / 字段 Profile / 指标注册表</td><td>适配结构化报表和 Excel，统一多来源数据的字段与聚合逻辑</td></tr>
<tr><td>存储</td><td>SQLite / WAL / 行哈希 / 批次记录</td><td>适合当时单机与定时批处理规模，部署和备份成本低；不把它宣称为分布式高并发数据库</td></tr>
<tr><td>产品</td><td>Streamlit / AgGrid / FastAPI</td><td>快速交付筛选和宽表分析；移动查询复用服务端口径，避免再维护一套指标</td></tr>
<tr><td>安全</td><td>Argon2id / Session 哈希 / 角色与作用域 / 审计</td><td>服务端处理登录、失效和数据边界；同步和界面权限独立</td></tr>
<tr><td>运行</td><td>Windows 计划任务 → Linux systemd timer / Nginx / HTTPS</td><td>从本地报表演进到持续可访问服务；此项目不把 Docker 当作已使用的部署成果</td></tr></tbody></table></div>
<h2>6. 可验证结果与价值</h2><p>已形成取数、清洗、入库、筛选、汇总、时段下钻、导出和定时报表的应用链路，支持两类投放平台及五类服务端数据作用域。原流程中手工搬运报表、核对口径和重复发送的步骤被组织为可追踪流程；运营可以从汇总定位到具体时段。</p><p>本次对现有代码运行四组专项测试：数据范围 10 项、跨日/完整时段比较 3 项、数据库结构演进 2 项、时报运行与稳定性 8 项，共 23 项通过。这是本地代码验证，不冒充近期生产运行指标。</p><p>没有可信的前后工时、错误率或收益对照，因此不写“提升百分之多少”。公开材料仅保留框架和验证摘要，不发布公司源码、真实数据、账户、人员映射、内部接口和生产地址。</p>
<div class="source-box"><strong>继续查看</strong><a href="../experience.html">工作经历与职责 →</a><a href="ad-platform.html">另一个项目：投放中台原型 →</a><a href="../notes/data-quality.html">数据准确性实践笔记 →</a><a href="../evidence/engineering-validation.html">脱敏工程验证摘要 →</a></div>''','projects','<p class="eyebrow">项目归属</p><p>公司内部业务项目<br>脱敏展示，源码不公开</p><p class="eyebrow">我的职责</p><p>业务与指标建模<br>数据链路与界面设计<br>AI 协作开发、部署、验证</p><p class="eyebrow">FDE 能力</p><p>现场约束识别<br>已有系统集成<br>可维护交付</p>')

    article('projects/ad-platform.html','WORK · 产品与前端工程','投放中台：先让业务流程可以被操作和讨论','与投放数据看板分开呈现：本项目是业务模型与前端原型，真实取数和生产权限由另一个项目承载。','''
<section class="engineering-summary"><span class="badge neutral">工作相关原型 · 自有前端工程 · 固定模拟数据</span><h2>已实现的能力</h2><p>Vite + React 18 + TypeScript + Tailwind；实时统计、推广管理、今日/历史聚合、综合看板与指标说明；复用表格、筛选栏、弹窗和页面布局组件。</p><a class="button primary" href="../demo/iaa/index.html">打开可交互 Demo ↗</a></section>
<h2>真实问题</h2><p>运营关心的是账户和产品怎样关联、哪些指标放在一起、如何从总览下钻到时段。仅凭需求文档，很难确认宽表、筛选、合计和多个工作页面是否适合日常使用。</p>
<h2>我的职责</h2><p>我负责业务对象、指标口径与页面流程梳理，提出交互要求，使用 AI 协作实现和调整前端原型。负责模块包括布局与导航、可复用 DataTable、FilterBar、条件着色、合计行和时段分析弹窗。</p>
<h2>技术选择为什么不同于数据看板</h2><p>中台原型要验证多页面布局和细粒度交互，选择 Vite + React + TypeScript + Tailwind，方便复用组件并独立构建。数据看板则优先用 Python 处理数据并快速输出分析界面。两者解决的问题不同，不把两套框架堆在同一份成果里。</p>
<h2>具体难点与处理</h2><ul><li><strong>模拟数据漂移：</strong>为每个数据集使用独立固定种子，避免一个组件消耗随机序列后让另一个页面的对照值变化。</li><li><strong>宽表可用性：</strong>把粘性列、排序、指标条件色和合计行集中在通用表格组件，保持不同页面的交互一致。</li><li><strong>产品与实现边界：</strong>数据库和后端只有设计/骨架，不能用前端登录画面证明真实鉴权或租户隔离。</li></ul>
<h2>可验证结果</h2><p>公开 Demo 可以进入工作台、浏览已实现页面和图表，体验表格与时段弹窗，全部使用固定模拟数据。部分菜单、筛选和写操作仍是原型占位。演示登录只控制体验入口；它不是安全边界，不连接公司数据或后端。</p><p>这个原型的价值是让业务流程和界面要求变得可讨论、可验证，为后续取舍提供依据。未完成的后端和数据库不计入已落地成果。</p>
<div class="source-box"><strong>项目关系</strong><a href="../demo/iaa/index.html">体验固定数据原型 →</a><a href="data-dashboard.html">查看实际数据看板工程 →</a><a href="../evidence/engineering-validation.html">查看验证与展示范围 →</a></div>''','projects','<p class="eyebrow">项目归属</p><p>工作相关产品原型<br>不是成熟生产中台</p><p class="eyebrow">技术</p><p>Vite · React 18<br>TypeScript · Tailwind<br>固定种子 Mock</p>')

    page('experience.html','工作经历与项目职责','脱敏展示数字营销业务中的投放中台与投放数据看板项目。','''<section class="wrap listing"><p class="eyebrow">EXPERIENCE</p><h1>在业务现场，<br>把问题推进到<span class="accent">可用系统。</span></h1><p class="listing-lead">某数字营销公司 · 任职期间项目实践（公司及业务数据脱敏）</p><div class="editor-note">项目职责：业务分析、数据产品设计、AI 协作开发与工程交付。下方分别展示两个项目的实现阶段和成果。</div>
<div class="experience-block"><p class="eyebrow">业务数据产品 / AI 协作开发与交付</p><h2>从投放运营需求，到中台原型与数据看板</h2><p>围绕产品、账户、代理和运营的协作，梳理指标口径及查询流程。先用前端原型验证操作方式，再在数据看板中处理真实的数据接入、质量控制、服务端权限与部署。</p><h3>承担的工作</h3><ul><li>把业务指标和对象关系转成字段映射、计算口径、页面筛选及下钻规则。</li><li>在没有现成开放接口的阶段，从已有授权网页报表识别结构化数据请求，设计采集和导入路径。</li><li>围绕重复抓取、BI 补数、时间范围不一致等故障设计校验和停止条件。</li><li>借助 AI 推进 Python 数据管道、Web 界面、鉴权和部署，按业务结果验收。</li></ul><h3>交付价值</h3><p>将分散的网页/Excel 报表组织为统一查询和分析入口；把取数、校验、聚合和汇报串联起来；通过服务端数据范围减少跨角色误读与越权风险。</p></div>
<div class="project-grid"><a class="project-card" href="projects/data-dashboard.html"><span class="badge">实际数据工程</span><h3>投放数据看板</h3><p>采集、清洗、数据库、口径、权限、时报和部署。查看具体坑点与 23 项本地验证。</p><span class="card-bottom">Python / SQLite / Streamlit / FastAPI →</span></a><a class="project-card" href="projects/ad-platform.html"><span class="badge neutral">产品与前端原型</span><h3>投放中台</h3><p>业务建模和中台交互。查看可以操作的固定模拟数据 Demo。</p><span class="card-bottom">React / TypeScript / Tailwind →</span></a></div>
<h2>这些经历如何对应 FDE</h2><p>理解现场流程和系统约束，找到实际可用的数据入口，做出最小可用方案，再补齐准确性、权限、运行与交付。技术选择围绕业务问题展开，而不是先选一套框架再寻找应用场景。</p></section>''','experience')

    page('skills.html','技能与工程能力','按实际项目分类展示数据工程、应用开发、Agent 集成、鉴权部署和产品交付能力。','''<section class="wrap listing"><p class="eyebrow">SKILLS / EVIDENCE</p><h1>技能，放到<span class="accent">实际项目</span>里看。</h1><p class="listing-lead">按做过的工作归类，每项都有对应案例。能力来自 AI 协作开发与实际验证，不以“精通所有技术栈”概括。</p><div class="skill-grid">
<section><h2>业务分析与 FDE 交付</h2><p>需求拆解、业务对象建模、指标口径、流程原型、验收标准、部署约束与交接。</p><a href="experience.html">投放中台与数据看板 →</a></section>
<section><h2>数据接入与准确性</h2><p>让分散的报表可以一起看，并在数据不完整或口径不一致时及时发现问题。</p><details><summary>技术与实现范围</summary><p>Python、pandas、Excel；Chrome CDP/结构化响应；字段归一化、重复检测、时间对齐、批次指纹、缺失值语义。</p></details><a href="projects/data-dashboard.html">无开放接口的数据链路 →</a></section>
<section><h2>Web 与 API 开发</h2><p>把需求做成能操作的页面、内容后台和数据服务。</p><details><summary>技术与实现范围</summary><p>React、TypeScript、Vite、Tailwind；Next.js/Hono；Streamlit/AgGrid、FastAPI；内容管理与异步 API 调用。</p></details><a href="projects/blog.html">开源内容发布系统 →</a></section>
<section><h2>数据库与鉴权</h2><p>让数据持续保存，并让每个人只看到自己有权访问的内容。</p><details><summary>技术与实现范围</summary><p>SQLite/WAL、PostgreSQL/Drizzle；账号登录、密码哈希、Session、租户过滤、角色和数据作用域。</p></details><a href="projects/data-dashboard.html">服务端数据边界 →</a></section>
<section><h2>Agent 集成与可靠性</h2><p>处理消息乱序、失败重试和后台内容误入记忆等真实使用问题。</p><details><summary>技术与实现范围</summary><p>Hermes 二次开发、重试与后备路径、同会话异步预处理、自动记忆写入边界、事件与回执。</p></details><a href="contributions.html">公开修复与合入记录 →</a></section>
<section><h2>部署、调试与协作</h2><p>把应用接到实际使用环境，定位访问故障，并留下可恢复的版本。</p><details><summary>技术与实现范围</summary><p>Linux/systemd、Nginx/HTTPS、LAN TLS/WebSocket、Git/PR、版本恢复、pytest。Docker/Redis 仅列于本地创建平台探索，未当作投放看板生产成果。</p></details><a href="projects/shell.html">LAN 网关接入与故障定位 →</a></section></div><div class="editor-note">能力主线：业务理解 → 数据与系统集成 → 应用交付 → 验证和维护。点击各项案例查看具体实现与当前阶段。</div></section>''','skills')

    article('evidence/engineering-validation.html','EVIDENCE · 脱敏验证摘要','投放项目：工程能力与证据范围','仅公开验证方法和结果，不公开雇主源码、真实数据、账户、域名或内部接口。','''
<h2>本次核对范围 · 2026-09-05</h2><p>只读核对了投放数据看板现有代码、依赖与相关项目记录，以及投放中台当前状态、组件结构和已公开的演示产物。未重新访问公司系统、采集业务数据或修改生产服务。</p>
<h2>本地专项验证</h2><div class="table-scroll"><table><thead><tr><th>测试组</th><th>数量</th><th>证明的范围</th></tr></thead><tbody><tr><td>服务端数据范围</td><td>10 通过</td><td>跨代理、运营、产品和账户过滤，显式权限及指标投影</td></tr><tr><td>时段比较</td><td>3 通过</td><td>跨日范围、目标日选择、双方排除进行中小时</td></tr><tr><td>数据库结构演进</td><td>2 通过</td><td>新增字段和来源字段投影</td></tr><tr><td>时报运行与稳定性</td><td>8 通过</td><td>已结束时段指纹、不同刷新批次及运行约束</td></tr></tbody></table></div><p>合计 23 项通过。测试运行在本地现有项目上，不证明全部生产异常均被覆盖，也不等同于最新线上验收。</p>
<h2>可公开量化的内容</h2><ul><li>数据看板覆盖两类投放平台；服务端具备渠道、代理、运营、产品、账户五类数据作用域。</li><li>稳定性判断需要两个不同刷新批次的已结束时段事实一致；不是反复读取同一份数据。</li><li>中台 Demo 使用固定模拟数据，提供页面导航、表格与筛选交互；不连接后端。</li></ul>
<h2>归属与复查边界</h2><p>投放项目属于工作场景，生产源码不公开。此页为基于本地代码和测试回执整理的脱敏说明，外部读者不能独立访问企业测试环境。可直接操作的公开材料是中台模拟 Demo；个人开源项目和上游 PR 可到对应仓库检查。</p><p>没有可靠的工时、业务 ROI 或故障率前后对照，因此未提供效率/收益百分比。</p><div class="source-box"><strong>公开入口</strong><a href="../projects/data-dashboard.html">数据看板案例 →</a><a href="../demo/iaa/index.html">中台模拟 Demo →</a><a href="../contributions.html">个人开源贡献 →</a></div>''','projects')

    article('notes/data-quality.html','工作实践 · 数据工程','没有开放 API 时，如何避免“抓到了，但抓错了”？','我在投放数据看板中遇到的分页和 BI 补数问题，以及对应的校验方法。','''
<section class="case-anchor"><span class="badge">工作项目 · 本地代码与测试核对</span><h2>对应我的实践</h2><a href="../projects/data-dashboard.html">投放数据看板：授权网页取数与稳定性校验 →</a></section>
<h2>网页能看，不代表有现成开放接口</h2><p>当时可用的入口是授权后的网页 BI 和导出报表。我从浏览器网络响应找到结构化字段与行数据，再对日期、字段和结果范围做校验。这是对网页内部数据请求的适配，不是拿到了一份官方 OpenAPI。</p>
<h2>第一个坑：页码增加，数据却不变</h2><p>该报表忽略了一个常见页码参数，真正控制返回量的是表格配置中的另一个参数。如果照常循环页码，会把第一页重复多次。我的管道因此检查实际总页数和唯一行；返回仍不完整或出现疑似重复分页时，中止入库，不能把更大的行数当作成功。</p>
<h2>第二个坑：同一小时的数据还在变</h2><p>BI 会修订已出现的数据，单纯等几分钟不能证明稳定。时报采用批次时间判断数据确实刷新过，再对报表实际消费的已结束小时字段生成与行顺序无关的指纹。两个不同批次一致才放行，期间若继续变化则继续等，超时不推送。</p>
<h2>准确性需要多层判断</h2><p>取数层校验字段和完整性，处理层做归一化与去重，分析层对齐时间范围和指标来源，发布层检查数据稳定性。官方数据缺失不能用另一来源的同名字段冒充，更不能无条件填零。</p>
<h2>我能拿出什么证据</h2><p>本次在现有代码上复跑了数据范围、时段比较、数据库演进、时报运行和稳定性的 23 项专项测试，全部通过。它们说明对应实现满足这些测试条件，不是对源系统数据真实性的无限保证。</p><div class="source-box"><strong>继续查看</strong><a href="../projects/data-dashboard.html">技术选型与职责 →</a><a href="../evidence/engineering-validation.html">脱敏测试范围 →</a></div>''')
