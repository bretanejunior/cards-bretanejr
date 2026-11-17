# -*- coding: utf-8 -*-
# Lote 2 — pesquisa de jurisprudência (nov/2026). Conteúdo EDUCATIVO, sem casos do escritório.
from conteudo import HASHTAGS_BASE as H
D = "\n\nConteúdo informativo. Cada caso exige análise individual."

POSTS2 = [
dict(id="P25", tipo="carrossel", area="Motoristas e Entregadores", titulo="Motorista ou entregador bloqueado no aplicativo?",
 sub="A plataforma pode suspender, mas precisa explicar e permitir defesa.",
 slides=[
  dict(h="O que decidiu o STJ", txt="A plataforma pode suspender imediatamente o perfil diante de ato grave, mas deve informar o motivo e garantir ao motorista a possibilidade de se defender e pedir a revisão (REsp 2.135.783)."),
  dict(h="Bloqueio sem explicação", txt="Tribunais de vários estados têm determinado a reativação da conta — e, em alguns casos, indenização por lucros cessantes — quando o descredenciamento ocorre sem motivo informado e sem chance de defesa."),
  dict(h="Mas atenção", txt="Quando a empresa comprova a infração (fraude no GPS, corridas por fora, denúncias graves) e oferece defesa, a Justiça costuma manter o bloqueio."),
  dict(h="O que guardar", items=["Print da notificação de bloqueio","Histórico de avaliações e corridas","Pedido de revisão feito no app","Comprovantes dos ganhos mensais"]),
 ],
 ref="STJ, REsp 2.135.783 · Código Civil, arts. 187 e 422",
 legenda="Ficou sem trabalhar porque o aplicativo bloqueou sua conta “do nada”?\n\nO STJ entende que a plataforma pode suspender o perfil em caso de ato grave, mas precisa informar o motivo e garantir defesa. Sem isso, o bloqueio pode ser revisto na Justiça.\n\n➡️ Arraste e veja o que guardar desde já.\n🚗🛵 Compartilhe no grupo dos motoristas e entregadores."+D,
 hashtags="#motoristadeaplicativo #uber #99 #entregador #motoboy "+H,
 reels="GANCHO: “Teve a conta do app bloqueada sem explicação?” · MEIO: decisão do STJ (suspensão + direito de defesa) e as 4 provas · FINAL: “Manda no grupo dos motoristas.”"),

dict(id="P26", tipo="post", area="Motoristas e Entregadores", titulo="Motorista e entregador de app têm carteira assinada?",
 items=["O tema está em análise no STF (Tema 1291), que vai fixar uma regra válida para todo o país","Enquanto isso, as decisões variam e o STF tem afastado o vínculo em casos individuais","Guarde seus registros de jornada, ganhos e regras impostas pela plataforma"],
 ref="STF, RE 1.446.336 (Tema 1291)",
 legenda="Uma das maiores discussões do Direito hoje: quem trabalha por aplicativo é empregado?\n\nO STF vai decidir a questão no Tema 1291, com efeito para todo o Brasil. Até lá, o cenário é de incerteza — e informação faz diferença.\n\n💬 Você trabalha com aplicativo? Conta nos comentários como é a sua rotina."+D+"\n\n(Antes de publicar: confira se o STF já julgou o Tema 1291.)",
 hashtags="#uberizacao #motoristadeaplicativo #entregador #stf #direitodotrabalho "+H),

dict(id="P27", tipo="post", area="Locação de Veículos", titulo="Alugou moto por aplicativo para trabalhar? Leia o contrato.",
 items=["Faça vistoria com fotos e vídeo na retirada e na devolução","Cobrança de danos deve ser comprovada — multas desproporcionais podem ser reduzidas pelo juiz","A caução deve ser devolvida no prazo do contrato, descontados apenas débitos comprovados"],
 ref="Código Civil, arts. 413 e 422 · CDC, art. 51",
 legenda="Muitos entregadores alugam moto por aplicativo para trabalhar. Mas, na hora de devolver, aparecem cobranças de danos, multas altas e caução retida.\n\nA lei exige boa-fé: cobranças precisam de prova, e multas excessivas podem ser reduzidas.\n\n📌 Salve e mostre para quem trabalha com moto alugada."+D,
 hashtags="#motoboy #entregador #alugueldemoto #contrato #direitodoconsumidor "+H),

dict(id="P28", tipo="carrossel", area="Direito do Consumidor", titulo="Consórcio com “contemplação garantida”: como provar o golpe?",
 sub="Nesses casos, a prova decide o resultado.",
 slides=[
  dict(h="Com prova da promessa", txt="Quando o consumidor comprova que foi enganado com promessa de contemplação imediata, tribunais têm anulado o contrato, determinado a devolução integral dos valores e, em muitos casos, indenização por dano moral."),
  dict(h="Sem prova da promessa", txt="Se o contrato é claro sobre sorteio e lance e não há prova da promessa, a devolução segue a regra do consórcio: em regra, ao final do grupo (Tema 312 do STJ)."),
  dict(h="O que serve de prova", items=["Prints e áudios do WhatsApp com o vendedor","Anúncios e panfletos","Testemunhas da negociação","Gravação da ligação de pós-venda"]),
  dict(h="Faça isso logo", items=["Não assine novos documentos","Registre boletim de ocorrência","Reclame no Procon e no Banco Central","Procure orientação jurídica"]),
 ],
 ref="CDC, arts. 6º, 30 e 37 · Lei 11.795/2008 · STJ, Tema 312",
 legenda="“Paga a entrada que o carro sai em 7 dias.” Se você ouviu isso e assinou um consórcio, guarde todas as conversas.\n\nNa Justiça, quem prova a falsa promessa costuma conseguir a anulação do contrato e a devolução integral. Sem prova, a devolução pode ficar para o fim do grupo.\n\n➡️ Arraste e veja o que serve de prova.\n📌 Compartilhe: esse golpe faz vítimas todos os dias."+D,
 hashtags="#consorcio #golpe #falsacontemplacao #procon #direitodoconsumidor "+H,
 reels="GANCHO: “Te prometeram o carro em 7 dias no consórcio?” · MEIO: com prova x sem prova + 4 provas · FINAL: “Salva e manda pra quem tá pensando em consórcio.”"),

dict(id="P29", tipo="carrossel", area="Direito Bancário", titulo="Juros do financiamento estão altos demais?",
 sub="A revisional compara seus juros com a média do mercado.",
 slides=[
  dict(h="Juros altos, por si só, não bastam", txt="Juros acima de 12% ao ano não são automaticamente ilegais (Súmula 382 do STJ). O que se analisa é se a taxa está muito acima da média de mercado."),
  dict(h="A régua do STJ", txt="Em julgamento repetitivo, o STJ definiu que a revisão é possível quando a taxa contratada for abusiva em comparação à média praticada pelo mercado na época do contrato (REsp 1.061.530)."),
  dict(h="Como conferir", items=["Pegue o contrato e veja a taxa mensal e anual","Consulte as taxas médias no site do Banco Central","Compare o mesmo tipo de crédito e o mesmo mês","Verifique tarifas e seguros embutidos"]),
  dict(h="Tarifas que chamam atenção", txt="A cobrança de TAC e TEC só é válida em contratos firmados até 30/04/2008 (Súmula 565 do STJ). Seguros embutidos sem escolha podem ser venda casada."),
 ],
 ref="STJ, REsp 1.061.530 · Súmulas 382 e 565 do STJ",
 legenda="Financiou carro, moto ou fez empréstimo e sente que está pagando juros demais?\n\nA ação revisional compara a taxa do seu contrato com a média do mercado divulgada pelo Banco Central. Quando a diferença é muito grande, a Justiça pode ajustar.\n\n➡️ Arraste e aprenda a conferir.\n📌 Salve e confira seu contrato."+D,
 hashtags="#revisional #jurosabusivos #financiamento #direitobancario #bancocentral "+H),

dict(id="P30", tipo="carrossel", area="Golpes e Fraudes", titulo="Caiu no golpe do PIX? Corra contra o relógio.",
 sub="Existe um mecanismo oficial para tentar recuperar o dinheiro.",
 slides=[
  dict(h="Acione o MED", txt="O Mecanismo Especial de Devolução, criado pelo Banco Central, permite pedir ao seu banco o bloqueio e a devolução do valor enviado em caso de fraude. O pedido deve ser feito em até 80 dias, mas quanto antes, melhor."),
  dict(h="E se o banco não agir?", txt="Tribunais têm reconhecido a responsabilidade do banco que, avisado da fraude a tempo, deixa de acionar o MED ou demora a agir."),
  dict(h="Atenção", txt="Quando a vítima entrega senhas e códigos ou ignora alertas evidentes, a Justiça pode entender que houve culpa exclusiva do consumidor. Cada caso é analisado."),
  dict(h="Passo a passo", items=["Ligue para o banco e peça o MED","Anote o protocolo","Registre boletim de ocorrência","Guarde prints de tudo"]),
 ],
 ref="Resolução BCB 103/2021 · Súmula 479 do STJ · CDC, art. 14",
 legenda="Fez um PIX e percebeu que era golpe? Cada minuto conta.\n\nPeça imediatamente ao seu banco a abertura do MED (Mecanismo Especial de Devolução). Se o banco foi avisado e não agiu, pode responder pelo prejuízo.\n\n➡️ Arraste e veja o passo a passo.\n📌 Salve: você ou alguém da família pode precisar."+D,
 hashtags="#golpedopix #pix #fraudebancaria #med #bancocentral "+H,
 reels="GANCHO: “Caiu no golpe do PIX? Faz isso AGORA.” · MEIO: MED + protocolo + BO + prints · FINAL: “Salva e manda pros seus pais.”"),

dict(id="P31", tipo="post", area="Golpes e Fraudes", titulo="Golpe do falso advogado: proteja-se.",
 items=["Advogado sério não cobra PIX por WhatsApp para “liberar” valor de processo","Desconfie de números novos, urgência e pedidos de dados pessoais","Confirme sempre ligando para o telefone oficial do seu advogado"],
 ref="Alerta do TJSE · CP, art. 171",
 legenda="O TJSE alertou a população sobre o golpe do falso advogado: criminosos usam nome, foto e dados de processos reais para pedir depósitos às vítimas.\n\nRegra de ouro: na dúvida, ligue para o número oficial do seu advogado antes de qualquer pagamento.\n\n🔁 Compartilhe — informação é a melhor proteção."+D,
 hashtags="#golpe #falsoadvogado #tjse #seguranca #pix "+H),

dict(id="P32", tipo="carrossel", area="Direito Digital", titulo="Instagram hackeado ou bloqueado sem motivo?",
 sub="A rede social também tem deveres com o usuário.",
 slides=[
  dict(h="Bloqueio precisa de motivo", txt="Decisões de diversos tribunais consideram abusivo o bloqueio de conta com justificativa genérica, como “violação dos padrões da comunidade”, sem indicar o que aconteceu."),
  dict(h="Conta invadida", txt="Há condenações de plataformas que não restabeleceram o acesso ou não derrubaram perfis usados por golpistas, mesmo após avisadas pelo usuário."),
  dict(h="Conta de trabalho", txt="Quando o perfil é usado para vender ou divulgar serviços, a Justiça tem considerado o prejuízo maior — podendo haver indenização e ordem urgente de reativação."),
  dict(h="O que fazer", items=["Use os canais oficiais de recuperação","Faça prints de tudo (e-mails, avisos)","Registre boletim de ocorrência se houve invasão","Avise seus seguidores sobre o golpe"]),
 ],
 ref="Marco Civil da Internet (Lei 12.965/2014) · CDC, art. 14 · LGPD",
 legenda="Perdeu o acesso ao seu Instagram, e o suporte só responde com mensagens automáticas?\n\nA Justiça tem obrigado plataformas a restabelecer contas bloqueadas sem motivo claro ou invadidas por golpistas, principalmente quando o perfil é ferramenta de trabalho.\n\n➡️ Arraste e veja o que fazer.\n📌 Salve e ative a verificação em duas etapas hoje."+D,
 hashtags="#instagramhackeado #contabloqueada #direitodigital #meta #redessociais "+H,
 reels="GANCHO: “Seu Instagram foi hackeado?” · MEIO: bloqueio sem motivo + conta de trabalho + 4 passos · FINAL: “Ativa a verificação em duas etapas agora.”"),

dict(id="P33", tipo="post", area="Direito Digital", titulo="Seus dados vazaram. Isso gera indenização?",
 items=["Para o STJ, vazamento de dados comuns não gera dano moral automático: é preciso provar o prejuízo","Vazamento de dados sensíveis ou uso para golpes pode mudar esse cenário","Você pode exigir da empresa informações sobre o vazamento e reclamar na ANPD"],
 ref="STJ, AREsp 2.130.619 · LGPD, arts. 18 e 42",
 legenda="Recebeu aviso de que seus dados vazaram? Calma: nem todo vazamento gera indenização automática.\n\nO STJ entende que, para dados comuns, é preciso comprovar o dano. Mas você tem direito a saber o que aconteceu e a exigir providências da empresa.\n\n📌 Salve para quando precisar."+D,
 hashtags="#lgpd #vazamentodedados #protecaodedados #direitodigital "+H),

dict(id="P34", tipo="post", area="Propriedade Intelectual", titulo="Sua marca é sua? Só se estiver registrada no INPI.",
 items=["No Brasil, a exclusividade da marca vem do registro, não do tempo de uso","O registro vale por 10 anos e pode ser renovado sem limite","MEI, ME, EPP e pessoa física têm desconto nas taxas do INPI"],
 ref="Lei 9.279/1996, arts. 129 e 133",
 legenda="Você tem CNPJ, logo, perfil nas redes e clientes fiéis… mas registrou sua marca?\n\nPela lei, quem registra primeiro tem a exclusividade. Sem registro, outra pessoa pode registrar o seu nome e impedir você de usá-lo.\n\n📌 Salve e marque um empreendedor."+D,
 hashtags="#registrodemarca #inpi #empreendedorismo #mei #propriedadeintelectual "+H),

dict(id="P35", tipo="carrossel", area="Direito Imobiliário", titulo="Usucapião: dá para fazer em cartório?",
 sub="Sim — e costuma ser mais rápido que o processo judicial.",
 slides=[
  dict(h="O que é", txt="É a forma de se tornar dono de um imóvel pela posse prolongada, contínua, sem oposição e com intenção de dono."),
  dict(h="Prazos mais comuns", items=["15 anos — extraordinária (10 se for moradia ou houver obras)","10 anos — com justo título e boa-fé","5 anos — imóvel urbano de até 250 m² usado como moradia","2 anos — familiar, após abandono do lar pelo ex-cônjuge"]),
  dict(h="Em cartório", txt="Sem conflito, o pedido é feito no Cartório de Registro de Imóveis, sempre com advogado, com ata notarial, planta, memorial descritivo e certidões."),
  dict(h="Documentos que ajudam", items=["Contas de luz e água antigas","IPTU pago em seu nome","Contrato de compra (mesmo “de gaveta”)","Declarações de vizinhos"]),
 ],
 ref="Código Civil, arts. 1.238 a 1.242 e 1.240-A · Lei 6.015/73, art. 216-A · Provimento CNJ 149/2023",
 legenda="Mora há anos num imóvel sem escritura? A usucapião pode resolver — e, em muitos casos, direto no cartório.\n\nOs prazos variam de 2 a 15 anos, conforme a situação. Sem conflito com vizinhos ou antigos donos, o procedimento extrajudicial costuma ser bem mais rápido.\n\n➡️ Arraste e veja os prazos e documentos.\n📌 Salve e compartilhe com a família."+D,
 hashtags="#usucapiao #imovel #escritura #cartorio #direitoimobiliario "+H),

dict(id="P36", tipo="carrossel", area="Superendividamento", titulo="Dívidas maiores que o salário? Existe a Lei do Superendividamento.",
 sub="Ela permite renegociar várias dívidas em um único plano.",
 slides=[
  dict(h="Para quem é", txt="Para a pessoa física de boa-fé que não consegue pagar suas dívidas de consumo sem comprometer o mínimo necessário para viver."),
  dict(h="Como funciona", txt="As dívidas são reunidas em um plano de pagamento de até 5 anos, negociado com todos os credores em audiência de conciliação, no Procon ou na Justiça."),
  dict(h="Atenção às regras", items=["É preciso provar o comprometimento do mínimo existencial","Algumas dívidas ficam de fora (ex.: financiamento imobiliário com garantia)","Fraude ou má-fé impedem o benefício"]),
  dict(h="Organize-se", items=["Liste todas as dívidas e credores","Separe contracheques e extratos","Some as despesas básicas da casa","Procure orientação antes de novos empréstimos"]),
 ],
 ref="CDC, arts. 54-A e 104-A (Lei 14.181/2021) · Decreto 11.150/2022",
 legenda="Cartão, empréstimo, cheque especial… e o salário não fecha o mês?\n\nA Lei do Superendividamento permite reunir as dívidas de consumo em um plano de até 5 anos, preservando o mínimo para você viver.\n\n➡️ Arraste e veja como funciona.\n📌 Salve e compartilhe com quem está sufocado pelas dívidas."+D,
 hashtags="#superendividamento #dividas #renegociacao #educacaofinanceira #direitodoconsumidor "+H),

dict(id="P37", tipo="carrossel", area="Direito Previdenciário", titulo="Regras da aposentadoria em 2026: veja o que mudou.",
 sub="As regras de transição ficam mais rígidas a cada ano.",
 slides=[
  dict(h="Aposentadoria por idade", txt="Não mudou: 62 anos para mulheres e 65 para homens, com no mínimo 15 anos de contribuição."),
  dict(h="Regra dos pontos", txt="Em 2026, a soma de idade + tempo de contribuição precisa chegar a 93 pontos (mulheres, com 30 anos de contribuição) ou 103 pontos (homens, com 35 anos)."),
  dict(h="Idade mínima progressiva", txt="Em 2026: 59 anos e 6 meses para mulheres e 64 anos e 6 meses para homens, além do tempo mínimo de contribuição."),
  dict(h="Antes de pedir", items=["Simule no Meu INSS","Confira o CNIS (vínculos e salários)","Compare as regras: a melhor muda o valor","Faça um planejamento previdenciário"]),
 ],
 ref="EC 103/2019, arts. 15, 16, 17, 18 e 20 · Lei 8.213/91",
 legenda="Vai se aposentar? Atenção: em 2026, a regra dos pontos e a idade mínima progressiva subiram.\n\nEscolher a regra certa pode mudar bastante o valor do benefício. Por isso, simule antes de fazer o pedido.\n\n➡️ Arraste e veja os números de 2026.\n📌 Salve e envie para quem está perto de se aposentar."+D+"\n\n(Válido para 2026. Em 2027 os números mudam.)",
 hashtags="#aposentadoria #inss #reformadaprevidencia #previdenciario #planejamentoprevidenciario "+H,
 reels="GANCHO: “O que mudou na aposentadoria em 2026?” · MEIO: 93/103 pontos + 59,5/64,5 anos · FINAL: “Simula no Meu INSS e salva esse vídeo.”"),

dict(id="P38", tipo="post", area="Direito à Saúde", titulo="Plano de saúde pode limitar as terapias para autismo?",
 items=["Não. O STJ definiu que é abusivo limitar o número de sessões de terapias multidisciplinares para pessoas com TEA","A ANS também garante cobertura do método indicado pelo médico","Guarde a prescrição médica e a negativa do plano por escrito"],
 ref="STJ, Tema 1.295 · RN ANS 539/2022 · Lei 12.764/2012",
 legenda="Mães e pais atípicos: o plano de saúde não pode limitar as sessões de terapia do seu filho com autismo.\n\nO STJ fixou, em julgamento repetitivo, que a limitação é abusiva. Se o plano negar, peça a recusa por escrito.\n\n💙 Compartilhe com outras famílias."+D,
 hashtags="#autismo #tea #planodesaude #maeatipica #direitoasaude "+H),

dict(id="P39", tipo="post", area="Direito do Trabalho", titulo="O INSS deu alta, mas a empresa diz que você não pode voltar?",
 items=["Essa situação é chamada de “limbo previdenciário”","A Justiça do Trabalho tem entendido que a empresa deve pagar os salários ou readaptar o trabalhador","Guarde a decisão do INSS e o atestado do médico da empresa"],
 ref="CF, art. 7º · CLT, arts. 2º e 4º · jurisprudência do TST",
 legenda="Recebeu alta do INSS, foi à empresa e ouviu que está inapto para voltar? Você não pode ficar sem salário e sem benefício.\n\nNo chamado limbo previdenciário, a Justiça do Trabalho tem entendido que cabe à empresa pagar os salários ou oferecer outra função.\n\n📌 Salve e compartilhe."+D,
 hashtags="#limboprevidenciario #inss #direitodotrabalho #trabalhador "+H),

dict(id="P40", tipo="post", area="Direito do Passageiro", titulo="Voo atrasado ou cancelado: quais são seus direitos?",
 items=["A partir de 1 hora: comunicação (internet, ligação); 2 horas: alimentação","A partir de 4 horas: hospedagem, se necessário, e opção de reacomodação ou reembolso","Indenização por dano moral depende das circunstâncias — guarde comprovantes de gastos e prejuízos"],
 ref="Resolução ANAC 400/2016, arts. 21 e 26 a 28 · CDC, art. 14",
 legenda="Vai viajar? Saiba o que a companhia aérea deve oferecer em caso de atraso ou cancelamento.\n\nA assistência material é obrigatória e aumenta conforme o tempo de espera. Já a indenização depende do prejuízo concreto, por isso guarde tudo.\n\n✈️ Salve antes da sua próxima viagem."+D,
 hashtags="#vooatrasado #voocancelado #anac #direitodopassageiro #viagem "+H),

dict(id="S05", tipo="story", area="Enquete", titulo="Você já teve uma conta de rede social bloqueada ou hackeada?",
 enquete=["Sim, já aconteceu","Não, nunca"],
 legenda="(Story) Use a figurinha de ENQUETE. No dia seguinte, direcione para o post P32.", hashtags=""),

dict(id="S06", tipo="story", area="Quiz", titulo="Verdadeiro ou falso: advogado pode pedir PIX por WhatsApp para “liberar” o dinheiro do seu processo.",
 enquete=["Verdadeiro","Falso"],
 resposta="FALSO! Isso é golpe. Ligue sempre para o número oficial do seu advogado.",
 legenda="(Story) Use a figurinha de QUIZ. No story seguinte, revele a resposta e direcione para o post P31.", hashtags=""),
]
