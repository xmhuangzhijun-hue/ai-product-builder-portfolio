"""Render deterministic typographic share cards; requires Pillow and a CJK font."""
from pathlib import Path
import argparse,json
from PIL import Image,ImageDraw,ImageFont

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--font',default='C:/Windows/Fonts/msyh.ttc')
args=parser.parse_args()
for item in json.loads((root/'content/share-cards.json').read_text(encoding='utf-8')):
    im=Image.new('RGB',(1200,630),'#f7f9fc');d=ImageDraw.Draw(im)
    font=lambda size:ImageFont.truetype(args.font,size)
    d.rectangle((64,63,114,69),fill='#2859df')
    d.text((64,97),'黄智军  /  FDE',font=font(27),fill='#2859df')
    title=item['title'];lines=[];line=''
    for ch in title:
        if d.textlength(line+ch,font=font(50))>1060:lines.append(line);line=''
        line+=ch
    if line:lines.append(line)
    for i,line in enumerate(lines[:4]):d.text((60,184+i*72),line,font=font(50),fill='#142136')
    d.line((64,520,1136,520),fill='#dce2eb',width=2)
    d.text((64,550),'业务集成 · AI 应用交付 · 公开实践与贡献',font=font(23),fill='#59677b')
    dest=root/'docs'/item['image'];dest.parent.mkdir(parents=True,exist_ok=True)
    im.save(dest,quality=90,optimize=True)
print('Share cards generated.')
