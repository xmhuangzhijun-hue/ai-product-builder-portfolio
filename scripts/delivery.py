"""Recruiter-facing outcomes and direct verification paths."""
GH='https://github.com/xmhuangzhijun-hue/'
CASES={
 'data-dashboard':('业务交付 · 源码不公开','23 项本地专项测试','不同来源的报表口径混杂，人工整理容易漏数或重复。','设计取数、口径、权限与交付验收，借助 AI 实现。','覆盖 5 类数据作用域；23 项指定本地测试通过。','evidence/engineering-validation.html','脱敏测试摘要'),
 'ad-platform':('可交互原型 · 模拟数据','1 个公开模拟 Demo','投放账户、产品与指标流程需要在开发前对齐。','把业务对象变成页面、筛选与操作原型。','可体验固定数据原型；部分操作仍为占位。','demo/iaa/','在线模拟 Demo'),
 'blog':('MIT 开源 · 原站备案中','61 篇发布文章已核对','更新内容依赖修改页面代码，难以持续维护。','定义内容模型与发布流程，协作实现后台并部署。','只读接口核对到 61 篇发布文章；源码含后台与存储实现。',GH+'xmhua-card','源码与部署说明'),
 'assistant':('个人自用 · Hermes Fork','1 项修复获上游采纳','个人信息分散，助手反复需要背景且执行结果难确认。','连接 Obsidian、记忆与 MCP 工具，定义结果验收。','视觉超时修复经维护者保留署名整合合入。','https://github.com/NousResearch/hermes-agent/pull/101570','上游合入记录'),
 'shell':('开源原型 · 完整手机流程待验收','3 类连接状态有记录','手机能打开页面，却无法登录或接入实时会话。','增加界面外壳、TLS 登录与 WebSocket 网关。','连接实验覆盖 401 / 403 / 101；不等同手机任务闭环。',GH+'ruoxi-shell','源码与连接实验'),
 'memory':('开源参考实现 · 早期','4 类执行终态','跨会话接续丢失依据，执行完成与未知状态混淆。','设计来源分层与接续规则，公开最小执行实验。','参考实现包含 4 类终态与 5 个单元测试。',GH+'organic-agent-os','参考代码与测试'),
 'builder':('产品探索 · 本地底座','方案与实现边界公开','配置、知识处理与发布状态分散，用户难判断进度。','拆解创建、检查与发布流程，探索本地底座。','产品流程与底座案例可查，完整 SaaS 尚未验收。',GH+'ai-product-builder-portfolio/blob/main/docs/organic-console.md','公开方案与范围'),
}
def evidence_link(slug,base='@BASE@'):
    c=CASES[slug];url=c[5] if c[5].startswith('https://') else base+c[5]
    return f'<a href="{url}"'+(' target="_blank" rel="noopener noreferrer"' if url.startswith('https://') else '')+f'>{c[6]} ↗</a>'
def case_grid(slug):
    if slug not in CASES:return ''
    c=CASES[slug]
    return '<section class="case-four" aria-label="案例快速评估">'+''.join(f'<div><h2>{k}</h2><p>{v}</p></div>' for k,v in [('场景',c[2]),('我的动作',c[3]),('结果',c[4]),('证明材料',evidence_link(slug))])+'</section>'
def grouped_cards(projects,roles):
    groups=[('数据交付','从分散报表到可检查的数据链路',['data-dashboard']),('产品原型与发布','把业务需求变成可操作、可维护的产品',['ad-platform','blog']),('Agent 工程','连接上下文、工具与实际使用入口',['assistant','shell','memory'])]
    by_slug={p[0]:p for p in projects};out='<div class="work-columns">'
    for title,desc,slugs in groups:
        out+=f'<section class="work-column"><h3>{title}</h3><p class="group-lead">{desc}</p>'
        for slug in slugs:
            _,name,title,desc,tags=by_slug[slug];c=CASES[slug]
            out+=f'<a class="project-card" href="@BASE@projects/{slug}.html"><span class="maturity">{c[0]}</span><h4>{title}</h4><p>{roles[slug][1]}</p><strong class="result-anchor">{c[1]}</strong><p class="role-tag">我的主责：{roles[slug][0]}</p><div class="card-bottom">{tags.split(" · ")[0]}</div></a>'
        out+='</section>'
    return out+'</div>'
def matrix(projects):
    rows=''.join(f'<tr><th scope="row"><a href="projects/{p[0]}.html">{label}</a></th><td>{CASES[p[0]][4]}</td><td>{evidence_link(p[0])}</td></tr>' for p,label in zip(projects,['投放数据看板','投放中台原型','内容发布系统','个人助手实例','手机接入扩展','上下文与执行实验']))
    return '<section class="wrap section" id="verify"><div class="section-head"><div><p class="eyebrow">VERIFY THE WORK</p><h2>每个结论，都有检查入口。</h2></div><p>先看案例，再看源码、测试摘要或演示。</p></div><div class="table-scroll"><table class="verification-table"><thead><tr><th>项目</th><th>可以核对什么</th><th>直接查看材料</th></tr></thead><tbody>'+rows+'</tbody></table></div><p class="evidence-scope">数字分别指本地测试、公开实验或历史只读核对，不合并为业务收益；尚无可披露的取数耗时前后测量。</p></section>'
def upstream():
    return '''<section class="wrap upstream-feature" id="upstream"><p class="eyebrow">OPEN SOURCE / 外部可核验</p><span class="badge">1 项原始修复获采纳</span><h2>图片已经超时，为什么还要再等一次？</h2><p>我从个人助手的使用问题出发，定位视觉请求的重试边界，将修复提交 Hermes 上游。</p><div class="before-after"><div><h3>修复前</h3><p>一次请求已耗尽完整超时预算，通用重试仍可能再次调用同一服务，继续占用等待时间。</p></div><div><h3>我的判断与修复</h3><p><strong>区分“快速失败”与“预算已耗尽”。</strong>后者停止同一路径的重复等待，交给后备流程；快速失败仍保留重试机会。</p></div><div><h3>可检查的结果</h3><p>原始 PR #97572 被维护者保留作者署名，通过 #101570 整合合入。改善的是等待路径，未宣称测得统一的端到端提速比例。</p></div></div><div class="hero-actions"><a class="button primary" href="https://github.com/NousResearch/hermes-agent/pull/101570" target="_blank" rel="noopener noreferrer">查看上游合入 ↗</a><a class="button" href="https://github.com/NousResearch/hermes-agent/pull/97572" target="_blank" rel="noopener noreferrer">原始贡献 ↗</a><a class="text-link" href="notes/vision-timeout.html">阅读修复复盘 →</a></div></section>'''
