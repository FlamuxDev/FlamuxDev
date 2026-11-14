"""Builds the animated brand SVGs in ../assets from the Faraj palette. Run: python3 scripts/build.py"""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
f = lambda n: base64.b64encode((root / 'scripts/fonts' / n).read_bytes()).decode()
FONTS = f"""@font-face{{font-family:U;src:url(data:font/woff;base64,{f('unb.woff')}) format('woff');font-weight:700}}
@font-face{{font-family:G;src:url(data:font/woff;base64,{f('sg.woff')}) format('woff')}}"""
VOID, CREAM, LIME, LINE = '#0F0D0C', '#F7F1E8', '#C8FF00', 'rgba(247,241,232,.14)'
SHARDS = [  # the Faraj F mark (kit/svg/mark), three shards
  (CREAM, 'M48.82 121.19 L53.62 119.42 L145.09 74.83 L207.18 26.00 L141.78 43.38 L53.73 87.40 L51.05 91.98 L48.82 121.19 Z'),
  (CREAM, 'M56.57 131.08 L54.16 228.10 L57.79 230.00 L86.23 200.53 L87.96 153.51 L90.88 149.59 L112.98 136.90 L117.85 101.11 L56.57 131.08 Z'),
  (LIME,  'M121.43 160.24 L123.37 161.16 L190.49 80.08 L183.51 80.54 L128.40 105.24 L125.94 111.99 L121.43 160.24 Z')]

def svg(w, h, css, body, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
<style>{FONTS}
text{{font-family:G,'Space Grotesk',system-ui,sans-serif;fill:{CREAM}}} .u{{font-family:U,'Space Grotesk',system-ui,sans-serif;font-weight:700}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
{css}</style>{body}</svg>'''

def header():
    roles = ['AI agents','SaaS platforms','mobile apps','backends that scale','products people love']
    n, step = len(roles), 2.6
    role_css = ''.join(f'.r{i}{{animation:roll {n*step}s {i*step}s infinite}}' for i in range(n))
    pct = 100 / n
    css = f'''
.bg{{fill:{VOID}}}
.dot{{fill:{CREAM};opacity:.09}}
.s{{opacity:0;transform-box:fill-box;transform-origin:center;animation:in 1.1s cubic-bezier(.2,.8,.2,1) forwards}}
.s0{{--x:-80px;--y:-50px;--r:-25deg}} .s1{{--x:-50px;--y:70px;--r:20deg;animation-delay:.15s}} .s2{{--x:90px;--y:30px;--r:40deg;animation-delay:.3s}}
@keyframes in{{from{{opacity:0;transform:translate(var(--x),var(--y)) rotate(var(--r))}}to{{opacity:1;transform:none}}}}
.mark{{animation:float 6s ease-in-out 1.4s infinite}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}
.ring{{fill:none;stroke:{LINE};stroke-dasharray:4 8;transform-origin:1010px 210px;animation:spin 40s linear infinite}}
.ring2{{fill:none;stroke:{LINE};transform-origin:1010px 210px;animation:spin 70s linear infinite reverse}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.fade{{opacity:0;animation:up .9s cubic-bezier(.2,.8,.2,1) forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:none}}}}
.r{{opacity:0;fill:{LIME}}} {role_css}
@keyframes roll{{0%{{opacity:0;transform:translateY(14px)}}{pct*.12:.1f}%,{pct*.85:.1f}%{{opacity:1;transform:none}}{pct:.1f}%,100%{{opacity:0;transform:translateY(-14px)}}}}
.ping{{fill:{LIME};animation:ping 2s ease-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes ping{{0%{{opacity:.7;transform:scale(1)}}100%{{opacity:0;transform:scale(3.2)}}}}
.tag{{font-size:13px;letter-spacing:.35em;fill:rgba(247,241,232,.55)}}'''
    dots = ''.join(f'<circle class="dot" cx="{x}" cy="{y}" r="1.2"/>' for x in range(20, 1280, 40) for y in range(20, 420, 40))
    shards = ''.join(f'<path class="s s{i}" fill="{c}" d="{d}"/>' for i, (c, d) in enumerate(SHARDS))
    role_txt = ''.join(f'<text class="r r{i} u" x="64" y="282" font-size="34">{r}.</text>' for i, r in enumerate(roles))
    body = f'''<rect class="bg" width="1280" height="420" rx="20"/>{dots}
<circle class="ring2" cx="1010" cy="210" r="175"/><circle class="ring" cx="1010" cy="210" r="150"/>
<g class="mark"><g transform="translate(880 75) scale(1.05)"><g transform="translate(-40 -20)">{shards}</g></g></g>
<g class="fade" style="animation-delay:.2s"><circle class="ping" cx="72" cy="78" r="5"/><circle fill="{LIME}" cx="72" cy="78" r="5"/>
<text x="88" y="83" font-size="15" fill-opacity=".7">Available for new projects · Amman / Riyadh</text></g>
<text class="u fade" x="62" y="168" font-size="62" style="animation-delay:.35s">Abdulrahman Faraj</text>
<text class="fade" x="64" y="218" font-size="24" fill-opacity=".72" style="animation-delay:.5s">Full-stack &amp; AI engineer. I build</text>
{role_txt}
<text class="tag fade" x="64" y="362" style="animation-delay:.8s">BUILD · CREATE · GROW  —  MORE THAN A MOMENT</text>'''
    return svg(1280, 420, css, body, 'Abdulrahman Faraj — Full-stack and AI engineer')

def title(num, word, text):
    css = f'''.t{{font-size:13px;letter-spacing:.35em;fill:rgba(247,241,232,.55)}} .t tspan{{fill:{LIME}}}
.h{{opacity:0;animation:up .8s cubic-bezier(.2,.8,.2,1) .1s forwards}} @keyframes up{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
.l{{stroke:{LIME};stroke-width:2;stroke-dasharray:1200;stroke-dashoffset:1200;animation:draw 1.6s cubic-bezier(.2,.8,.2,1) .2s forwards}} @keyframes draw{{to{{stroke-dashoffset:0}}}}'''
    body = f'''<rect width="1280" height="120" rx="16" fill="{VOID}"/>
<text class="t" x="40" y="44">{num} — <tspan>{word}</tspan></text>
<text class="u h" x="38" y="92" font-size="34">{text}</text>
<line class="l" x1="40" y1="112" x2="1240" y2="112"/>'''
    return svg(1280, 120, css, body, text)

def stats():
    items = [('20+', 'products shipped'), ('6', 'backend languages'), ('4', 'platforms'), ('11', 'live sites &amp; apps')]
    css = '.n{opacity:0;animation:up .8s cubic-bezier(.2,.8,.2,1) forwards} @keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}} .lb{font-size:16px;fill-opacity:.6}'
    cells = ''.join(f'''<g class="n" style="animation-delay:{.15*i:.2f}s"><text class="u" x="{40+i*310}" y="78" font-size="52">{n.replace('+', '')}<tspan fill="{LIME}">{'+' if '+' in n else ''}</tspan></text>
<text class="lb" x="{42+i*310}" y="112">{l}</text></g>''' + (f'<line x1="{20+(i+1)*310}" y1="30" x2="{20+(i+1)*310}" y2="120" stroke="{LINE}"/>' if i < 3 else '') for i, (n, l) in enumerate(items))
    return svg(1280, 150, css, f'<rect width="1280" height="150" rx="16" fill="{VOID}" stroke="{LINE}"/>{cells}', 'Stats')

def marquee():
    words = ['AI AGENTS','LLM · RAG','MCP','NEXT.JS','GO','TYPESCRIPT','REACT NATIVE','POSTGRES','JAVA','.NET','PYTHON','DOCKER','TEMPORAL','AWS','TAURI','ODOO']
    # one text run stretched to an exact width (textLength), so the loop seam is seamless
    sep = f'<tspan fill="{LIME}">  /  </tspan>'
    x = sum(len(w) + 5 for w in words) * 16.5
    row = f'<text class="u" x="0" y="58" font-size="26" textLength="{x}" lengthAdjust="spacing">' + sep.join(words) + sep + '</text>'
    css = f'.m{{animation:mq 40s linear infinite}} @keyframes mq{{to{{transform:translateX(-{x}px)}}}}'
    return svg(1280, 90, css, f'<rect width="1280" height="90" rx="16" fill="#161412"/><g class="m">{row}<g transform="translate({x} 0)">{row}</g></g>', 'Tech stack')

out = root / 'assets'
(out / 'header.svg').write_text(header())
(out / 'stats.svg').write_text(stats())
(out / 'stack.svg').write_text(marquee())
for k, a in {'about': ('01', 'ABOUT', 'More than a moment.'), 'build': ('02', 'CAPABILITIES', 'What I build.'),
             'work': ('03', 'SELECTED WORK', 'Live products I built.'), 'contact': ('04', 'CONTACT', "Let's build something.")}.items():
    (out / f'title-{k}.svg').write_text(title(*a))
print('ok')
