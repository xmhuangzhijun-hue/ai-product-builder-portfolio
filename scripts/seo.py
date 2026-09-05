"""Canonical URLs and metadata for the static GitHub Pages site."""
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from html import escape
import json, re

ORIGIN='https://xmhuangzhijun-hue.github.io/ai-product-builder-portfolio/'
PREFIX='/ai-product-builder-portfolio/'

def canonical(path):
    return ORIGIN + (path[:-10] if path.endswith('index.html') else path)

def normalize_links(html, path):
    def replace(m):
        link=m.group(1)
        if link.startswith('#') or urlsplit(link).scheme or link.startswith('//'): return m.group(0)
        target=urlsplit(urljoin(ORIGIN+path,link))
        normalized=target.path
        if normalized.endswith('/index.html'): normalized=normalized[:-10]
        return 'href="'+normalized+('?' + target.query if target.query else '')+('#'+target.fragment if target.fragment else '')+'"'
    return re.sub(r'href="([^"]*)"',replace,html)

HOOKS={
 'index.html':'FDE 求职作品集：业务集成、数据质量与 Agent 应用交付，附 Hermes 上游采纳记录。',
 'projects/data-dashboard.html':'无开放 API 时的授权网页取数、数据校验与看板交付；附 23 项本地专项测试摘要。',
 'projects/assistant.html':'Hermes 二次开发：视觉重试、消息顺序与记忆边界；附原始 PR 和上游采纳记录。',
 'projects/blog.html':'个人博客的内容后台、独立 API 与 PostgreSQL；附开源实现和 61 篇发布文章核对说明。',
 'projects/shell.html':'Agent 手机交互外壳与 LAN 登录网关；附公开源码及 401、403、101 连接实验记录。',
 'projects/memory.html':'项目记忆接续与 Agent 参考运行时；附公开案例、4 类终态和 5 个边界测试。',
 'projects/ad-platform.html':'投放中台的业务模型与 React 原型；附可操作的固定模拟数据 Demo，注明未完成范围。',
 'projects/builder.html':'Agent 创建与发布的本地底座探索；附流程设计、技术选择和当前实现边界。',
}

def finalize(out, pages):
    manifest=[]
    for path, info in pages.items():
        p=out/path; html=p.read_text(encoding='utf-8')
        title,description=info
        description=HOOKS.get(path,description)
        if path.startswith('notes/') and path!='notes/index.html': description+=' 附对应个人案例与可检查材料。'
        url=canonical(path)
        slug=path.removesuffix('.html').replace('/','-')
        img=ORIGIN+'static/og/'+slug+'.jpg'
        html=re.sub(r'(<meta name="description" content=")[^"]*',lambda m:m[1]+escape(description,quote=True),html)
        html=re.sub(r'(<meta property="og:description" content=")[^"]*',lambda m:m[1]+escape(description,quote=True),html)
        html=re.sub(r'(<meta property="og:url" content=")[^"]*',lambda m:m[1]+url,html)
        html=re.sub(r'(<link rel="canonical" href=")[^"]*',lambda m:m[1]+url,html)
        typ='article' if path.startswith('notes/') and path!='notes/index.html' else 'website'
        html=re.sub(r'(<meta property="og:type" content=")[^"]*',lambda m:m[1]+typ,html)
        person={'@type':'Person','@id':ORIGIN+'#person','name':'黄智军','alternateName':'xmhuangzhijun-hue','url':ORIGIN+'about.html','sameAs':['https://github.com/xmhuangzhijun-hue'],'description':'求职主方向：FDE（Forward Deployed Engineer）；延伸方向：AI 产品定义与应用开发。','email':'xmhuangzhijun@gmail.com','knowsAbout':['Business systems integration','Data quality','AI application development']}
        data={'@context':'https://schema.org','@type':'WebPage','@id':url+'#page','url':url,'name':title,'description':description,'inLanguage':'zh-CN','author':person}
        if path in {'index.html','about.html'}: data.update({'@type':'ProfilePage','mainEntity':person})
        elif typ=='article': data.update({'@type':'BlogPosting','headline':title,'image':img,'mainEntityOfPage':url,'datePublished':'2026-09-05'})
        extra=f'<meta property="og:site_name" content="黄智军 · FDE 作品集"><meta property="og:locale" content="zh_CN"><meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{escape(title,quote=True)} · 黄智军"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{img}"><meta name="twitter:title" content="{escape(title,quote=True)} · 黄智军"><script type="application/ld+json">{json.dumps(data,ensure_ascii=False).replace("<", chr(92)+"u003c")}</script>'
        if path=='404.html': extra+='<meta name="robots" content="noindex">'
        extra+='<link rel="stylesheet" href="'+PREFIX+'static/discovery.css">'
        html=normalize_links(html.replace('</head>',extra+'</head>'),path)
        p.write_text(html,encoding='utf-8')
        manifest.append({'path':path,'title':title,'description':description,'image':'static/og/'+slug+'.jpg','canonical':url})
    # Demo is a simulated app, not a searchable career article.
    demo=out/'demo/iaa/index.html'
    html=demo.read_text(encoding='utf-8')
    html=re.sub(r'<meta name="robots"[^>]*>|<link rel="canonical"[^>]*>','',html)
    html=html.replace('</head>',f'<meta name="robots" content="noindex,follow"><link rel="canonical" href="{canonical("demo/iaa/index.html")}"></head>')
    demo.write_text(normalize_links(html,'demo/iaa/index.html'),encoding='utf-8')
    urls=[x['canonical'] for x in manifest if x['path']!='404.html']
    (out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(u)+'</loc></url>' for u in sorted(urls))+'</urlset>',encoding='utf-8')
    (out.parent/'content/share-cards.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
