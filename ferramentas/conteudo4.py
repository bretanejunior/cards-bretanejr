# -*- coding: utf-8 -*-
# Lote 4 — pesquisa de nov/2026 (STJ, STF, Banco Central, MDS, EC 103/2019). Conteúdo EDUCATIVO, sem casos do escritório.
from conteudo import HASHTAGS_BASE as H
D = "\n\nConteúdo informativo. Cada caso exige análise individual."

CF5_XXXII = "O Estado promoverá, na forma da lei,<br>a defesa do consumidor."

POSTS4 = [
dict(id="P48", tipo="carrossel", area="Direito Previdenciário", titulo="Aposentadoria em 2027: o que muda em janeiro.",
 sub="A regra dos pontos e a idade mínima sobem de novo na virada do ano.",
 slides=[
  dict(h="Regra dos pontos", txt="A partir de janeiro de 2027, a soma de idade + tempo de contribuição passa a ser 94 pontos para mulheres (com 30 anos de contribuição) e 104 pontos para homens (com 35 anos)."),
  dict(h="Idade mínima progressiva", txt="Em 2027: 60 anos para mulheres e 65 anos para homens, além de 30 e 35 anos de contribuição. Para os homens, essa é a idade final da regra."),
  dict(h="Aposentadoria por idade", txt="Não muda: 62 anos para mulheres e 65 para homens. As regras de pedágio (50% e 100%) também seguem as mesmas condições."),
  dict(h="Antes de pedir", items=["Simule no Meu INSS","Confira o CNIS (vínculos e salários)","Se já cumpriu os requisitos em 2026, o direito está garantido","Compare as regras: a melhor muda o valor"]),
 ],
 ref="EC 103/2019, arts. 15, 16, 17, 18 e 20 · Lei 8.213/91",
 legenda="Vai se aposentar? Em 1º de janeiro de 2027 as regras de transição ficam mais exigentes.\n\nA regra dos pontos sobe para 94 (mulheres) e 104 (homens), e a idade mínima progressiva vai a 60 e 65 anos. Quem completou os requisitos até 31/12/2026 mantém o direito pelas regras de 2026.\n\n➡️ Arraste e veja os números de 2027.\n📌 Salve e envie para quem está perto de se aposentar."+D+"\n\n(Substitui o card P37 a partir de janeiro de 2027.)",
 hashtags="#aposentadoria #inss #aposentadoria2027 #previdenciario #regrasdetransicao "+H,
 reels="GANCHO: “Vai se aposentar? Em janeiro tudo muda.” · MEIO: 94/104 pontos + idade mínima 60/65 + direito adquirido de quem completou em 2026 · FINAL: “Simula no Meu INSS e manda pra quem precisa.”"),

dict(id="P49", tipo="carrossel", area="Golpes e Fraudes", titulo="Golpe do PIX: o que mudou no MED em 2026.",
 sub="O Banco Central reforçou as regras para tentar devolver o dinheiro à vítima.",
 slides=[
  dict(h="Rastreamento do dinheiro", txt="Desde fevereiro de 2026, o MED 2.0 permite seguir o dinheiro mesmo depois que o golpista o transfere para outras contas, aumentando a chance de bloqueio e devolução."),
  dict(h="Prazo de 80 dias", txt="A vítima pode pedir a abertura do MED ao seu banco em até 80 dias da transação. Mas quanto antes, melhor: o dinheiro costuma ser movimentado em minutos."),
  dict(h="Responsabilidade do banco", txt="Bancos respondem por fraudes ligadas à sua atividade (Súmula 479 do STJ). Se o banco foi avisado a tempo e não agiu, pode ter de reparar o prejuízo."),
  dict(h="Faça isso logo", items=["Ligue no canal oficial do banco e peça o MED","Anote o número do protocolo","Registre boletim de ocorrência","Guarde prints, comprovante e dados do recebedor"]),
 ],
 ref="Resolução BCB 1/2020 (Regulamento do Pix) · IN BCB 766/2026 · STJ, Súmula 479",
 legenda="Caiu no golpe do PIX? As regras para recuperar o dinheiro mudaram em 2026.\n\nO MED agora consegue rastrear o dinheiro entre várias contas, e a vítima tem até 80 dias para pedir a devolução. Ainda assim, agir nos primeiros minutos faz toda a diferença.\n\n➡️ Arraste e veja o passo a passo.\n📌 Salve e mande para seus pais e avós."+D,
 hashtags="#golpedopix #pix #med #bancocentral #fraudebancaria "+H,
 reels="GANCHO: “O Banco Central mudou as regras do golpe do PIX.” · MEIO: MED 2.0 rastreia o dinheiro + prazo de 80 dias + Súmula 479 · FINAL: “Salva e manda no grupo da família.”"),

dict(id="P50", tipo="post", area="Direito do Consumidor", titulo="Cobrança indevida: devolução em dobro, mesmo sem má-fé.",
 items=["O STJ fixou em repetitivo: quem paga o que não deve tem direito ao dobro quando a cobrança contraria a boa-fé, mesmo sem intenção da empresa","Se você reclamou e a empresa ignorou ou recusou, isso já reforça o pedido","Só não há dobro em erro justificável, como cláusula depois anulada pela Justiça"],
 ref="STJ, Corte Especial, Tema 929 (REsp 1.963.770/CE) · CDC, art. 42, parágrafo único",
 legenda="Pagou uma cobrança que não devia? A lei garante a devolução em dobro, com correção e juros.\n\nO STJ consolidou, em julgamento repetitivo, que não é preciso provar má-fé da empresa: basta que a cobrança contrarie a boa-fé. E a decisão vale também para cobranças antigas.\n\n📌 Salve e guarde seus comprovantes e protocolos.\n💬 Já pagou algo que não devia? Conta nos comentários."+D,
 hashtags="#devolucaoemdobro #cobrancaindevida #direitodoconsumidor #cdc #stj "+H),

dict(id="P51", tipo="post", area="Motoristas e Entregadores", titulo="Uberização: o STF adiou e a OIT aprovou nova convenção.",
 items=["Em junho de 2026 o STF retirou de pauta o Tema 1291 (vínculo de motoristas e entregadores) e ainda não há nova data","O motivo: a OIT aprovou a Convenção 193, com regras mínimas para quem trabalha por plataformas","A convenção ainda depende de aprovação do Congresso para valer no Brasil"],
 ref="STF, RE 1.446.336 (Tema 1291) · Convenção 193 da OIT (12/06/2026)",
 legenda="Motorista e entregador de aplicativo: a decisão do STF sobre vínculo de emprego ficou para depois.\n\nO julgamento estava marcado para 24 de junho, mas foi retirado de pauta após a aprovação da Convenção 193 da OIT, que trata de remuneração, saúde, previdência e gestão por algoritmo. Até o STF decidir, as decisões continuam variando caso a caso.\n\n🚗🛵 Compartilhe no grupo dos motoristas e entregadores.\n💬 Você acha que deve haver carteira assinada? Comente."+D,
 hashtags="#uberizacao #motoristadeaplicativo #entregador #stf #oit "+H),

dict(id="P52", tipo="post", area="Direito Previdenciário", titulo="BPC: prazo do CadÚnico prorrogado para 2027.",
 items=["Vale para quem recebe ou pediu o BPC e estava no antigo Formulário de Impossibilidade de cadastro","O novo prazo para regularizar o Cadastro Único é 31/12/2027","Os demais beneficiários continuam com a atualização obrigatória a cada 24 meses"],
 ref="IN Conjunta SAGICAD/SNBA nº 2/2026 · Informe Cadastro Único nº 103 (MDS) · Lei 8.742/93",
 legenda="Atenção, famílias de idosos e pessoas com deficiência que recebem o BPC.\n\nO Governo Federal prorrogou até 31 de dezembro de 2027 o prazo para regularizar o Cadastro Único de quem estava no antigo Formulário de Impossibilidade, como pessoas acamadas ou sem representante legal. Quem perde o prazo pode ter o benefício negado ou suspenso.\n\n📌 Salve e procure o CRAS do seu município.\n🔁 Compartilhe com quem cuida de um beneficiário."+D,
 hashtags="#bpc #loas #cadunico #inss #assistenciasocial "+H),

dict(id="P53", tipo="post", area="Direito Previdenciário", titulo="Eletricista tem aposentadoria especial? O STJ vai decidir.",
 items=["O STJ vai definir se a exposição à eletricidade conta como atividade especial após o Decreto 2.172/1997","Enquanto isso, os processos sobre o tema estão suspensos em todo o país","Guarde PPP, laudos (LTCAT) e comprovantes de que o risco era habitual e permanente"],
 ref="STJ, Tema de Relevância 1.475 (REsp 2.267.903/GO) · Lei 8.213/91, arts. 57 e 58",
 legenda="Trabalha ou trabalhou exposto à alta tensão? Esse tema voltou ao STJ.\n\nA Primeira Seção vai decidir, com efeito para todo o país, se o risco de choque elétrico ainda permite contar o tempo como especial. Até lá, os processos sobre o assunto estão suspensos.\n\n⚡ Compartilhe com eletricistas e colegas do setor elétrico.\n📌 Salve e reúna seus documentos desde já."+D,
 hashtags="#aposentadoriaespecial #eletricista #inss #stj #previdenciario "+H),

dict(id="S10", tipo="story", area="Quiz", titulo="Verdadeiro ou falso: para receber em dobro uma cobrança indevida, você precisa provar a má-fé da empresa.",
 enquete=["Verdadeiro","Falso"],
 resposta="FALSO! Basta a cobrança contrariar a boa-fé (STJ, Tema 929).",
 legenda="(Story) Use a figurinha de QUIZ. No story seguinte, revele a resposta e direcione para o post P50.", hashtags=""),

dict(id="P54", tipo="arte", formato="post", area="Frases do Direito", titulo="Constituição: defesa do consumidor (art. 5º, XXXII)",
 pages=[("citacao", (1080, 1350, CF5_XXXII, "CONSTITUIÇÃO FEDERAL", "ART. 5º, XXXII"))],
 legenda="Você sabia que a defesa do consumidor está na Constituição, entre os direitos fundamentais?\n\nFoi desse artigo que nasceu o Código de Defesa do Consumidor, em 1990: a lei que protege você contra cobranças indevidas, produtos com defeito e práticas abusivas.\n\n💬 Qual direito do consumidor você mais usa? Comente."+D,
 hashtags="#constituicao #direitodoconsumidor #cdc #frasesdodireito #cidadania "+H),
]
