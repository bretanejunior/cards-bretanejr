# -*- coding: utf-8 -*-
# Lote 3 — artes da marca (nova identidade, citações, áreas de atuação, boas-vindas).
# tipo "arte": cada página é ("função do marca.py", (argumentos)).
from conteudo import HASHTAGS_BASE as H
D = "\n\nConteúdo informativo. Cada caso exige análise individual."

ALLENDE = "Não basta que todos sejam iguais perante a lei.<br>É preciso que a lei seja igual perante todos."
RUI = "Justiça atrasada não é justiça,<br>senão injustiça qualificada e manifesta."
ULPIANO = "Justiça é a vontade constante e perpétua<br>de dar a cada um o que é seu."
CF5 = "Todos são iguais perante a lei,<br>sem distinção de qualquer natureza."

POSTS3 = [
dict(id="P41", tipo="arte", formato="post", area="Frases do Direito", titulo="Frase: igualdade perante a lei (Salvador Allende)",
 pages=[("citacao", (1080, 1350, ALLENDE, "SALVADOR ALLENDE"))],
 legenda="Igualdade não é só estar escrita na lei. É a lei valer do mesmo jeito para todos: para quem tem muito e para quem tem pouco.\n\nVocê concorda? Comente com um ⚖️ se esta frase faz sentido para você.",
 hashtags="#frasesdodireito #igualdade #justica #advocacia " + H),

dict(id="P42", tipo="arte", formato="carrossel", area="Institucional", titulo="Nova identidade: conheça o símbolo do escritório",
 pages=[("identidade_capa", (4,)), ("identidade_significado", (4,)), ("areas_card", (3, 4)), ("identidade_cta", (4,))],
 legenda="Uma nova assinatura para o mesmo compromisso. ⚖️\n\nA partir de hoje, o escritório Bretane Júnior · Sociedade Individual de Advocacia passa a usar uma nova identidade visual.\n\nA coluna representa a solidez e a ética do Direito. O B e o J unidos, o nome por trás de cada orientação. O arco, a porta do tribunal, onde o direito se realiza.\n\nArraste para conhecer cada detalhe e as áreas de atuação. 👉\n\nO que achou da nova marca? Conta aqui nos comentários!",
 hashtags="#novaidentidade #advocacia #advogado #escritoriodeadvocacia #oab " + H),

dict(id="P43", tipo="arte", formato="post", area="Institucional", titulo="Áreas de atuação",
 pages=[("areas_card", ())],
 legenda="Você sabe em quais áreas este perfil traz conteúdo e orientação jurídica?\n\n⚖️ Direito Previdenciário\n🏛️ Direito Público e Gestão Municipal\n👮 Servidores Públicos e Segurança Pública\n🛒 Consumidor e Bancário\n👨‍👩‍👧 Família e Sucessões\n⛪ Direito Eclesiástico\n🏠 Imobiliário e Contratos\n\nSalve este post e compartilhe com quem precisa conhecer seus direitos." + D,
 hashtags="#areasdeatuacao #advogado #previdenciario #direitopublico #servidorpublico " + H),

dict(id="P44", tipo="arte", formato="post", area="Institucional", titulo="Boas-vindas: o que você encontra neste perfil",
 pages=[("boas_vindas", ())],
 legenda="Seja bem-vindo(a)! 👋\n\nAqui o Direito é explicado de forma simples, para você entender e defender os seus direitos no dia a dia.\n\nToda semana tem conteúdo novo sobre direitos do consumidor, INSS, família, servidores públicos, golpes e muito mais, inclusive com as novidades dos tribunais, como o TJSE.\n\nAtive as notificações e mande sua dúvida nos comentários: ela pode virar o próximo post.",
 hashtags="#bemvindo #direitoparatodos #advocacia #seusdireitos " + H),

dict(id="P45", tipo="arte", formato="post", area="Frases do Direito", titulo="Frase: justiça atrasada (Rui Barbosa)",
 pages=[("citacao", (1080, 1350, RUI, "RUI BARBOSA", "ORAÇÃO AOS MOÇOS"))],
 legenda="Mais de cem anos depois, a frase de Rui Barbosa continua atual.\n\nA Constituição garante a todos a razoável duração do processo (art. 5º, LXXVIII). Quando a demora é excessiva, existem caminhos para pedir prioridade e celeridade, como a tramitação prioritária para idosos e pessoas com doença grave.\n\nVocê já esperou anos por uma decisão? Conte nos comentários.",
 hashtags="#ruibarbosa #frasesdodireito #justica #processo " + H),

dict(id="P46", tipo="arte", formato="post", area="Frases do Direito", titulo="Frase: dar a cada um o que é seu (Ulpiano)",
 pages=[("citacao", (1080, 1350, ULPIANO, "ULPIANO", "JURISCONSULTO ROMANO · DIGESTO"))],
 legenda="Uma das definições de justiça mais antigas do mundo, escrita pelo jurista romano Ulpiano há quase 1.800 anos.\n\nE continua sendo a base de tudo: garantir que cada pessoa receba aquilo que é seu por direito, seja um benefício, uma indenização ou um contrato cumprido.\n\nMarque alguém que precisa ler isto hoje.",
 hashtags="#ulpiano #direitoromano #frasesdodireito #justica " + H),

dict(id="P47", tipo="arte", formato="post", area="Frases do Direito", titulo="Constituição: todos são iguais perante a lei (art. 5º)",
 pages=[("citacao", (1080, 1350, CF5, "CONSTITUIÇÃO FEDERAL", "ART. 5º, CAPUT"))],
 legenda="É o artigo mais conhecido da Constituição, e o mais importante para o cidadão.\n\nO art. 5º garante igualdade, vida, liberdade, segurança e propriedade, e ainda lista dezenas de direitos fundamentais, como o acesso à Justiça e a ampla defesa.\n\nVocê já leu o art. 5º inteiro? Comente “sim” ou “não”.",
 hashtags="#constituicao #artigo5 #direitosfundamentais #cidadania " + H),

dict(id="S07", tipo="arte", formato="story", area="Institucional", titulo="Story: nova identidade",
 pages=[("story_identidade", ())],
 legenda="Story de lançamento da nova marca. Use o adesivo “Link” ou “Ver post” apontando para o carrossel P42.",
 hashtags=""),

dict(id="S08", tipo="arte", formato="story", area="Frases do Direito", titulo="Story: frase de Salvador Allende",
 pages=[("citacao", (1080, 1920, ALLENDE, "SALVADOR ALLENDE"))],
 legenda="Story com a frase. Sugestão: adesivo de enquete “Concorda?” — Sim / Não.",
 hashtags=""),

dict(id="S09", tipo="arte", formato="story", area="Frases do Direito", titulo="Story: frase de Rui Barbosa",
 pages=[("citacao", (1080, 1920, RUI, "RUI BARBOSA", "ORAÇÃO AOS MOÇOS"))],
 legenda="Story com a frase. Sugestão: caixa de perguntas “Seu processo está demorando? Me conte.”",
 hashtags=""),
]
