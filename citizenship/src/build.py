"""美国入籍助手 隐私政策 / 支持页：从 content.json（简中、英文）和 content-hant.json（繁中，OpenCC cn→tw 转后人工改过）生成静态页。
用法：python3 -I src/build.py <输出目录>   → 写 index.html、privacy.html、support.html。
发布位置：pulsational/pulsational.github.io 的 citizenship/（UP5，TroiBot 1570352373572833340）。
页面不引用任何外部资源（没有字体、脚本、统计），只有正文里写到的链接。"""
import html
import json
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else sys.exit('用法：python3 -I build.py <输出目录>')
C = json.loads((SRC / 'content.json').read_text(encoding='utf-8'))
H = json.loads((SRC / 'content-hant.json').read_text(encoding='utf-8'))

LANGS = [('zh-Hans', '简体中文'), ('zh-Hant', '繁體中文'), ('en', 'English')]

CSS = """
:root { --bg:#fbf8f2; --fg:#1f2a37; --muted:#5b6573; --accent:#1d4e89; --rule:#e3dccd; }
@media (prefers-color-scheme: dark) { :root { --bg:#141a22; --fg:#e8e4dc; --muted:#a7afba; --accent:#8db8ec; --rule:#2c3644; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font: 18px/1.7 -apple-system, "PingFang SC", "PingFang TC", "Helvetica Neue", Arial, sans-serif; }
main { max-width: 42rem; margin: 0 auto; padding: 1.5rem 1rem 4rem; }
nav.langs { display:flex; gap:1rem; flex-wrap:wrap; padding:.75rem 0 1rem; border-bottom:1px solid var(--rule); }
nav.langs a, a { color: var(--accent); }
section.lang { padding-top: 1.5rem; border-bottom: 1px solid var(--rule); padding-bottom: 1.5rem; }
h1 { font-size: 1.6rem; line-height: 1.3; margin: .25rem 0 1rem; }
h2 { font-size: 1.15rem; margin: 1.6rem 0 .4rem; }
p { margin: .4rem 0; }
footer { color: var(--muted); font-size: .9rem; padding-top: 1.5rem; }
"""


def para(text: str, eff: str, contact: str) -> str:
    t = html.escape(text.replace('{effective}', eff).replace('{contact}', contact))
    t = re.sub(r'(https?://[^\s，。）)]+)', r'<a href="\1">\1</a>', t)
    t = re.sub(r'(?<![/\w])(privacy\.html)', r'<a href="\1">\1</a>', t)
    t = re.sub(r'([\w.+-]+@[\w-]+\.[\w.]+)', r'<a href="mailto:\1">\1</a>', t)
    return f'<p>{t}</p>'


def section(lang: str, doc: dict, eff: str, contact: str) -> str:
    out = [f'<section class="lang" id="{lang}" lang="{lang}">', f'<h1>{html.escape(doc["title"])}</h1>']
    for head, paras in doc['sections']:
        out.append(f'<h2>{html.escape(head)}</h2>')
        out.extend(para(p, eff, contact) for p in paras)
    out.append('</section>')
    return '\n'.join(out)


def page(name: str, title: str, body: str) -> None:
    nav = ' '.join(f'<a href="#{code}" lang="{code}">{label}</a>' for code, label in LANGS)
    doc = f"""<!doctype html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<nav class="langs">{nav}</nav>
{body}
<footer>© 2026 Fangyi Wang</footer>
</main>
</body>
</html>
"""
    (OUT / name).write_text(doc, encoding='utf-8')


for key, fname in [('privacy', 'privacy.html'), ('support', 'support.html')]:
    parts = [
        section('zh-Hans', C[key]['zh'], C['effective']['zh'], C['contact']['zh']),
        section('zh-Hant', H[key], H['effective'], H['contact']),
        section('en', C[key]['en'], C['effective']['en'], C['contact']['en']),
    ]
    page(fname, f"{C[key]['zh']['title']} · {C[key]['en']['title']}", '\n'.join(parts))

links = """<section class="lang"><h1>美国入籍助手 · 美國入籍助手 · Citizenship Helper</h1>
<p><a href="privacy.html">隐私政策 · 隱私政策 · Privacy Policy</a></p>
<p><a href="support.html">帮助与支持 · 幫助與支援 · Help &amp; Support</a></p></section>"""
page('index.html', 'Citizenship Helper', links)
print(f'wrote index.html, privacy.html, support.html → {OUT}')
