# -*- coding: utf-8 -*-
import json, os, base64, html, sys, asyncio
sys.path.insert(0, os.path.dirname(__file__))
import glob as _g, importlib as _il
from conteudo import CONTATO
POSTS = []
for _f in sorted(_g.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conteudo*.py')), key=lambda x: (len(x), x)):
    _m = _il.import_module(os.path.basename(_f)[:-3])
    for _n in sorted(k for k in dir(_m) if k.startswith('POSTS')):
        POSTS += getattr(_m, _n)
from icons import for_area, svg as isvg

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
FOTO = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(HERE, "foto.jpg"), "rb").read()).decode()
E = html.escape

MONO = """<svg class="mono" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="3" width="94" height="94" fill="none" stroke="currentColor" stroke-width="2.2"/>
<rect x="9" y="9" width="82" height="82" fill="none" stroke="currentColor" stroke-width="0.8"/>
<text x="50" y="66" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="50" fill="currentColor" letter-spacing="-2">BJ</text>
</svg>"""

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--navy:#0D2033;--navy2:#132D47;--gold:#B8925A;--gold2:#D9BF8F;--ivory:#F5F0E6;--ink:#1A2533;--mute:#5E6B7A}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased}
.pg{position:relative;width:100%%;height:100%%;padding:84px 84px 72px;display:flex;flex-direction:column}
.dark{background:var(--navy);color:var(--ivory)}
.dark::before{content:"";position:absolute;inset:0;background:
 radial-gradient(1200px 700px at 110%% -10%%, rgba(184,146,90,.16), transparent 60%%),
 repeating-linear-gradient(135deg, rgba(255,255,255,.018) 0 2px, transparent 2px 26px);pointer-events:none}
.light{background:var(--ivory);color:var(--ink)}
.frame{position:absolute;inset:34px;border:1.5px solid rgba(184,146,90,.45);pointer-events:none}
.top{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:2}
.brand{display:flex;align-items:center;gap:20px}
.mono{width:74px;height:74px;color:var(--gold)}
.bn{font-family:'Cormorant Garamond';font-weight:600;font-size:30px;letter-spacing:6px;line-height:1}
.bs{white-space:nowrap;font-size:12.5px;letter-spacing:3.2px;margin-top:8px;color:var(--gold);font-weight:500}
.tag{border:1.5px solid var(--gold);color:var(--gold);padding:11px 20px;font-size:15px;letter-spacing:2.2px;text-transform:uppercase;font-weight:600;border-radius:40px;white-space:nowrap}
.light .tag{color:#8C6B3A;border-color:#B8925A}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}
h1{font-family:'Playfair Display';font-weight:600;font-size:90px;line-height:1.08;letter-spacing:-.5px}
h1 .g{color:var(--gold2);font-style:italic}
.sub{font-size:33px;line-height:1.45;font-weight:400;margin-top:40px;color:rgba(245,240,230,.82);max-width:860px}
.rule{width:120px;height:3px;background:var(--gold);margin:44px 0 0}
.bot{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:2;font-size:19px;letter-spacing:2px}
.bot .h{color:var(--gold);font-weight:600}
.swipe{color:var(--gold);font-weight:700;letter-spacing:4px}
.num{font-family:'Playfair Display';font-size:150px;color:var(--gold);line-height:.9;font-weight:500}
h2{font-family:'Playfair Display';font-weight:600;font-size:72px;line-height:1.12;margin-top:26px;color:var(--navy)}
.txt{font-size:41px;line-height:1.55;margin-top:44px;color:#2A3646}
ul.it{list-style:none;margin-top:40px}
ul.it li{font-size:38px;line-height:1.4;padding:24px 0 24px 58px;position:relative;border-bottom:1px solid rgba(13,32,51,.12);color:#2A3646}
ul.it li::before{content:"";position:absolute;left:6px;top:40px;width:18px;height:18px;background:var(--gold);transform:rotate(45deg)}
.dark ul.it li{color:var(--ivory);border-color:rgba(255,255,255,.12)}
.ref{display:flex;align-items:center;gap:16px;font-size:20px;color:#7A6340;letter-spacing:.5px;font-weight:500}
.ref b{white-space:nowrap;flex:none;background:var(--gold);color:#fff;font-size:15px;letter-spacing:2.5px;padding:7px 12px;font-weight:700}
.lfoot{display:flex;justify-content:space-between;font-size:18px;letter-spacing:2px;color:var(--mute);margin-top:34px;padding-top:24px;border-top:1px solid rgba(13,32,51,.15)}
/* post único */
.split{display:flex;flex-direction:column;height:100%%}
.split .up{position:relative;padding:84px 84px 60px;flex:0 0 auto}
.split .up h1{font-size:76px;margin-top:64px}
.split .up{overflow:hidden}.split .up::before{z-index:0}.split .dn{flex:1;background:var(--ivory);color:var(--ink);padding:40px 84px 60px;display:flex;flex-direction:column;position:relative}
.ol{counter-reset:c;list-style:none}
.ol li{counter-increment:c;font-size:35px;line-height:1.42;padding:22px 0 22px 92px;position:relative;border-bottom:1px solid rgba(13,32,51,.12);color:#2A3646}
.ol li::before{content:counter(c,decimal-leading-zero);position:absolute;left:0;top:18px;font-family:'Playfair Display';font-size:46px;color:var(--gold);font-weight:600}
/* CTA */
.cta h1{font-size:76px}
.acts{display:flex;gap:28px;margin-top:60px}
.act{flex:1;border:1.5px solid rgba(217,191,143,.5);padding:34px 20px;text-align:center}
.act .i{font-size:54px;line-height:1}
.act .l{margin-top:16px;font-size:24px;letter-spacing:3px;color:var(--gold2);font-weight:600;text-transform:uppercase}
.contact{margin-top:56px;font-size:28px;line-height:1.8;color:rgba(245,240,230,.9)}
.contact span{color:var(--gold2);font-weight:600}
.disc{margin-top:auto;font-size:19px;color:rgba(245,240,230,.6);line-height:1.5;position:relative;z-index:2}
/* foto */

.dark::after{content:"";position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter><rect width='100%%' height='100%%' filter='url(%%23n)'/></svg>");opacity:.10;mix-blend-mode:overlay;pointer-events:none}
.light{background:radial-gradient(900px 700px at 0% 0%,#FBF8F1,#F2ECE0 70%)}
.light::after{content:"";position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter><rect width='100%%' height='100%%' filter='url(%%23n)'/></svg>");opacity:.06;pointer-events:none}
.wm{position:absolute;pointer-events:none;z-index:1}
.num{background:linear-gradient(160deg,#E6CC96 0%,#B8925A 55%,#8A6834 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.tag{display:flex;align-items:center;gap:10px}
.goldline{height:3px;background:linear-gradient(90deg,transparent,#B8925A 15%,#E6CC96 50%,#B8925A 85%,transparent)}
.frame{border-image:linear-gradient(135deg,rgba(230,204,150,.7),rgba(184,146,90,.2),rgba(230,204,150,.7)) 1}
.rule{background:linear-gradient(90deg,#E6CC96,#B8925A)}
.foto{width:330px;height:330px;border-radius:50%%;border:6px solid var(--gold);background:url(%(foto)s) center 20%%/cover;margin-bottom:56px;box-shadow:0 20px 60px rgba(0,0,0,.35)}
/* story */
.story h1{font-size:84px}
.poll{margin-top:70px;border:2px dashed rgba(217,191,143,.55);height:300px;display:flex;align-items:center;justify-content:center;color:rgba(217,191,143,.75);font-size:24px;letter-spacing:4px;text-transform:uppercase}
.opts{margin-top:60px;display:flex;flex-direction:column;gap:26px}
.opts div{border:2px solid var(--gold);padding:30px 40px;font-size:38px;font-weight:600;color:var(--ivory);border-radius:60px;text-align:center}
.kick{font-size:28px;letter-spacing:6px;color:var(--gold);font-weight:700;text-transform:uppercase;margin-bottom:34px}
"""

def tag(area, light=False):
    c = '#8C6B3A' if light else '#C9A46A'
    return f'<div class="tag">{for_area(area,size=26,w=9,color=c)}{E(area)}</div>'

def brand(dark=True):
    return f"""<div class="brand">{MONO}<div><div class="bn">BRETANE JÚNIOR</div><div class="bs">SOCIEDADE INDIVIDUAL DE ADVOCACIA</div></div></div>"""

def page(body, w=1080, h=1350):
    css = CSS.replace('%%','%').replace('%(w)dpx',f'{w}px').replace('%(h)dpx',f'{h}px').replace('%(foto)s',FOTO)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"

def hl(t):
    # destaca a última palavra-chave após '?' não; usa itálico dourado na última frase curta se houver ':'
    return E(t)

def cover(p, n, total):
    foto = '<div class="foto"></div>' if p.get("foto") else ""
    return page(f"""<div class="pg dark"><div class="frame"></div>
<div class="wm" style="right:-130px;bottom:10px;opacity:{'.10' if p.get('foto') else '.13'}">{isvg('coluna',620,1.6,'#D9BF8F') if p.get('foto') else for_area(p['area'],size=600,w=1.6,color='#D9BF8F')}</div>
<div class="top">{brand()}{tag(p['area'])}</div>
<div class="mid">{foto}<h1>{hl(p['titulo'])}</h1><div class="rule"></div><div class="sub">{E(p.get('sub',''))}</div></div>
<div class="bot"><span>{CONTATO['insta']} · {CONTATO['oab']}</span><span class="swipe">ARRASTE &nbsp;→ &nbsp;1/{total}</span></div></div>""")

def inner(p, s, n, total):
    body = f'<div class="txt">{E(s["txt"])}</div>' if s.get("txt") else ""
    if s.get("items"):
        body += '<ul class="it">' + "".join(f"<li>{E(i)}</li>" for i in s["items"]) + "</ul>"
    ref = f'<div class="ref"><b>BASE LEGAL</b>{E(p["ref"])}</div>' if p.get("ref") else '<div class="ref"></div>'
    return page(f"""<div class="pg light"><div class="frame"></div>
<div class="wm" style="right:40px;top:150px;opacity:.07">{for_area(p['area'],size=380,w=2,color='#0D2033')}</div>
<div class="top">{brand()}{tag(p['area'],True)}</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2;padding-bottom:30px"><div class="num">{n:02d}</div><h2>{E(s['h'])}</h2>{body}</div>
{ref}
<div class="lfoot"><span>{CONTATO['insta']}</span><span>{n}/{total} &nbsp;→</span></div></div>""".replace('class="mono"', 'class="mono" style="color:#B8925A"').replace('<div class="bn">', '<div class="bn" style="color:#0D2033">'))

def cta(p, total):
    return page(f"""<div class="pg dark cta"><div class="frame"></div><div class="wm" style="right:-110px;top:120px;opacity:.07">{isvg('balanca',560,1.6,'#D9BF8F')}</div>
<div class="top">{brand()}<div class="tag">{total}/{total}</div></div>
<div class="mid"><div class="kick">Este conteúdo foi útil?</div><h1>Salve, compartilhe e <span class="g">tire suas dúvidas</span> nos comentários.</h1>
<div class="acts"><div class="act"><div class="i"><svg viewBox="0 0 24 24" width="58" height="58" fill="none" stroke="#D9BF8F" stroke-width="1.6"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg></div><div class="l">Salvar</div></div><div class="act"><div class="i"><svg viewBox="0 0 24 24" width="58" height="58" fill="none" stroke="#D9BF8F" stroke-width="1.6"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg></div><div class="l">Compartilhar</div></div><div class="act"><div class="i"><svg viewBox="0 0 24 24" width="58" height="58" fill="none" stroke="#D9BF8F" stroke-width="1.6"><path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/></svg></div><div class="l">Comentar</div></div></div>
<div class="contact"><span>{CONTATO['insta']}</span> &nbsp;·&nbsp; {CONTATO['site']}<br>Bretane Júnior · {CONTATO['oab']}</div></div>
<div class="disc">Conteúdo de caráter informativo. Cada situação exige análise individual por profissional habilitado.</div></div>""")

def single(p):
    ref = f'<div class="ref" style="margin-top:auto;padding-top:20px"><b>BASE LEGAL</b>{E(p["ref"])}</div>'
    items = '<ul class="ol">' + "".join(f"<li>{E(i)}</li>" for i in p["items"]) + "</ul>"
    return page(f"""<div class="split"><div class="up dark"><div class="wm" style="right:-40px;top:40px;opacity:.15">{for_area(p['area'],size=520,w=1.6,color='#D9BF8F')}</div><div class="top">{brand()}{tag(p['area'])}</div>
<h1 style="position:relative;z-index:2">{E(p['titulo'])}</h1></div>
<div class="goldline"></div><div class="dn">{items}{ref}<div class="lfoot"><span>{CONTATO['insta']} · {CONTATO['oab']}</span><span>SALVE ESTE POST</span></div></div></div>""")

def story(p):
    extra = ""
    if p.get("enquete"):
        extra = '<div class="sub" style="font-size:34px;margin-top:60px;color:#D9BF8F">Vote abaixo ↓</div><div style="height:420px"></div>'
    elif p.get("caixa"):
        extra = '<div class="sub" style="font-size:34px;margin-top:60px;color:#D9BF8F">Envie sua pergunta abaixo ↓</div><div style="height:420px"></div>'
    elif p.get("dica"):
        extra = f'<div class="sub" style="font-size:44px;margin-top:50px">{E(p["dica"])}</div>'
    return page(f"""<div class="pg dark story" style="padding:150px 84px 160px"><div class="frame"></div>
<div class="wm" style="right:-120px;bottom:120px;opacity:.13">{for_area(p['area'],size=760,w=1.4,color='#D9BF8F')}</div>
<div class="top">{brand()}</div>
<div class="mid"><div class="kick">{E(p['area'])}</div><h1>{E(p['titulo'])}</h1>{extra}</div>
<div class="bot"><span>{CONTATO['insta']}</span><span class="h">{CONTATO['oab']}</span></div></div>""", 1080, 1920)

def story_resp(p):
    return page(f"""<div class="pg dark story" style="padding:150px 84px 160px"><div class="frame"></div>
<div class="wm" style="right:-120px;bottom:120px;opacity:.13">{isvg('balanca',760,1.4,'#D9BF8F')}</div>
<div class="top">{brand()}</div>
<div class="mid"><div class="kick">Resposta</div><h1>{E(p['resposta'])}</h1><div class="sub">Quer entender melhor? Veja o post completo no feed.</div></div>
<div class="bot"><span>{CONTATO['insta']}</span><span class="h">{CONTATO['oab']}</span></div></div>""", 1080, 1920)

def jobs():
    for p in POSTS:
        if p["tipo"] == "carrossel":
            total = len(p["slides"]) + 2
            yield p, 1, cover(p, 1, total), (1080, 1350)
            for i, s in enumerate(p["slides"], start=2):
                yield p, i, inner(p, s, i, total), (1080, 1350)
            yield p, total, cta(p, total), (1080, 1350)
        elif p["tipo"] == "post":
            yield p, 1, single(p), (1080, 1350)
        else:
            yield p, 1, story(p), (1080, 1920)
            if p.get("resposta"):
                yield p, 2, story_resp(p), (1080, 1920)

async def main(only=None):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(**({"executable_path": "/usr/bin/google-chrome"} if os.path.exists("/usr/bin/google-chrome") else {}), args=["--no-sandbox"])
        pg = await b.new_page(device_scale_factor=1)
        files = {}
        for p, n, h, (w, hh) in jobs():
            if only and p["id"] not in only: continue
            await pg.set_viewport_size({"width": w, "height": hh})
            await pg.set_content(h)
            await pg.evaluate("document.fonts.ready")
            fn = f"{p['id']}_{n:02d}.png"
            await pg.screenshot(path=os.path.join(OUT, fn))
            files.setdefault(p["id"], []).append(fn)
        await b.close()
    return files

if __name__ == "__main__":
    only = sys.argv[1:] or None
    files = asyncio.run(main(only))
    print(json.dumps(files, indent=0)[:3000])
