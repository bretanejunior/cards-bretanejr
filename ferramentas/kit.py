# -*- coding: utf-8 -*-
import asyncio, base64, os, re
from icons import svg as isvg
OUT = "/home/claude/cards/kit"; os.makedirs(OUT, exist_ok=True)
FOTO = "data:image/jpeg;base64," + base64.b64encode(open("/home/claude/cards/foto_hd.jpg","rb").read()).decode()
NOISE = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"

from marca import simbolo
def mono(size, uid="g"):
    return simbolo(int(size*1.15), cut="#0D2033", uid=uid)

BASE = """<style>*{margin:0;padding:0;box-sizing:border-box}body{width:%dpx;height:%dpx;overflow:hidden;font-family:Montserrat}
.navy{position:relative;width:100%%;height:100%%;background:radial-gradient(1400px 900px at 85%% 0%%,#1B3A5C 0%%,#0D2033 55%%,#081624 100%%);color:#F5F0E6;overflow:hidden}
.navy::after{content:"";position:absolute;inset:0;background:url("NOISE");opacity:.12;mix-blend-mode:overlay}
.ivory{position:relative;width:100%%;height:100%%;background:radial-gradient(1200px 800px at 0%% 0%%,#FBF8F1,#EFE8DA);color:#0D2033;overflow:hidden}
.wm{position:absolute;pointer-events:none}
.bn{font-family:Cinzel;font-weight:600;letter-spacing:.12em;line-height:1}
.bs{font-weight:500;letter-spacing:.32em;color:#C9A46A;white-space:nowrap}
.gl{height:2px;background:linear-gradient(90deg,transparent,#B8925A 12%%,#EBD3A0 50%%,#B8925A 88%%,transparent)}
.c{display:flex;align-items:center;justify-content:center}
</style>""".replace("NOISE", NOISE.replace('%','%%'))

def page(w, h, body):
    return "<!doctype html><html><head><meta charset='utf-8'>" + (BASE % (w, h)) + f"</head><body>{body}</body></html>"

def logo_h(bg="navy", fg="#F5F0E6"):
    return page(2400, 800, f"""<div class="{bg} c"><div class="c" style="gap:70px;position:relative;z-index:2">{mono(280,'a')}
<div style="border-left:2px solid #B8925A;padding-left:70px"><div class="bn" style="font-size:128px;color:{fg}">BRETANE JÚNIOR</div>
<div class="gl" style="margin:30px 0 26px"></div><div class="bs" style="font-size:34px">SOCIEDADE INDIVIDUAL DE ADVOCACIA</div></div></div></div>""")

def logo_v():
    return page(1600, 1600, f"""<div class="navy c" style="flex-direction:column;gap:46px;text-align:center">
<div class="wm" style="left:50%;top:50%;transform:translate(-50%,-52%);opacity:.06">{isvg('balanca',1300,1.2,'#D9BF8F')}</div>
<div style="position:relative;z-index:2" class="c">{mono(330,'b')}</div>
<div class="bn" style="font-size:112px;position:relative;z-index:2">BRETANE JÚNIOR</div>
<div class="gl" style="width:760px;position:relative;z-index:2"></div>
<div class="bs" style="font-size:31px;position:relative;z-index:2">SOCIEDADE INDIVIDUAL DE ADVOCACIA</div>
<div style="font-size:26px;letter-spacing:.3em;opacity:.7;position:relative;z-index:2">OAB/SE 10.203</div></div>""")

def avatar_mono():
    return page(1080, 1080, f"""<div class="navy c"><div style="position:relative;z-index:2" class="c">{mono(600,'c')}</div></div>""")

def avatar_foto():
    return page(1080, 1080, f"""<div class="navy c">
<div style="position:relative;z-index:2;width:1080px;height:1080px;border-radius:50%;background:url({FOTO}) center 22%/cover"></div>
<div style="position:absolute;inset:0;z-index:3;border-radius:50%;box-shadow:inset 0 0 0 14px rgba(201,164,106,.95), inset 0 0 0 20px rgba(13,32,51,.6)"></div></div>""")

def capa(w, h, foto=True, scale=1.0):
    s = scale
    ph = (f'<div style="position:relative;z-index:2;width:{int(330*s)}px;height:{int(330*s)}px;border-radius:50%;border:{int(6*s)}px solid #C9A46A;'
          f'background:url({FOTO}) center 25%/cover;box-shadow:0 20px 60px rgba(0,0,0,.45);flex:none"></div>') if foto else ""
    areas = "Consumidor e Bancário · Previdenciário · Família e Sucessões · Servidor Público · Direito Eclesiástico · Imobiliário"
    return page(w, h, f"""<div class="navy c">
<div class="wm" style="left:{int(-60*s)}px;bottom:{int(-40*s)}px;opacity:.10">{isvg('coluna',int(560*s),1.4,'#D9BF8F')}</div>
<div class="wm" style="right:{int(-50*s)}px;top:{int(-30*s)}px;opacity:.09">{isvg('balanca',int(520*s),1.4,'#D9BF8F')}</div>
<div class="c" style="gap:{int(60*s)}px;position:relative;z-index:2">{ph}
<div><div style="display:flex;align-items:center;gap:{int(28*s)}px">{mono(int(120*s),'d')}<div><div class="bn" style="font-size:{int(84*s)}px">BRETANE JÚNIOR</div>
<div class="bs" style="font-size:{int(21*s)}px;margin-top:{int(14*s)}px">SOCIEDADE INDIVIDUAL DE ADVOCACIA</div></div></div>
<div class="gl" style="margin:{int(30*s)}px 0 {int(24*s)}px"></div>
<div style="font-size:{int(21*s)}px;letter-spacing:.06em;opacity:.85;max-width:{int(900*s)}px;line-height:1.6">{areas}</div>
<div style="font-size:{int(20*s)}px;letter-spacing:.2em;color:#C9A46A;margin-top:{int(18*s)}px">OAB/SE 10.203 · @bretanejr · bretanejunioradv.com</div></div></div></div>""")

DESTAQUES = [("Quem sou","balanca"),("Consumidor","carrinho"),("INSS","ampulheta"),("Família","familia"),
             ("Igrejas","igreja"),("Concursos","coluna"),("Dúvidas","pergunta"),("Contratos","documento")]
def destaque(nome, ic):
    return page(1080, 1920, f"""<div class="navy c" style="flex-direction:column;gap:60px">
<div class="c" style="position:relative;z-index:2;width:560px;height:560px;border-radius:50%;border:3px solid #C9A46A;box-shadow:inset 0 0 0 14px rgba(13,32,51,1), inset 0 0 0 15px rgba(201,164,106,.5)">{isvg(ic,300,4,'#D9BF8F')}</div>
<div class="bn" style="font-size:64px;position:relative;z-index:2">{nome.upper()}</div></div>""")

def fundo_story():
    return page(1080, 1920, f"""<div class="navy" style="padding:150px 84px">
<div class="wm" style="right:-160px;bottom:160px;opacity:.08">{isvg('balanca',820,1.3,'#D9BF8F')}</div>
<div style="display:flex;align-items:center;gap:22px;position:relative;z-index:2">{mono(84,'e')}<div><div class="bn" style="font-size:34px">BRETANE JÚNIOR</div>
<div class="bs" style="font-size:14px;margin-top:8px">SOCIEDADE INDIVIDUAL DE ADVOCACIA</div></div></div>
<div style="position:absolute;left:84px;right:84px;bottom:150px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.12em;z-index:2"><span>@bretanejr</span><span style="color:#C9A46A">OAB/SE 10.203</span></div></div>""")

JOBS = [("logo_horizontal_azul.png", logo_h()), ("logo_horizontal_claro.png", logo_h("ivory", "#0D2033")),
        ("logo_vertical_azul.png", logo_v()), ("foto_perfil_monograma.png", avatar_mono()),
        ("foto_perfil_retrato.png", avatar_foto()), ("capa_facebook_1640x624.png", capa(1640, 624, True, .78)),
        ("capa_linkedin_1584x396.png", capa(1584, 396, False, .62)), ("fundo_story_bastidores.png", fundo_story())]
JOBS += [(f"destaque_{i+1:02d}_{n.lower().replace('í','i').replace(' ','_')}.png", destaque(n, ic)) for i, (n, ic) in enumerate(DESTAQUES)]

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"]); pg = await b.new_page()
        for fn, h in JOBS:
            w = int(re.search(r'width:(\d+)px', h).group(1)); hh = int(re.search(r'height:(\d+)px', h).group(1))
            await pg.set_viewport_size({"width": w, "height": hh}); await pg.set_content(h); await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=os.path.join(OUT, fn))
        await b.close()
asyncio.run(main()); print(len(JOBS))
