"""Career case studies grounded in the author's public repositories and blog."""

def render(page, article, ext, gh, hermes, note_list):
    blog = gh + '/xmhua-card'
    shell = gh + '/ruoxi-shell'
    runtime = gh + '/organic-agent-os'

    article('projects/blog.html', 'PROJECT 01 · AI 协作开发', '我自己的博客：从展示页，到内容发布系统', '我既是需求提出者，也是实际使用者。这个项目展示我如何借助 AI，把“有一个网站”推进到内容可以持续维护。', f'''
<h2>起点：我需要一个能持续更新的个人博客</h2><p>最初的页面能展示介绍，但发布笔记、改项目和更新联系方式，都不应该依赖开发者每次改代码。我的要求逐渐明确：自己在后台完成内容维护，读者在公开页面读到完整正文，保存后的内容持续存在。</p>
<h2>我负责的部分</h2><p>我提出并校正产品目标，决定笔记、项目、社交入口与独立页面这些内容对象，围绕编辑、保存、发布和公开阅读提出验收要求；开发、调试与部署过程中使用 AI 协作。公开仓库提供实现细节，便于检查这些要求怎样落地。</p>
<div class="flow"><span>后台编辑</span><b>→</b><span>API 校验与写入</span><b>→</b><span>PostgreSQL</span><b>→</b><span>公开页面读取</span></div>
<h2>三个具体取舍</h2><ul><li><strong>前后端独立：</strong>Next.js 负责页面，Hono API 负责鉴权、数据和写入。前端不直接持有数据库连接。</li><li><strong>草稿与发布分开：</strong>公开读取按发布标志过滤。后台保存了一条内容，不代表访客就应该看到它。</li><li><strong>真实入口优先：</strong>未填写地址的链接不显示；二维码联系入口需要真实图片。内容完整性也是产品可用性的一部分。</li></ul>
<h2>现在能核对到什么</h2><p>2026 年 9 月 5 日，通过已部署 API 的只读接口核对到 PostgreSQL 中有 <strong>61 篇已发布文章</strong>，并读到了实际微信入口。源代码公开，包含内容后台、数据模型、API 与部署说明。原站正处于备案审核期间，因此求职内容在此站公开阅读。</p><p>这次核对证明已部署数据可读取；没有在本次核对中重新执行后台保存或整机恢复测试。GitHub Pages 求职版是精选静态发布，内容后台属于原博客系统。</p>
<h2>从项目延伸出的实践笔记</h2><ul><li><a href="../notes/project-boundaries.html">用 AI 做博客时，我怎么定义“做完了”？</a></li><li><a href="../notes/blog-delivery.html">一个博客，怎样才算真的交付了？</a></li></ul>
<div class="source-box"><strong>检查这个项目</strong>{ext(blog,'完整开源仓库')}{ext(blog+'/blob/master/api/src/services/content.ts','发布状态与内容读取源码')}{ext(blog+'/blob/master/docs/DEPLOYMENT.md','部署与验收说明')}</div>''', 'projects', '<p class="eyebrow">我的角色</p><p>项目发起者 / 产品定义<br>AI 协作开发与验收</p><p class="eyebrow">技术</p><p>Next.js · TypeScript<br>Hono · Drizzle · PostgreSQL</p><p class="eyebrow">阶段</p><p>已部署、自用<br>源码公开 · MIT</p>')

    article('projects/shell.html', 'PROJECT 03 · AGENT 交互', '让手机也能连接自己的 Agent', '在 DeepSeek Harness 的已有能力上增加交互外壳和局域网登录入口，处理从“能看页面”到“能连接会话”的差距。', f'''
<h2>我想解决的使用问题</h2><p>Agent 在电脑上运行，但我希望能从手机进入同一个交互环境。增加一个页面并不足够：登录、可信连接、会话消息以及上游的能力入口都需要一起工作。</p>
<h2>我的项目实现</h2><p>我发起 ruoxi-shell，借助 AI 制作交互外壳和局域网网关。外壳接入上游的 UI 插槽和配置补丁，保留会话、工作区、工具、权限、轨迹与任务等原有能力；网关提供 TLS 和登录。</p><p>这些核心 Agent 能力来自 DeepSeek Harness。我的仓库提供附加界面和接入层，没有把上游运行时称为自己的实现。</p>
<h2>关键取舍：跟随上游，减少侵入</h2><p>用上游公开的扩展位置接入，而不修改上游源码。移除配置补丁即可移除外壳，代价是少量页面品牌仍在加载时显示上游值。这个取舍把后续维护成本放在视觉上的完全一致之前。</p>
<h2>最有代表性的一次接入验证</h2><p>公开 README 记录了：未登录的 WebSocket 升级返回 401；登录后允许连接时返回 101；局域网 Host 没有加入上游信任配置时返回 403。页面打开后不更新，问题发生在会话连接层。</p><p>这组记录来自 V1 构建时的实验，本次重新检查的是公开代码和记录，没有重新运行手机端语音或通话验收。</p>
<h2>目前的使用范围</h2><p>单人家庭局域网的早期实现，依赖用户自己的 DeepSeek Harness 环境。仓库不分发人物、声音和视频资产，也不是已商业化的多用户伴侣平台。</p><div class="source-box"><strong>检查这个项目</strong>{ext(shell,'项目与实验记录')}{ext(shell+'/blob/main/gateway/gateway.mjs','登录与连接网关源码')}{ext(shell+'/blob/main/packages/ui-shell/src/client/AvatarStage.tsx','交互舞台实现')}<a href="../notes/lan-access.html">阅读手机接入复盘 →</a></div>''', 'projects', '<p class="eyebrow">我的角色</p><p>项目发起者<br>交互需求与接入设计<br>AI 协作实现</p><p class="eyebrow">技术</p><p>TypeScript · Node.js<br>UI 插槽 · TLS · WebSocket</p><p class="eyebrow">阶段</p><p>早期实现 · 源码公开<br>单人局域网使用</p>')

    article('notes/blog-delivery.html', '实践笔记 · 从阅读到项目', '一个博客，怎样才算真的交付了？', '原博客的上线笔记讲可观察、可恢复；我把它对应到自己正在使用的内容发布系统。', f'''
<h2>原笔记提出的问题</h2><p>我原先整理过《Vibe Coding 项目的上线、运维与可恢复性验收》。其中对我有用的判断是：页面能打开，只能证明一次访问成功。上线还需要知道内容存在哪里、运行的是哪个版本，以及出问题后怎样恢复。</p>
<h2>在我的博客中，它具体意味着什么</h2><p>这个博客同时有页面、内容 API 和数据库。看见页面不代表后台改动已经保存；API 返回 200 也不代表读者看见了新正文。所以验收需要沿用户的完整路径走：编辑内容、保存、重新读取，再检查公开文章。</p><p>我把笔记、项目、社交入口都放进可维护的内容对象中。这次求职站改版就是一个真实使用案例：不是从代码种子里猜微信号，而是从已部署内容 API 读取了我实际发布的微信入口。</p>
<h2>本次读到了什么</h2><p>2026 年 9 月 5 日，原博客 API 返回的数据来源标记为 PostgreSQL，读到 61 篇已发布文章和微信二维码。文章包括我对 Agent、AI 开发流程和知识管理的整理。这些是发布数量和数据读取证据，不是阅读量或招聘效果指标。</p>
<h2>部署方案为什么要考虑机器约束</h2><p>项目部署文档记录服务器资源不足以承担 Next.js 构建，因此在本地 Linux 环境构建，再上传产物。前端和后端分开运行、分别检查，版本目录和切换步骤也写进了文档。</p><p>我希望自己下次更新时仍能解释“改的是哪一版、数据在哪里、怎样退回去”。具体命令可以交给工具执行，这些判断仍需要自己掌握。</p>
<h2>我现在怎样使用这条经验</h2><p>做 AI 协作项目时，先把完成条件写成使用者能观察的结果，再决定要补哪些技术检查。原博客的保存和发布路径是一种验收；这里的静态求职站则要验证匿名访问、文章正文、项目链接和联系方式。两者不能套用同一份成功报告。</p><div class="source-box"><strong>本人的应用证据</strong>{ext(blog+'/blob/master/docs/DEPLOYMENT.md','原博客部署与恢复步骤')}{ext(blog+'/blob/master/api/src/routes/public.ts','公开内容接口')}<a href="../projects/blog.html">我的博客项目案例 →</a></div>''')

    article('notes/project-boundaries.html', '实践笔记 · AI 产品交付', '用 AI 做博客时，我怎么定义“做完了”？', '把开发流程中的范围、架构与验收，落到我自己的内容产品中。', f'''
<h2>我从原笔记里保留了什么</h2><p>《Vibe Coding 开发流程》讨论了项目规则与阶段计划。对我的价值，是把一句模糊的“帮我做博客”拆成明确的产品行为。但有了文档仍不够，AI 的总结不能替代真正使用。</p>
<h2>一次真实的目标纠正</h2><p>我需要的是个人博客，不只是能展示介绍的页面。这改变了实现的重点：文章要有完整正文，内容要能在后台编辑，保存要进入持续存在的数据存储，公开页面要正确读取发布状态。</p>
<h2>我把需求落成了哪些对象</h2><p>笔记有标题、摘要、正文、发布时间和发布标志；项目有说明和外部入口；联系方式既要支持链接，也要支持二维码。它们都需要让站点主人维护，而不是散落在前端代码里。</p><p>公开源码中的内容服务按租户读取数据，只返回已发布文章；未填写的链接会被过滤。读者看到的状态因此有明确的数据依据。</p>
<h2>架构取舍与产品行为是连在一起的</h2><p>前端负责展示，独立 API 负责写入、鉴权与 PostgreSQL。这样的分工让页面和内容管理各有稳定边界。对我而言，选择技术栈不是列出熟悉的名词，而是说明它怎样支持后续编辑、发布和维护。</p>
<h2>我负责什么，AI 帮了什么</h2><p>我负责提出需求、纠正偏离目标的方案、决定关键取舍，并从使用者角度检验结果。调研、编码、调试和部署由 AI 协作推进。我不把 AI 生成的每一行代码当作独立手写能力，也不把提出需求当作已经完成交付。</p>
<h2>这次求职站同样接受这个标准</h2><p>招聘方需要快速看见联系入口，并沿文章找到个人实践与公开材料。因此，正文是否完整、案例是否具体、证据能否打开，比单纯增加文章数量更重要。</p><div class="source-box"><strong>从需求到代码</strong>{ext(blog+'/blob/master/README.md','项目功能与结构')}{ext(blog+'/blob/master/api/src/services/content.ts','发布过滤与链接处理')}{ext(blog+'/blob/master/api/src/db/schema.ts','内容数据模型')}</div>''')

    article('notes/lan-access.html', '实践笔记 · 开源项目复盘', '页面打开了，为什么手机上的 Agent 还不能用？', '我的 ruoxi-shell 接入案例：页面加载、登录和实时会话连接，需要分别核对。', f'''
<h2>具体场景</h2><p>我希望手机可以访问自己的 Agent，于是在 DeepSeek Harness 上增加交互外壳和局域网网关。目标不只是显示界面，还要能进入已有会话并收到更新。</p>
<h2>公开实验记录中的三个结果</h2><div class="table-scroll"><table><thead><tr><th>条件</th><th>WebSocket 结果</th><th>说明</th></tr></thead><tbody><tr><td>未登录</td><td>401</td><td>网关拒绝连接</td></tr><tr><td>已登录，但局域网 Host 未获信任</td><td>403</td><td>请求到达上游后被拒绝</td></tr><tr><td>登录和 Host 配置都满足</td><td>101</td><td>升级到实时连接</td></tr></tbody></table></div>
<h2>它为什么容易误判</h2><p>页面和实时会话使用不同的请求路径。HTML 已经加载成功，不能证明后面的连接成功。此时继续改页面提示或对话 Prompt，都不会改变上游拒绝连接的事实。</p>
<h2>我的实现选择</h2><p>把 TLS 和登录放进独立网关；界面通过上游扩展位置接入。语音相关浏览器能力还受设备与安全上下文影响，因此 HTTPS 和可信证书是接入设计的一部分，不能仅检查桌面端页面。</p>
<h2>结果与边界</h2><p>公开仓库保留了 V1 构建时的连接记录和接入文档。这说明我处理过一个具体的接入问题，不表示所有手机浏览器、语音识别和实时通话组合均已通过测试。当前项目限定单人局域网。</p><div class="source-box"><strong>复现与源码</strong>{ext(shell+'#verified-behaviour','原始实验记录')}{ext(shell+'/blob/main/gateway/README.zh.md','网关接入说明')}{ext(shell+'/blob/main/gateway/gateway.mjs','网关实现')}</div>''')

    article('notes/trace-evaluation.html', '实践笔记 · 可运行实验', 'Agent 说“完成了”，我用什么来核对？', '将原博客的 Agent 评测笔记，对应到自己公开的最小运行时实验。', f'''
<h2>从评测文章回到一个小问题</h2><p>我整理过《Agent 评测不能只看答案》。文章讨论轨迹、真实任务和边界条件。我没有把这套完整评测体系都实现出来，而是先在自己的参考运行时里验证一个更小的问题：执行结果能否明确区分成功、拒绝、失败和未知。</p>
<h2>我的参考实现检查什么</h2><p>运行时接收一个事件，先检查是否允许该风险类型，再查找处理器并执行，最后产生与事件关联的回执。语义判断仍由模型或调用方完成；这里的代码只执行明确的权限和状态约束。</p><ul><li><strong>成功：</strong>处理结果返回，并保留原事件的 trace_id。</li><li><strong>拒绝：</strong>没有被允许的外部动作在执行前被拒绝。</li><li><strong>失败：</strong>处理器抛异常后产生失败回执。</li><li><strong>未知：</strong>没有处理器时不能宣称成功。</li></ul>
<h2>为什么这些小测试值得公开</h2><p>读者可以直接打开测试文件，检查断言究竟证明什么。仓库目前有五个相关测试，包括显式允许某类外部动作的情况。它们比一句“我的 Agent 很可靠”更具体，也暴露了这个实现的实际范围。</p>
<h2>可以怎样复现</h2><pre><code>python -m unittest discover -s tests -v
python examples/heartbeat.py</code></pre><p>在参考项目根目录运行上述命令。示例使用合成数据，不需要个人知识库或真实用户内容。</p>
<h2>不能从中推出什么</h2><p>这不是完整 Agent 评测平台，没有证明长期自主运行、多租户隔离或全部工具链可靠。持续存储、广泛 Provider 集成和学习机制仍是公开路线图中的待办。我的下一步需要围绕真实任务继续验证，而不是把最小实验包装为成熟系统。</p><div class="source-box"><strong>检查实验</strong>{ext(runtime+'/blob/main/tests/test_runtime.py','测试与断言')}{ext(runtime+'/blob/main/src/organic_agent_os/runtime.py','事件执行与回执源码')}{ext(runtime+'/blob/main/ROADMAP.md','尚未完成的工作')}</div>''')

    page('notes/index.html','实践笔记','每篇笔记对应我自己的项目、使用场景或开源实验。', f'''<section class="wrap listing"><p class="eyebrow">FIELD NOTES / 08</p><h1>我读过什么，<br>也写清楚<span class="accent">我怎么用。</span></h1><p class="listing-lead">从原博客的学习积累中，选出能接到个人实践的主题。<br>每篇开头都给出对应项目、当前阶段与公开证据。</p><div class="editor-note">这里有项目复盘、开源提交，以及从原博客重新整理的应用笔记。研究过一个框架不等于已经部署它；每篇按实际完成的范围说明。</div><div class="notes-section">{note_list()}</div></section>''','notes')

    page('about.html','关于与联系','XMHUA 的求职方向、个人贡献、项目入口与直接联系方式。',f'''<section class="wrap about-page"><p class="eyebrow">ABOUT XMHUA</p><h1>既关心产品怎么用，<br>也愿意把它<span class="accent">做出来。</span></h1><p class="about-intro">我关注 AI 产品、Agent 应用和知识系统。以自己的真实需求作为起点，借助 AI 做产品定义、实现、部署和持续改进。公开账号是 xmhuangzhijun-hue。</p><div class="about-columns"><div><h2>求职方向</h2><p><strong>AI 产品经理：</strong>拆解用户任务、设计功能流程、定义状态和验收标准，推动从原型到可用产品。</p><p><strong>AI 应用开发：</strong>集成开源 Agent、构建 Web 与 API、处理数据持久化与部署问题，并把可复现的修复提交上游。</p><h2>我的协作方式</h2><p>需求、优先级和关键取舍由我负责；调研、编码与调试使用 AI 协作。底层框架、我发起的项目、个人提交和维护者后续改动分别注明。</p></div><div><h2>可以先看这三项</h2><ol><li><a href="projects/blog.html">个人博客：从需求到内容发布系统</a></li><li><a href="notes/vision-timeout.html">Hermes 修复：从使用问题到上游采纳</a></li><li><a href="projects/shell.html">Agent 外壳：从电脑界面到手机接入</a></li></ol><h2>其他探索</h2><p><a href="projects/memory.html">Agent 记忆与知识管理</a>展示我的长期实践和参考实现；<a href="projects/builder.html">Agent 创建平台</a>目前是产品方案与本地底座，作为补充材料保留。</p><p>{ext(gh,'查看对外 GitHub 账号')}</p></div></div><div class="about-end"><a class="button primary" href="#contact">直接联系我 ↓</a><a class="button" href="notes/index.html">阅读实践笔记</a></div></section>''','about')
