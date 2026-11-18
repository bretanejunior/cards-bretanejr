# -*- coding: utf-8 -*-
"""Marca Bretane Júnior: releituras das 3 artes enviadas + logotipo novo."""
import asyncio, os, sys, math, re
OUT = "/home/claude/cards/marca"; os.makedirs(OUT, exist_ok=True)

NOME = "BRETANE JÚNIOR"
SUB = "SOCIEDADE INDIVIDUAL DE ADVOCACIA"
OAB = "OAB/SE 10.203"
NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")

GOLD = """<linearGradient id="{id}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#F1DDAE"/><stop offset=".35" stop-color="#D2AF72"/>
<stop offset=".7" stop-color="#B08548"/><stop offset="1" stop-color="#8C6631"/></linearGradient>"""
SILVER = """<linearGradient id="{id}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#E9ECEF"/><stop offset=".3" stop-color="#A9AFB6"/>
<stop offset=".55" stop-color="#7C838B"/><stop offset=".8" stop-color="#B9BEC4"/><stop offset="1" stop-color="#6A7078"/></linearGradient>"""

# ---------------------------------------------------------------- símbolo novo
def simbolo(size, fill="url(#g1)", cut="#0B1C2E", arch=True, uid="s"):
    """Ligadura B+J: a coluna clássica é a haste comum das duas letras,
    dentro de um arco (pórtico do tribunal)."""
    f = fill.replace("#g1", f"#{uid}g")
    a = ""
    if arch:
        a = (f'<path d="M14,262 V112 A86,86 0 0 1 186,112 V262 Z" fill="none" stroke="{f}" stroke-width="4.5"/>'
             f'<path d="M24,252 V112 A76,76 0 0 1 176,112 V252 Z" fill="none" stroke="{f}" stroke-width="1.4"/>'
             f'<line x1="2" y1="262" x2="198" y2="262" stroke="{f}" stroke-width="4.5"/>')
    flutes = "".join(f'<line x1="{x}" y1="90" x2="{x}" y2="190" style="stroke:{cut}" stroke-width="1.5"/>' for x in (64, 69, 74))
    body = f"""<g transform="translate(100,140) scale(.9) translate(-112,-138)">
<path d="M54,62 L111,40 L168,62 Z" fill="none" stroke="{f}" stroke-width="3.2" stroke-linejoin="miter"/>
<rect x="50" y="64" width="122" height="7" fill="{f}"/>
<path d="M54,74 H90 L85,82 H59 Z" fill="{f}"/>
<circle cx="54" cy="79" r="4.6" fill="none" stroke="{f}" stroke-width="2.4"/>
<circle cx="90" cy="79" r="4.6" fill="none" stroke="{f}" stroke-width="2.4"/>
<rect x="58" y="82" width="22" height="114" fill="{f}"/>
<rect x="53" y="196" width="32" height="6" fill="{f}"/>
{flutes}
<path d="M76,93 H100 A20.5,20.5 0 0 1 100,134 H76" fill="none" stroke="{f}" stroke-width="11"/>
<path d="M76,134 H104 A25,25 0 0 1 104,184 H76" fill="none" stroke="{f}" stroke-width="11"/>
<rect x="148" y="74" width="20" height="132" fill="{f}"/>
<rect x="142" y="74" width="32" height="6" fill="{f}"/>
<path d="M158,205 A29,29 0 0 1 100,205 V198" fill="none" stroke="{f}" stroke-width="20"/>
</g>
"""
    defs = f"<defs>{GOLD.format(id=uid+'g')}{SILVER.format(id=uid+'s')}</defs>"
    return (f'<svg viewBox="0 0 200 270" width="{size*200/270:.0f}" height="{size}" xmlns="http://www.w3.org/2000/svg">'
            f'{defs}{a}{body}</svg>')

# ---------------------------------------------------------------- utilidades
CSS = """<style>*{margin:0;padding:0;box-sizing:border-box}
body{width:WWpx;height:HHpx;overflow:hidden;font-family:Montserrat}
.navy{position:relative;width:100%;height:100%;background:radial-gradient(1500px 1000px at 80% 0%,#1A3756 0%,#0D2033 50%,#071422 100%);color:#F5F0E6;overflow:hidden}
.char{position:relative;width:100%;height:100%;background:radial-gradient(900px 900px at 50% 38%,#24282D 0%,#17191C 60%,#0E0F11 100%);color:#F5F0E6;overflow:hidden}
.light{position:relative;width:100%;height:100%;background:radial-gradient(1600px 1100px at 50% 40%,#FFFFFF 0%,#F2F3F5 60%,#E3E6EA 100%);color:#0D2033;overflow:hidden}
.ivory{position:relative;width:100%;height:100%;background:radial-gradient(1400px 900px at 20% 0%,#FCFAF5,#EFE8DA);color:#0D2033;overflow:hidden}
.tr{position:relative;width:100%;height:100%;background:transparent}
.grain::after{content:"";position:absolute;inset:0;background:url("NOISE");opacity:.10;mix-blend-mode:overlay;pointer-events:none}
.c{display:flex;align-items:center;justify-content:center}
.cin{font-family:Cinzel;font-weight:600;line-height:1}
.mon{font-family:Montserrat}
.gl{height:2px;background:linear-gradient(90deg,transparent,#B8925A 12%,#EBD3A0 50%,#B8925A 88%,transparent)}
.gtxt{background:linear-gradient(180deg,#F1DDAE,#C9A46A 55%,#9C773E);-webkit-background-clip:text;background-clip:text;color:transparent}
</style>"""

def page(w, h, body):
    return ("<!doctype html><html><head><meta charset='utf-8'>" +
            CSS.replace("WW", str(w)).replace("HH", str(h)).replace("NOISE", NOISE) +
            f"</head><body>{body}</body></html>")

# ================================================================ 1. citação (louros + balança)
def laurel():
    out=[]; cx,cy,r=200,190,152
    for side in (-1,1):
        a0,a1 = (100,248) if side==-1 else (80,-68)
        n=15
        pts=[]
        for i in range(n+1):
            a=math.radians(a0+(a1-a0)*i/n); pts.append((cx+r*math.cos(a), cy+r*math.sin(a)))
        out.append('<polyline points="%s" fill="none" stroke="url(#lg)" stroke-width="3" stroke-linecap="round"/>' % " ".join(f"{x:.1f},{y:.1f}" for x,y in pts))
        for i in range(1,n):
            a=math.radians(a0+(a1-a0)*i/n)
            nx,ny=math.cos(a),math.sin(a)
            tx,ty=(-math.sin(a),math.cos(a)) if side==-1 else (math.sin(a),-math.cos(a))
            x,y=cx+r*nx, cy+r*ny
            sc=1.15-0.45*i/n
            for k in (1,-1):
                c,sn=math.cos(math.radians(40)),math.sin(math.radians(40))*k
                dx,dy=tx*c+nx*sn, ty*c+ny*sn
                rot=math.degrees(math.atan2(dx,-dy))
                out.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f}) scale({sc:.2f})"><path d="M0,0 C10,-9 10,-27 0,-40 C-10,-27 -10,-9 0,0 Z" fill="url(#lg)"/></g>')
        a=math.radians(a1); x,y=cx+r*math.cos(a), cy+r*math.sin(a)
        tx,ty=(-math.sin(a),math.cos(a)) if side==-1 else (math.sin(a),-math.cos(a))
        out.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({math.degrees(math.atan2(tx,-ty)):.1f}) scale(.7)"><path d="M0,0 C10,-9 10,-27 0,-40 C-10,-27 -10,-9 0,0 Z" fill="url(#lg)"/></g>')
    return "".join(out)

def louros(size):
    leaves = []
    for side in (-1, 1):
        for i in range(13):
            t = 0.16 + i * 0.062                       # ângulo ao longo do arco
            ang = math.pi / 2 + side * (math.pi * t * 1.25)
            r = 150
            x = 200 + r * math.cos(ang); y = 190 + r * math.sin(ang) * 1.0
            rot = math.degrees(ang) + (90 if side == 1 else -90) + side * 28
            sc = 1 - i * 0.035
            leaves.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f}) scale({sc:.2f})">'
                          f'<path d="M0,0 C9,-10 9,-26 0,-38 C-9,-26 -9,-10 0,0 Z" fill="url(#lg)"/>'
                          f'<path d="M0,-3 V-34" stroke="#17191C" stroke-width=".9" opacity=".55"/></g>')
            # folha externa
            ang2 = ang + side * 0.02
            x2 = 200 + (r + 26) * math.cos(ang2); y2 = 190 + (r + 26) * math.sin(ang2)
            leaves.append(f'<g transform="translate({x2:.1f},{y2:.1f}) rotate({rot + side*55:.1f}) scale({sc*.85:.2f})">'
                          f'<path d="M0,0 C8,-9 8,-23 0,-33 C-8,-23 -8,-9 0,0 Z" fill="url(#lg)"/></g>')
        # ramo
    arcs = ''.join(f'<path d="M{200 + 150*math.cos(math.pi/2 + s*math.pi*.12):.1f},{190 + 150*math.sin(math.pi/2 + s*math.pi*.12):.1f} '
                   f'A150,150 0 0 {1 if s==1 else 0} {200 + 150*math.cos(math.pi/2 + s*math.pi*.98):.1f},{190 + 150*math.sin(math.pi/2 + s*math.pi*.98):.1f}" '
                   f'fill="none" stroke="url(#lg)" stroke-width="3"/>' for s in (-1, 1))
    ribbon = '<path d="M176,344 Q200,330 224,344 L214,362 L200,350 L186,362 Z" fill="url(#lg)"/>'
    # balança com flecha (conceito original)
    bal = """
<g stroke="url(#lg)" fill="none" stroke-linecap="round">
 <line x1="200" y1="92" x2="200" y2="292" stroke-width="5"/>
 <path d="M200,72 L190,96 L200,90 L210,96 Z" fill="url(#lg)" stroke="none"/>
 <path d="M200,290 l-12,-14 M200,290 l12,-14 M200,280 l-12,-14 M200,280 l12,-14" stroke-width="3"/>
 <path d="M126,148 Q200,128 274,148" stroke-width="4.5"/>
 <circle cx="200" cy="136" r="7" fill="url(#lg)" stroke="none"/>
 <line x1="126" y1="148" x2="102" y2="222" stroke-width="1.8"/><line x1="126" y1="148" x2="150" y2="222" stroke-width="1.8"/>
 <line x1="274" y1="148" x2="250" y2="222" stroke-width="1.8"/><line x1="274" y1="148" x2="298" y2="222" stroke-width="1.8"/>
 <path d="M94,222 Q126,252 158,222 Z" fill="url(#lg)" stroke="none"/>
 <path d="M242,222 Q274,252 306,222 Z" fill="url(#lg)" stroke="none"/>
 <circle cx="126" cy="148" r="4" fill="url(#lg)" stroke="none"/><circle cx="274" cy="148" r="4" fill="url(#lg)" stroke="none"/>
 
</g>"""
    return (f'<svg viewBox="0 0 400 380" width="{size*400/380:.0f}" height="{size}" xmlns="http://www.w3.org/2000/svg">'
            f'<defs>{GOLD.format(id="lg").replace('x1="0" y1="0" x2="1" y2="1"','gradientUnits="userSpaceOnUse" x1="60" y1="20" x2="340" y2="370"')}</defs>{laurel()}{bal}</svg>')

def citacao(w, h, q=None, autor='SALVADOR ALLENDE', fonte=''):
    q = q or 'Não basta que todos sejam iguais perante a lei.<br>É preciso que a lei seja igual perante todos.'
    big = h > w
    st = h >= 1900
    if st: q = q.replace('<br>', ' ')
    return page(w, h, f"""<div class="char grain c" style="flex-direction:column;text-align:center">
<div style="position:absolute;inset:34px;border:1.5px solid rgba(201,164,106,.55)"></div>
<div style="position:absolute;inset:44px;border:.8px solid rgba(201,164,106,.25)"></div>
<div style="position:relative;z-index:2" class="c">{louros(560 if st else (470 if big else 400))}</div>
<div class="cin" style="font-size:{84 if st else (70 if big else 62)}px;letter-spacing:.14em;margin-top:{40 if big else 26}px;position:relative;z-index:2">{NOME}</div>
<div class="gl" style="width:560px;margin:24px auto 20px"></div>
<div class="mon" style="font-size:21px;font-weight:500;letter-spacing:.42em;color:#C9A46A;white-space:nowrap;position:relative;z-index:2">{SUB}</div>
<div style="font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:{56 if st else (44 if big else 39)}px;line-height:1.32;color:#EFE7D6;
max-width:860px;margin-top:{70 if big else 44}px;position:relative;z-index:2">“{q}”</div>
<div class="mon" style="font-size:20px;font-weight:600;letter-spacing:.38em;color:#C9A46A;margin-top:26px;position:relative;z-index:2">— {autor}</div>{f'<div class="mon" style="font-size:17px;letter-spacing:.2em;color:rgba(245,240,230,.5);margin-top:12px;position:relative;z-index:2">{fonte}</div>' if fonte else ''}
<div class="mon" style="position:absolute;bottom:{150 if st else 68}px;left:0;right:0;font-size:17px;letter-spacing:.3em;color:rgba(245,240,230,.55)">@BRETANEJR · {OAB}</div>
</div>""")

# ================================================================ 2. escudo + coluna + circuito
def escudo(size, uid="e"):
    traces = []
    pts = [(132, 150, 168, 114), (132, 166, 178, 128), (132, 182, 184, 146), (132, 198, 178, 170)]
    for i, (x0, y0, x1, y1) in enumerate(pts):
        mx = x0 + 14 + i * 4
        traces.append(f'<path d="M{x0},{y0} H{mx} L{x1-8},{y1} H{x1}" fill="none" stroke="url(#{uid}g)" stroke-width="3.2" stroke-linecap="round"/>'
                      f'<circle cx="{x1+3}" cy="{y1}" r="5" fill="#0D2033" stroke="url(#{uid}g)" stroke-width="2.6"/>')
    return f"""<svg viewBox="0 0 240 280" width="{size*240/280:.0f}" height="{size}" xmlns="http://www.w3.org/2000/svg">
<defs>{GOLD.format(id=uid+'g')}{SILVER.format(id=uid+'s')}
<linearGradient id="{uid}n" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1D3B5E"/><stop offset="1" stop-color="#0A1A2B"/></linearGradient>
<filter id="{uid}sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#0D2033" flood-opacity=".28"/></filter></defs>
<g filter="url(#{uid}sh)">
<path d="M120,8 L228,40 V128 C228,196 182,246 120,272 C58,246 12,196 12,128 V40 Z" fill="url(#{uid}s)"/>
<path d="M120,8 L228,40 V128 C228,196 182,246 120,272 C58,246 12,196 12,128 V40 Z" fill="none" stroke="url(#{uid}g)" stroke-width="3"/>
<path d="M120,26 L212,53 V128 C212,186 173,229 120,252 C67,229 28,186 28,128 V53 Z" fill="url(#{uid}n)"/>
</g>

<g fill="url(#{uid}g)">
<rect x="86" y="62" width="68" height="9" rx="1"/>
<path d="M92,71 H148 L141,81 H99 Z"/>
<circle cx="88" cy="77" r="7" fill="none" stroke="url(#{uid}g)" stroke-width="3.4"/>
<circle cx="152" cy="77" r="7" fill="none" stroke="url(#{uid}g)" stroke-width="3.4"/>
<rect x="104" y="81" width="32" height="132"/>
<path d="M96,213 H144 V221 H96 Z"/><path d="M90,221 H150 V229 H90 Z"/>
</g>
<g stroke="#0D2033" stroke-width="2.2">{''.join(f'<line x1="{x}" y1="88" x2="{x}" y2="208"/>' for x in (112,120,128))}</g>
<circle cx="120" cy="44" r="9" fill="url(#{uid}g)"/>
{''.join(traces)}
</svg>"""

def logo_escudo(w=2400, h=1400):
    areas = ["DIREITO PREVIDENCIÁRIO", "DIREITO PÚBLICO", "GESTÃO MUNICIPAL", "SERVIDORES PÚBLICOS", "SEGURANÇA PÚBLICA"]
    sep = '<span style="color:#B8925A;margin:0 12px">|</span>'
    return page(w, h, f"""<div class="light grain c">
<div class="c" style="gap:80px;position:relative;z-index:2">
{escudo(500)}
<div style="width:4px;height:520px;background:linear-gradient(180deg,transparent,#B8925A 15%,#EBD3A0 50%,#B8925A 85%,transparent)"></div>
<div>
<div class="mon" style="font-size:150px;font-weight:700;letter-spacing:.12em;color:#0D2033;line-height:.95">BRETANE</div>
<div class="mon" style="font-size:107px;font-weight:600;letter-spacing:.12em;color:#0D2033;line-height:1.05">JÚNIOR</div>
<div class="mon" style="font-size:38px;font-weight:400;letter-spacing:.5em;color:#6E7680;margin-top:22px;white-space:nowrap">SOCIEDADE INDIVIDUAL</div>
<div class="mon" style="font-size:38px;font-weight:400;letter-spacing:.5em;color:#6E7680;margin-top:8px;white-space:nowrap">DE ADVOCACIA</div>
<div class="mon" style="font-size:21px;font-weight:600;letter-spacing:.05em;color:#3A4A5C;margin-top:40px;white-space:nowrap">{sep.join(areas)}</div>
</div></div></div>""")

# ================================================================ 3. monograma BJ prata
def bj_mono(size, uid="m", bg="#F2F3F5"):
    return f"""<svg viewBox="0 0 330 320" width="{size*330/320:.0f}" height="{size}" xmlns="http://www.w3.org/2000/svg">
<defs>{SILVER.format(id=uid+'s')}{GOLD.format(id=uid+'g')}
<filter id="{uid}f" x="-10%" y="-10%" width="130%" height="130%"><feDropShadow dx="5" dy="7" stdDeviation="6" flood-color="#0D2033" flood-opacity=".25"/></filter></defs>
<g filter="url(#{uid}f)">
<text x="8" y="246" font-family="Montserrat" font-weight="800" font-size="290" fill="url(#{uid}s)" letter-spacing="0">B</text>
<text x="150" y="282" font-family="Montserrat" font-weight="800" font-size="290" fill="url(#{uid}s)" stroke="{bg}" stroke-width="14" paint-order="stroke">J</text>
</g>

</svg>"""

def logo_bj(bg="light", w=2400, h=1400):
    dark = bg == "navy"
    fg = "#F5F0E6" if dark else "#1E2A36"
    sub = "#C9A46A" if dark else "#5F6872"
    return page(w, h, f"""<div class="{bg} grain c">
<div class="c" style="gap:84px;position:relative;z-index:2">
{bj_mono(560, 'm'+bg, '#0D2033' if dark else '#F2F3F5')}
<div style="width:3px;height:560px;background:linear-gradient(180deg,transparent,#B8925A 12%,#EBD3A0 50%,#B8925A 88%,transparent)"></div>
<div>
<div class="mon" style="font-size:178px;font-weight:400;letter-spacing:.14em;color:{fg};line-height:1">BRETANE</div>
<div class="mon" style="font-size:118px;font-weight:500;letter-spacing:.12em;color:{fg};line-height:1.15;margin-top:6px">JÚNIOR</div>
<div class="mon" style="font-size:40px;font-weight:400;letter-spacing:.62em;color:{sub};margin-top:34px;white-space:nowrap">SOCIEDADE INDIVIDUAL</div>
<div class="mon" style="font-size:40px;font-weight:400;letter-spacing:.62em;color:{sub};margin-top:12px;white-space:nowrap">DE ADVOCACIA</div>
</div></div></div>""")

# ================================================================ 4. logotipo novo
def wordmark(fg, scale=1.0, align="left"):
    s = scale
    return f"""<div style="text-align:{align}">
<div class="cin" style="font-size:{int(150*s)}px;letter-spacing:.11em;color:{fg};white-space:nowrap">BRETANE JÚNIOR</div>
<div style="display:flex;align-items:center;gap:{int(26*s)}px;margin-top:{int(34*s)}px;{'justify-content:center' if align=='center' else ''}">
<div style="height:{max(1,int(2*s))}px;width:{int(70*s)}px;background:#B8925A"></div>
<div class="mon" style="font-size:{int(33*s)}px;font-weight:500;letter-spacing:.42em;color:#C9A46A;white-space:nowrap">{SUB}</div>
<div style="height:{max(1,int(2*s))}px;width:{int(70*s)}px;background:#B8925A"></div></div></div>"""

def novo_h(bg="navy"):
    fg = "#F5F0E6" if bg == "navy" else "#0D2033"
    return page(2600, 1000, f"""<div class="{bg} grain c"><div class="c" style="gap:90px;position:relative;z-index:2">
{simbolo(560, cut='#0D2033' if bg=='navy' else '#F4EFE4', uid='h'+bg)}
<div style="width:2px;height:440px;background:linear-gradient(180deg,transparent,#B8925A 15%,#EBD3A0 50%,#B8925A 85%,transparent)"></div>
{wordmark(fg)}</div></div>""")

def novo_v(bg="navy", w=1800, h=1800):
    fg = "#F5F0E6" if bg == "navy" else "#0D2033"
    return page(w, h, f"""<div class="{bg} grain c" style="flex-direction:column">
<div style="position:relative;z-index:2" class="c">{simbolo(720, cut='#0D2033' if bg=='navy' else '#F4EFE4', uid='v'+bg)}</div>
<div style="position:relative;z-index:2;margin-top:70px">{wordmark(fg, .78, 'center')}</div>
<div class="mon" style="position:relative;z-index:2;margin-top:44px;font-size:26px;letter-spacing:.4em;color:{fg};opacity:.65">{OAB}</div></div>""")

def novo_avatar():
    return page(1080, 1080, f"""<div class="navy grain c">
<div style="position:absolute;inset:0;border-radius:50%;box-shadow:inset 0 0 0 10px rgba(201,164,106,.0)"></div>
<div style="position:relative;z-index:2;margin-top:-10px" class="c">{simbolo(700, cut='#0D2033', uid='av')}</div></div>""")

def novo_selo():   # transparente, para aplicar sobre fotos e cards
    return page(1200, 360, f"""<div class="tr c" style="gap:34px">{simbolo(300, cut='#0D2033', arch=True, uid='se')}
<div><div class="cin" style="font-size:72px;letter-spacing:.11em;color:#F5F0E6;white-space:nowrap;text-shadow:0 2px 12px rgba(0,0,0,.35)">BRETANE JÚNIOR</div>
<div class="mon" style="font-size:20px;font-weight:600;letter-spacing:.4em;color:#D9BF8F;margin-top:16px;white-space:nowrap;text-shadow:0 2px 10px rgba(0,0,0,.4)">{SUB}</div></div></div>""")

def apresentacao():
    """Prancha mostrando o logotipo aplicado (perfil, card e story)."""
    import base64
    def b64(p): return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()
    card = "/home/claude/cards/out/P02_01.png"
    card = card if os.path.exists(card) else sorted(f for f in os.listdir("/home/claude/cards/out"))[0]
    return page(2400, 1500, f"""<div class="ivory c" style="flex-direction:column;gap:70px">
<div class="mon" style="font-size:30px;font-weight:600;letter-spacing:.5em;color:#8C6631">APLICAÇÕES DO LOGOTIPO</div>
<div class="c" style="gap:90px;align-items:flex-end">
 <div style="text-align:center"><div style="width:520px;height:520px;border-radius:50%;overflow:hidden;box-shadow:0 30px 70px rgba(13,32,51,.3)">
   <img src="{b64(OUT+'/logo_novo_simbolo_perfil.png')}" style="width:100%"></div>
   <div class="mon" style="margin-top:34px;font-size:24px;letter-spacing:.3em;color:#0D2033">FOTO DE PERFIL</div></div>
 <div style="text-align:center"><div style="position:relative;width:640px;height:800px;box-shadow:0 30px 70px rgba(13,32,51,.3);overflow:hidden">
   <img src="{b64(card)}" style="width:100%;filter:brightness(.97)">
   <div style="position:absolute;left:12px;right:12px;top:12px;height:104px;background:linear-gradient(180deg,#0E2238,#0F2339)"></div>
   <img src="{b64(OUT+'/logo_novo_selo_transparente.png')}" style="position:absolute;left:30px;top:24px;width:290px"></div>
   <div class="mon" style="margin-top:34px;font-size:24px;letter-spacing:.3em;color:#0D2033">ASSINATURA NOS CARDS</div></div>
 <div style="text-align:center"><div style="width:700px;height:270px;box-shadow:0 30px 70px rgba(13,32,51,.3);overflow:hidden">
   <img src="{b64(OUT+'/logo_novo_horizontal_azul.png')}" style="width:100%"></div>
   <div class="mon" style="margin-top:34px;font-size:24px;letter-spacing:.3em;color:#0D2033">ASSINATURA HORIZONTAL</div></div>
</div></div>""")


# ================================================================ cards novos com as artes
CONT = dict(insta="@bretanejr", site="bretanejunioradv.com")
AREAS = ["Direito Previdenciário", "Direito Público e Gestão Municipal", "Servidores Públicos",
         "Segurança Pública", "Consumidor e Bancário", "Família e Sucessões", "Direito Eclesiástico", "Imobiliário e Contratos"]

def _frame(c="rgba(201,164,106,.5)"):
    return f'<div style="position:absolute;inset:34px;border:1.5px solid {c};pointer-events:none"></div>'

def _pag(n, total, light=False):
    col = "#8C6631" if light else "#C9A46A"
    return f'<div class="mon" style="position:absolute;bottom:64px;right:84px;font-size:18px;font-weight:700;letter-spacing:.3em;color:{col}">{"ARRASTE &nbsp;→ &nbsp;" if n < total else ""}{n}/{total}</div>'

def _rod(light=False):
    col = "rgba(13,32,51,.55)" if light else "rgba(245,240,230,.55)"
    return f'<div class="mon" style="position:absolute;bottom:64px;left:84px;font-size:18px;letter-spacing:.2em;color:{col}">{CONT["insta"]} · {OAB}</div>'

def identidade_capa(total=4):
    return page(1080, 1350, f"""<div class="navy grain c" style="flex-direction:column;text-align:center">{_frame()}
<div class="mon" style="font-size:22px;font-weight:600;letter-spacing:.55em;color:#C9A46A;position:relative;z-index:2">NOVA IDENTIDADE</div>
<div style="position:relative;z-index:2;margin:56px 0 50px" class="c">{simbolo(520, cut='#0D2033', uid='ic')}</div>
<div style="position:relative;z-index:2">{wordmark('#F5F0E6', .5, 'center')}</div>
<div style="font-family:'Cormorant Garamond';font-style:italic;font-size:44px;color:#EFE7D6;margin-top:56px;position:relative;z-index:2">Mesmo compromisso. Nova assinatura.</div>
{_rod()}{_pag(1,total)}</div>""")

def identidade_significado(total=4):
    def item(t, d):
        return (f'<div style="display:flex;gap:28px;align-items:flex-start;padding:26px 0;border-bottom:1px solid rgba(13,32,51,.12)">'
                f'<div style="width:16px;height:16px;background:#B8925A;transform:rotate(45deg);margin-top:16px;flex:none"></div>'
                f'<div><div class="cin" style="font-size:36px;letter-spacing:.06em;color:#0D2033">{t}</div>'
                f'<div class="mon" style="font-size:28px;line-height:1.45;color:#3A4656;margin-top:10px">{d}</div></div></div>')
    return page(1080, 1350, f"""<div class="ivory grain" style="padding:110px 96px">{_frame('rgba(184,146,90,.45)')}
<div style="display:flex;align-items:center;gap:50px;position:relative;z-index:2">
{simbolo(330, cut='#F4EFE4', uid='sg')}
<div><div class="mon" style="font-size:20px;font-weight:600;letter-spacing:.45em;color:#8C6631">O SÍMBOLO</div>
<div style="font-family:'Playfair Display';font-weight:600;font-size:64px;line-height:1.1;color:#0D2033;margin-top:18px">O que cada traço representa</div></div></div>
<div style="margin-top:44px;position:relative;z-index:2">
{item('A coluna', 'Solidez, ética e a tradição do Direito sustentando cada orientação.')}
{item('O B e o J unidos', 'O nome por trás de cada atendimento — um só compromisso.')}
{item('O arco e o frontão', 'A porta do tribunal: o lugar onde o direito se realiza.')}
{item('O dourado sobre o azul', 'Seriedade, confiança e respeito a quem nos procura.')}
</div>{_rod(True)}{_pag(2,total,True)}</div>""")

def areas_card(n=None, total=None):
    rows = "".join(f'<div style="display:flex;align-items:center;gap:20px;padding:20px 0;border-bottom:1px solid rgba(13,32,51,.12)">'
                   f'<div style="width:14px;height:14px;background:#B8925A;transform:rotate(45deg);flex:none"></div>'
                   f'<div class="mon" style="font-size:31px;font-weight:500;color:#1E2A36">{a}</div></div>' for a in AREAS)
    pag = _pag(n, total, True) if n else '<div class="mon" style="position:absolute;bottom:64px;right:84px;font-size:18px;font-weight:700;letter-spacing:.3em;color:#8C6631">SALVE ESTE POST</div>'
    return page(1080, 1350, f"""<div class="light grain" style="padding:100px 96px">{_frame('rgba(184,146,90,.45)')}
<div style="display:flex;align-items:center;gap:46px;position:relative;z-index:2">{escudo(300, uid='ar')}
<div><div class="mon" style="font-size:20px;font-weight:600;letter-spacing:.45em;color:#8C6631">BRETANE JÚNIOR</div>
<div style="font-family:'Playfair Display';font-weight:600;font-size:76px;line-height:1.05;color:#0D2033;margin-top:16px">Áreas de atuação</div>
<div class="mon" style="font-size:24px;color:#5F6872;margin-top:18px;letter-spacing:.04em">Tradição jurídica, com atendimento também digital.</div></div></div>
<div style="margin-top:40px;position:relative;z-index:2">{rows}</div>
{_rod(True)}{pag}</div>""")

def boas_vindas():
    items = ["Seus direitos explicados de forma simples", "Novidades dos tribunais, inclusive do TJSE",
             "Respostas às dúvidas enviadas por você", "Alertas sobre golpes e cobranças abusivas"]
    rows = "".join(f'<div style="display:flex;align-items:center;gap:22px;padding:22px 0;border-bottom:1px solid rgba(30,42,54,.12)">'
                   f'<div style="width:14px;height:14px;background:#B8925A;transform:rotate(45deg);flex:none"></div>'
                   f'<div class="mon" style="font-size:32px;color:#1E2A36">{t}</div></div>' for t in items)
    return page(1080, 1350, f"""<div class="light grain" style="padding:100px 96px">{_frame('rgba(124,131,139,.45)')}
<div style="display:flex;align-items:center;gap:40px;position:relative;z-index:2">{bj_mono(250,'bv')}
<div><div class="mon" style="font-size:20px;font-weight:600;letter-spacing:.45em;color:#6E7680">SEJA BEM-VINDO(A)</div>
<div style="font-family:'Playfair Display';font-weight:600;font-size:70px;line-height:1.08;color:#1E2A36;margin-top:16px">Direito explicado para o seu dia a dia</div></div></div>
<div style="width:100%;height:3px;margin:54px 0 20px;background:linear-gradient(90deg,#B8925A,#EBD3A0 40%,transparent)"></div>
<div class="mon" style="font-size:26px;font-weight:600;letter-spacing:.2em;color:#6E7680;position:relative;z-index:2">AQUI VOCÊ ENCONTRA, TODA SEMANA:</div>
<div style="margin-top:14px;position:relative;z-index:2">{rows}</div>
<div class="cin" style="font-size:34px;letter-spacing:.08em;color:#1E2A36;margin-top:54px;position:relative;z-index:2">Ative as notificações e acompanhe.</div>
{_rod(True)}<div class="mon" style="position:absolute;bottom:64px;right:84px;font-size:18px;font-weight:700;letter-spacing:.3em;color:#8C6631">SIGA {CONT['insta'].upper()}</div></div>""")

def identidade_cta(total=4):
    return page(1080, 1350, f"""<div class="navy grain c" style="flex-direction:column;text-align:center">{_frame()}
<div style="position:relative;z-index:2" class="c">{simbolo(300, cut='#0D2033', uid='ct')}</div>
<div style="font-family:'Playfair Display';font-weight:600;font-size:76px;line-height:1.12;margin-top:60px;max-width:860px;position:relative;z-index:2">Acompanhe conteúdos sobre <span style="color:#D9BF8F;font-style:italic">os seus direitos</span>.</div>
<div class="gl" style="width:420px;margin:50px auto"></div>
<div class="mon" style="font-size:30px;line-height:1.8;color:rgba(245,240,230,.9);position:relative;z-index:2"><b style="color:#D9BF8F">{CONT['insta']}</b> &nbsp;·&nbsp; {CONT['site']}<br>Bretane Júnior · {OAB}</div>
<div class="mon" style="font-size:19px;color:rgba(245,240,230,.55);margin-top:60px;max-width:820px;line-height:1.5;position:relative;z-index:2">Conteúdo de caráter informativo. Cada situação exige análise individual por profissional habilitado.</div>
{_pag(total,total)}</div>""")

def story_identidade():
    return page(1080, 1920, f"""<div class="navy grain c" style="flex-direction:column;text-align:center">{_frame()}
<div class="mon" style="font-size:26px;font-weight:600;letter-spacing:.55em;color:#C9A46A;position:relative;z-index:2">NOVA IDENTIDADE</div>
<div style="position:relative;z-index:2;margin:80px 0 70px" class="c">{simbolo(700, cut='#0D2033', uid='st')}</div>
<div style="position:relative;z-index:2">{wordmark('#F5F0E6', .5, 'center')}</div>
<div style="font-family:'Cormorant Garamond';font-style:italic;font-size:52px;color:#EFE7D6;margin-top:80px;position:relative;z-index:2">Conheça o significado no feed ↓</div>
<div class="mon" style="position:absolute;bottom:150px;left:0;right:0;font-size:22px;letter-spacing:.3em;color:rgba(245,240,230,.6)">{CONT['insta'].upper()} · {OAB}</div></div>""")

# ---------------------------------------------------------------- render
def jobs():
    return [
        ("01_citacao_allende_quadrado.png", citacao(1080, 1080), False),
        ("01_citacao_allende_feed.png", citacao(1080, 1350), False),
        ("02_logo_escudo_coluna.png", logo_escudo(), False),
        ("03_logo_monograma_BJ_claro.png", logo_bj("light"), False),
        ("03_logo_monograma_BJ_azul.png", logo_bj("navy"), False),
        ("logo_novo_horizontal_azul.png", novo_h("navy"), False),
        ("logo_novo_horizontal_marfim.png", novo_h("ivory"), False),
        ("logo_novo_vertical_azul.png", novo_v("navy"), False),
        ("logo_novo_vertical_marfim.png", novo_v("ivory"), False),
        ("logo_novo_simbolo_perfil.png", novo_avatar(), False),
        ("logo_novo_selo_transparente.png", novo_selo(), True),
        ("logo_novo_aplicacoes.png", None, False),
    ]

async def main(only):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        p = await b.new_page()
        for fn, html, transp in jobs():
            if only and not any(o in fn for o in only): continue
            if html is None: html = apresentacao()
            w = int(re.search(r'width:(\d+)px', html).group(1)); h = int(re.search(r'height:(\d+)px', html).group(1))
            await p.set_viewport_size({"width": w, "height": h})
            await p.set_content(html); await p.evaluate("document.fonts.ready"); await p.wait_for_timeout(150)
            await p.screenshot(path=f"{OUT}/{fn}", omit_background=transp)
            print("ok", fn)
        await b.close()
    # SVG vetorial do símbolo
    for nm, kw in (("logo_novo_simbolo.svg", {}), ("logo_novo_simbolo_sem_arco.svg", {"arch": False})):
        open(f"{OUT}/{nm}", "w").write(simbolo(540, cut="#0D2033", uid="x", **kw))

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
