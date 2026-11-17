# Ilustrações vetoriais originais (traço dourado) — viewBox 0 0 200 200
G = 'fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

_I = {
"carro": '''<path d="M30 120 L46 78 Q50 68 62 68 H138 Q150 68 154 78 L170 120"/><rect x="22" y="118" width="156" height="36" rx="10"/>
<circle cx="56" cy="156" r="14"/><circle cx="144" cy="156" r="14"/><line x1="60" y1="100" x2="140" y2="100"/><circle cx="44" cy="134" r="5"/><circle cx="156" cy="134" r="5"/>''',
"celular": '''<rect x="60" y="20" width="80" height="160" rx="14"/><line x1="88" y1="34" x2="112" y2="34"/><circle cx="100" cy="162" r="6"/>
<rect x="74" y="60" width="52" height="40" rx="6"/><circle cx="100" cy="80" r="9"/><line x1="74" y1="116" x2="126" y2="116"/><line x1="74" y1="132" x2="110" y2="132"/>''',
"aviao": '''<path d="M100 20 C108 20 110 32 110 44 V82 L170 116 V132 L110 114 V150 L130 166 V178 L100 168 L70 178 V166 L90 150 V114 L30 132 V116 L90 82 V44 C90 32 92 20 100 20 Z"/>''',
"registro": '''<circle cx="100" cy="100" r="74"/><circle cx="100" cy="100" r="62"/><path d="M80 140 V60 H106 C124 60 132 72 132 84 C132 98 122 106 106 106 H80 M104 106 L132 140"/>''',
"moto": '''<circle cx="46" cy="140" r="26"/><circle cx="154" cy="140" r="26"/><path d="M46 140 L82 96 H118 L154 140"/><path d="M118 96 L132 70 H150"/>
<path d="M82 96 L70 78 H50"/><path d="M96 96 L108 124 H130"/>''',
"balanca": '''<circle cx="100" cy="24" r="6"/><line x1="100" y1="30" x2="100" y2="166"/>
<path d="M36 56 Q100 44 164 56"/><circle cx="100" cy="50" r="4"/>
<path d="M42 56 L22 112 M42 56 L62 112"/><path d="M158 56 L138 112 M158 56 L178 112"/>
<path d="M16 112 H68 Q42 140 16 112 Z"/><path d="M132 112 H184 Q158 140 132 112 Z"/>
<path d="M70 176 Q100 158 130 176 Z"/><line x1="58" y1="178" x2="142" y2="178"/>''',
"coluna": '''<path d="M40 28 H160 L150 40 H50 Z"/><path d="M52 40 Q38 46 44 58 Q52 64 58 54"/><path d="M148 40 Q162 46 156 58 Q148 64 142 54"/>
<rect x="58" y="44" width="84" height="10"/>
<line x1="66" y1="56" x2="66" y2="154"/><line x1="80" y1="56" x2="80" y2="154"/><line x1="94" y1="56" x2="94" y2="154"/>
<line x1="106" y1="56" x2="106" y2="154"/><line x1="120" y1="56" x2="120" y2="154"/><line x1="134" y1="56" x2="134" y2="154"/>
<rect x="56" y="154" width="88" height="8"/><rect x="46" y="162" width="108" height="10"/><rect x="36" y="172" width="128" height="8"/>''',
"martelo": '''<g transform="rotate(-38 96 92)"><rect x="54" y="52" width="84" height="36" rx="6"/><rect x="46" y="58" width="10" height="24" rx="2"/>
<rect x="136" y="58" width="10" height="24" rx="2"/><line x1="72" y1="52" x2="72" y2="88"/><line x1="120" y1="52" x2="120" y2="88"/>
<rect x="90" y="88" width="12" height="78" rx="5"/></g><rect x="104" y="158" width="76" height="14" rx="4"/><line x1="100" y1="180" x2="184" y2="180"/>''',
"livro": '''<path d="M100 58 C80 46 50 44 26 50 V152 C50 146 80 148 100 160 C120 148 150 146 174 152 V50 C150 44 120 46 100 58 Z"/>
<line x1="100" y1="58" x2="100" y2="160"/><path d="M40 72 C56 68 74 70 88 76 M40 92 C56 88 74 90 88 96 M40 112 C56 108 74 110 88 116"/>
<path d="M112 76 C126 70 144 68 160 72 M112 96 C126 90 144 88 160 92 M112 116 C126 110 144 108 160 112"/><text x="100" y="40" text-anchor="middle" font-family="Playfair Display" font-size="26" fill="currentColor" stroke="none">§</text>''',
"escudo": '''<path d="M100 22 L162 44 V96 C162 138 134 162 100 178 C66 162 38 138 38 96 V44 Z"/><path d="M100 38 L148 55 V96 C148 128 128 148 100 161 C72 148 52 128 52 96 V55 Z"/>
<path d="M74 100 L94 120 L130 82"/>''',
"casa": '''<path d="M28 98 L100 38 L172 98"/><path d="M48 82 V170 H152 V82"/><rect x="86" y="120" width="28" height="50"/>
<rect x="60" y="100" width="20" height="20"/><rect x="120" y="100" width="20" height="20"/><path d="M134 62 V40 H148 V74"/><line x1="20" y1="170" x2="180" y2="170"/>''',
"banco": '''<path d="M24 70 L100 30 L176 70 Z"/><circle cx="100" cy="56" r="7"/><rect x="30" y="72" width="140" height="10"/>
<line x1="46" y1="86" x2="46" y2="150"/><line x1="72" y1="86" x2="72" y2="150"/><line x1="100" y1="86" x2="100" y2="150"/><line x1="128" y1="86" x2="128" y2="150"/><line x1="154" y1="86" x2="154" y2="150"/>
<rect x="30" y="152" width="140" height="10"/><rect x="20" y="164" width="160" height="10"/>''',
"documento": '''<path d="M54 24 H126 L154 52 V176 H54 Z"/><path d="M126 24 V52 H154"/>
<line x1="72" y1="72" x2="136" y2="72"/><line x1="72" y1="90" x2="136" y2="90"/><line x1="72" y1="108" x2="136" y2="108"/><line x1="72" y1="126" x2="112" y2="126"/>
<path d="M74 156 C84 140 92 166 102 150 C110 138 114 160 136 150"/>''',
"familia": '''<circle cx="64" cy="58" r="16"/><circle cx="136" cy="58" r="16"/><circle cx="100" cy="100" r="12"/>
<path d="M34 170 V118 C34 96 48 84 64 84 C80 84 94 96 94 118"/><path d="M106 118 C106 96 120 84 136 84 C152 84 166 96 166 118 V170"/>
<path d="M78 170 V140 C78 126 88 118 100 118 C112 118 122 126 122 140 V170"/><line x1="26" y1="172" x2="174" y2="172"/>''',
"igreja": '''<line x1="100" y1="16" x2="100" y2="46"/><line x1="90" y1="26" x2="110" y2="26"/><path d="M76 78 L100 46 L124 78"/>
<path d="M80 78 V172 H120 V78"/><path d="M40 110 L80 86 M160 110 L120 86"/><path d="M48 104 V172 H80 M152 104 V172 H120"/>
<path d="M92 172 V142 Q100 130 108 142 V172"/><circle cx="100" cy="102" r="9"/><line x1="30" y1="174" x2="170" y2="174"/>''',
"coracao": '''<path d="M100 170 C40 128 22 98 26 70 C30 42 60 30 80 42 C90 48 96 56 100 64 C104 56 110 48 120 42 C140 30 170 42 174 70 C178 98 160 128 100 170 Z"/>
<path d="M40 104 H74 L84 82 L98 126 L110 94 L118 104 H160"/>''',
"ampulheta": '''<line x1="54" y1="24" x2="146" y2="24"/><line x1="54" y1="176" x2="146" y2="176"/>
<path d="M64 24 C64 70 100 82 100 100 C100 118 64 130 64 176"/><path d="M136 24 C136 70 100 82 100 100 C100 118 136 130 136 176"/>
<path d="M80 160 Q100 140 120 160 Z"/><line x1="100" y1="112" x2="100" y2="146"/><path d="M80 52 H120"/>''',
"carrinho": '''<path d="M18 40 H44 L64 128 H154 L172 64 H52"/><circle cx="76" cy="156" r="12"/><circle cx="144" cy="156" r="12"/>
<line x1="82" y1="84" x2="160" y2="84"/><line x1="88" y1="106" x2="154" y2="106"/>''',
"aperto": '''<path d="M20 92 L56 62 L88 74 L116 64 L180 92"/><path d="M56 62 L40 120 L74 150 Q86 160 98 150 L132 124"/>
<path d="M88 74 L70 100 Q80 110 96 98 L112 88 L152 120 L140 132"/><path d="M84 138 L100 154 M100 126 L118 142 M114 116 L130 132"/>''',
"pergunta": '''<circle cx="100" cy="100" r="74"/><path d="M76 78 C76 60 90 50 104 50 C120 50 130 62 130 76 C130 98 102 98 102 122"/><circle cx="102" cy="146" r="5" fill="currentColor"/>''',
"lampada": '''<path d="M72 120 C56 106 50 90 50 76 C50 46 74 26 100 26 C126 26 150 46 150 76 C150 90 144 106 128 120 V140 H72 Z"/>
<line x1="76" y1="154" x2="124" y2="154"/><line x1="82" y1="168" x2="118" y2="168"/><path d="M88 120 V96 L100 106 L112 96 V120"/>''',
}

AREA_ICON = {
 "Institucional": "balanca", "Direito do Consumidor": "carrinho", "Direito Bancário": "banco",
 "Direito Previdenciário": "ampulheta", "Direito de Família": "familia", "Servidor Público e Concursos": "coluna",
 "Direito à Saúde": "coracao", "Sucessões": "documento", "Direito Eclesiástico": "igreja",
 "Direito Imobiliário": "casa", "Associações e Cooperativas": "aperto", "Direito Administrativo": "coluna",
 "Enquete": "pergunta", "Motoristas e Entregadores": "carro", "Direito Digital": "celular", "Golpes e Fraudes": "escudo", "Propriedade Intelectual": "registro", "Direito do Passageiro": "aviao", "Direito do Trabalho": "ampulheta", "Locação de Veículos": "moto", "Superendividamento": "banco", "Caixa de perguntas": "pergunta", "Quiz": "balanca", "Dica rápida": "lampada",
}

def svg(name, size=200, w=3, color="currentColor", style=""):
    return (f'<svg viewBox="0 0 200 200" width="{size}" height="{size}" style="color:{color};{style}" xmlns="http://www.w3.org/2000/svg">'
            f'<g {G.format(w=w)}>{_I[name]}</g></svg>')

def for_area(area, **kw):
    return svg(AREA_ICON.get(area, "balanca"), **kw)
