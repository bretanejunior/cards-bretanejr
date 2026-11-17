# -*- coding: utf-8 -*-
# Banco de conteúdo — Bretane Júnior Sociedade Individual de Advocacia
# Temas extraídos das ações e petições da pasta Advocacia, convertidos em conteúdo
# EDUCATIVO (Provimento 205/2021): sem nomes, sem números de processo, sem resultados de casos.

HASHTAGS_BASE = "#advogadoaracaju #advocaciasergipe #sergipe #aracaju #direito"

POSTS = [
# ---------------- SEMANA 1 ----------------
dict(id="P01", tipo="carrossel", area="Institucional", titulo="Prazer, Bretane Júnior.",
 sub="Advocacia próxima, técnica e humana, em todo o estado de Sergipe.",
 foto=True,
 slides=[
  dict(h="Quem sou", txt="Advogado inscrito na OAB/SE sob o nº 10.203. Atuo há anos ao lado de famílias, trabalhadores, aposentados, servidores, igrejas e pequenos negócios em Aracaju e no interior de Sergipe."),
  dict(h="Áreas de atuação", items=["Consumidor e Bancário","Previdenciário (INSS)","Família e Sucessões","Servidor Público e Concursos","Direito Eclesiástico e Terceiro Setor","Imobiliário e Contratos"]),
  dict(h="Como funciona o atendimento", items=["Atendimento presencial e on-line","Análise individual de cada caso","Linguagem clara, sem “juridiquês”","Acompanhamento do processo do início ao fim"]),
 ],
 legenda="Muito prazer! Sou Bretane Júnior, advogado (OAB/SE 10.203), e este perfil existe para uma coisa: explicar seus direitos de um jeito que qualquer pessoa entenda.\n\nAqui você vai encontrar conteúdos sobre consumidor e bancos, INSS, família e herança, concursos e servidores, igrejas e contratos — sempre com base na lei e na jurisprudência.\n\n👉 Salve este post e siga o perfil para não perder os próximos.\n💬 Conta nos comentários: qual tema você quer ver primeiro?",
 hashtags="#advogado #advocacia #direitosdocidadao "+HASHTAGS_BASE),

dict(id="P02", tipo="carrossel", area="Direito do Consumidor", titulo="Pagou a dívida e seu nome continua negativado?",
 sub="A lei dá prazo para o credor limpar seu nome.",
 slides=[
  dict(h="O prazo é de 5 dias úteis", txt="Depois do pagamento integral da dívida, o credor tem 5 dias úteis para pedir a retirada do seu nome do SPC/Serasa (Súmula 548 do STJ)."),
  dict(h="Negativação indevida pode gerar indenização", txt="Quando a inscrição é indevida — dívida paga, inexistente ou feita por fraude — os tribunais costumam reconhecer o dano moral, inclusive sem precisar provar o prejuízo."),
  dict(h="Atenção à exceção", txt="Se já existia outra negativação legítima no seu nome, a indenização por dano moral em regra não é devida (Súmula 385 do STJ). Mas a retirada do registro indevido continua sendo seu direito."),
  dict(h="O que fazer agora", items=["Guarde o comprovante de pagamento","Consulte seu CPF no Serasa e no SPC","Peça a baixa por escrito ao credor","Persistindo, procure um advogado"]),
 ],
 ref="Súmulas 548 e 385 do STJ · CDC, arts. 6º e 43",
 legenda="Pagou, mas o nome continua “sujo”? Isso não está certo.\n\nPela Súmula 548 do STJ, depois da quitação o credor tem 5 dias úteis para pedir a exclusão do seu nome dos cadastros de inadimplentes. Manter a negativação depois disso pode gerar dever de indenizar.\n\nArraste para o lado e veja o passo a passo ➡️\n\n📌 Salve para consultar depois e envie para quem precisa saber disso.\n\nConteúdo informativo. Cada situação exige análise individual.",
 hashtags="#direitodoconsumidor #nomesujo #serasa #spc #negativacaoindevida "+HASHTAGS_BASE,
 reels="GANCHO (0-3s): “Pagou a dívida e o nome continua no Serasa?” · MEIO: explique a regra dos 5 dias úteis (Súmula 548) e a exceção da Súmula 385 · FINAL: “Salva esse vídeo e manda pra quem está passando por isso.”"),

dict(id="P03", tipo="carrossel", area="Direito Bancário", titulo="Desconto no seu benefício de um empréstimo que você não fez?",
 sub="Aposentados e pensionistas: fiquem atentos.",
 slides=[
  dict(h="A responsabilidade é do banco", txt="Bancos respondem pelos danos causados por fraudes de terceiros em operações bancárias, como empréstimos feitos com documentos falsos (Súmula 479 do STJ)."),
  dict(h="Devolução em dobro", txt="Quem é cobrado indevidamente pode ter direito à devolução em dobro do que pagou, com correção e juros (art. 42, parágrafo único, do CDC)."),
  dict(h="Como descobrir", txt="Acesse o app ou site Meu INSS e baixe o “Extrato de Empréstimos”. Ele mostra todos os contratos consignados no seu benefício."),
  dict(h="O que fazer", items=["Registre boletim de ocorrência","Reclame no banco e no consumidor.gov.br","Guarde extratos e protocolos","Busque orientação jurídica"]),
 ],
 ref="Súmula 479 do STJ · CDC, arts. 14 e 42",
 legenda="Você confere o extrato do seu benefício todo mês?\n\nMuitos aposentados descobrem, tarde demais, descontos de empréstimos consignados que nunca contrataram. A boa notícia: a lei protege você. O banco responde por fraudes de terceiros (Súmula 479 do STJ) e a cobrança indevida pode ser devolvida em dobro.\n\n➡️ Arraste e veja como consultar e o que fazer.\n👵👴 Compartilhe com seus pais e avós — essa informação pode proteger a renda deles.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#aposentado #inss #emprestimoconsignado #fraudebancaria #direitobancario "+HASHTAGS_BASE,
 reels="GANCHO: “Seu benefício está vindo menor?” · MEIO: mostre na tela como baixar o Extrato de Empréstimos no Meu INSS · FINAL: Súmula 479 + “manda pra um aposentado que você ama”."),

dict(id="S01", tipo="story", area="Enquete", titulo="Você já foi negativado por uma dívida que já tinha pago?",
 enquete=["Sim, já aconteceu","Não, nunca"],
 legenda="(Story) Use a figurinha de ENQUETE sobre a área indicada. No dia seguinte, reposte o resultado com o link para o post sobre negativação indevida.",
 hashtags=""),

dict(id="P04", tipo="carrossel", area="Direito Previdenciário", titulo="Aposentadoria rural por idade: quem tem direito?",
 sub="Trabalhador do campo também se aposenta — e com regras próprias.",
 slides=[
  dict(h="Idade mínima", txt="60 anos para homens e 55 anos para mulheres — cinco anos a menos que na aposentadoria urbana."),
  dict(h="Tempo de atividade rural", txt="É preciso comprovar 15 anos de trabalho no campo (agricultura familiar, pesca artesanal etc.), mesmo que de forma descontínua."),
  dict(h="Como provar", items=["Autodeclaração do segurado especial","Documentos em seu nome ou da família (ITR, notas de venda, cadastro no sindicato, certidões)","Testemunhas, quando necessário"]),
  dict(h="Negado pelo INSS?", txt="Ainda é possível recorrer administrativamente ou buscar o benefício na Justiça, com produção de provas."),
 ],
 ref="Lei 8.213/91, arts. 11, VII, 39 e 48, §§ 1º e 2º",
 legenda="Trabalhou a vida inteira na roça? Você pode ter direito à aposentadoria rural por idade.\n\nAs regras são diferentes da aposentadoria urbana: a idade é menor (60 homens / 55 mulheres) e o que conta é o tempo de atividade rural, não as contribuições em carnê.\n\n➡️ Arraste e veja quais documentos ajudam a comprovar.\n💬 Tem alguma dúvida? Deixe nos comentários.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#aposentadoriarural #inss #previdenciario #seguradoespecial #trabalhadorrural "+HASHTAGS_BASE,
 reels="GANCHO: “Quem trabalhou na roça se aposenta mais cedo?” · MEIO: 60/55 anos + 15 anos de atividade rural + 3 documentos que ajudam · FINAL: “Marca alguém do interior que precisa ver isso.”"),

dict(id="P05", tipo="post", area="Direito de Família", titulo="Pensão alimentícia atrasada: o que a lei permite?",
 items=["Pedido de prisão civil do devedor pelas 3 últimas parcelas vencidas e as que vencerem no processo","Penhora de bens, salário e contas bancárias","Protesto da decisão em cartório e negativação do devedor"],
 ref="CPC, arts. 528 e 911 · Súmula 309 do STJ",
 legenda="Pensão atrasada não é “só uma dívida”: é o sustento de uma criança.\n\nA lei oferece ferramentas fortes para a cobrança, como o pedido de prisão civil pelas três últimas parcelas, a penhora de bens e o protesto do devedor.\n\n📌 Salve e compartilhe com quem está nessa situação.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#pensaoalimenticia #direitodefamilia #alimentos #maesolo "+HASHTAGS_BASE),

dict(id="P06", tipo="carrossel", area="Servidor Público e Concursos", titulo="Passou dentro das vagas e não foi chamado?",
 sub="A aprovação dentro do número de vagas gera direito à nomeação.",
 slides=[
  dict(h="Direito à nomeação", txt="O STF decidiu que o candidato aprovado dentro do número de vagas previsto no edital tem direito subjetivo à nomeação durante o prazo de validade do concurso (RE 598.099 – Tema 161)."),
  dict(h="E se contrataram outras pessoas?", txt="Contratar temporários ou terceirizados para a mesma função, enquanto há aprovados aguardando, pode caracterizar preterição — e também gerar direito à nomeação."),
  dict(h="Fique de olho no prazo", txt="O direito precisa ser exercido enquanto o concurso está válido ou logo após o seu término. Não deixe para depois."),
  dict(h="Separe os documentos", items=["Edital e resultado final","Publicações de prorrogação","Provas de contratações para o mesmo cargo"]),
 ],
 ref="CF, art. 37, IV · STF, RE 598.099 (Tema 161)",
 legenda="Você estudou, passou dentro das vagas… e nada de convocação?\n\nPara o STF, quem é aprovado dentro do número de vagas do edital tem DIREITO à nomeação, e não mera expectativa. A contratação de temporários para a mesma função também pode configurar preterição.\n\n➡️ Arraste e veja o que fazer.\n📌 Marque um amigo concurseiro.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#concursopublico #concurseiro #nomeacao #servidorpublico #direitoadministrativo "+HASHTAGS_BASE,
 reels="GANCHO: “Passou no concurso e a prefeitura não chama?” · MEIO: Tema 161 do STF + preterição por temporários · FINAL: “Marca o concurseiro que precisa saber disso.”"),

# ---------------- SEMANA 2 ----------------
dict(id="P07", tipo="carrossel", area="Direito à Saúde", titulo="Plano de saúde pode cancelar seu contrato por atraso?",
 sub="Pode — mas só seguindo regras rígidas.",
 slides=[
  dict(h="Mais de 60 dias de atraso", txt="Nos planos individuais e familiares, o cancelamento por inadimplência só é permitido com atraso superior a 60 dias, consecutivos ou não, nos últimos 12 meses."),
  dict(h="Notificação obrigatória", txt="O consumidor precisa ser comprovadamente notificado até o 50º dia de atraso. Sem essa notificação, o cancelamento é irregular."),
  dict(h="Nunca durante internação", txt="A lei proíbe a suspensão ou o cancelamento do contrato enquanto o titular estiver internado."),
  dict(h="Foi cancelado sem aviso?", items=["Guarde boletos e comprovantes","Peça por escrito o motivo do cancelamento","Registre reclamação na ANS (0800 701 9656)","Procure orientação jurídica com urgência"]),
 ],
 ref="Lei 9.656/98, art. 13, parágrafo único, II e III · normas da ANS",
 legenda="Descobriu que o plano foi cancelado só na hora de usar o hospital? Isso é mais comum do que parece — e muitas vezes é ilegal.\n\nA Lei dos Planos de Saúde exige atraso superior a 60 dias e notificação comprovada até o 50º dia. E durante internação, o cancelamento é proibido.\n\n➡️ Arraste e veja o que fazer.\n📌 Salve: um dia pode ser você ou alguém da família.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#planodesaude #direitoasaude #ans #direitodoconsumidor "+HASHTAGS_BASE,
 reels="GANCHO: “Seu plano de saúde foi cancelado sem aviso?” · MEIO: 60 dias + notificação até o 50º dia + proibição durante internação · FINAL: “Salva esse vídeo.”"),

dict(id="P08", tipo="post", area="Direito do Consumidor", titulo="Comprou pela internet e o produto não chegou?",
 items=["Você pode exigir a entrega, aceitar outro produto equivalente ou cancelar com devolução integral do valor","Em compras on-line, há 7 dias para desistir, contados do recebimento, sem precisar justificar","Guarde prints do anúncio, do pedido e das conversas"],
 ref="CDC, arts. 35 e 49",
 legenda="O prazo de entrega passou e nada do produto? Você não precisa ficar no prejuízo.\n\nO Código de Defesa do Consumidor permite exigir a entrega, trocar por outro equivalente ou cancelar a compra com devolução do dinheiro.\n\n📌 Salve e marque aquele amigo que vive comprando on-line.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#comprasonline #direitodoconsumidor #procon #ecommerce "+HASHTAGS_BASE),

dict(id="P09", tipo="post", area="Direito Previdenciário", titulo="Adicional de 25% na aposentadoria: quem tem direito?",
 items=["Quem recebe aposentadoria por incapacidade permanente (antiga aposentadoria por invalidez)","E precisa da assistência permanente de outra pessoa no dia a dia","O valor pode ultrapassar o teto do INSS e deve ser pedido ao INSS com laudos médicos"],
 ref="Lei 8.213/91, art. 45 · STF, Tema 1095",
 legenda="Você sabia que o aposentado por incapacidade permanente que depende de cuidador pode receber um acréscimo de 25% no benefício?\n\nAtenção: o STF decidiu (Tema 1095) que o adicional não se estende automaticamente às outras aposentadorias. Por isso, cada situação precisa ser avaliada com cuidado.\n\n💬 Ficou com dúvida? Pergunte nos comentários.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#inss #aposentadoria #adicional25 #previdenciario #cuidador "+HASHTAGS_BASE),

dict(id="S02", tipo="story", area="Caixa de perguntas", titulo="Qual é a sua dúvida sobre aposentadoria ou INSS?",
 caixa=True,
 legenda="(Story) Use a figurinha de PERGUNTAS sobre a área indicada. Responda as melhores em stories nos dias seguintes (sem citar dados pessoais de quem perguntou).",
 hashtags=""),

dict(id="P10", tipo="carrossel", area="Sucessões", titulo="Inventário: por onde começar?",
 sub="Organizar a herança evita multas, brigas e bens “travados”.",
 slides=[
  dict(h="Prazo de 2 meses", txt="O inventário deve ser aberto em até 2 meses após o falecimento. O atraso pode gerar multa sobre o imposto de herança (ITCMD), conforme a lei estadual."),
  dict(h="Cartório ou Justiça?", txt="Havendo acordo entre os herdeiros, o inventário pode ser feito em cartório, de forma mais rápida. Havendo conflito, segue pela via judicial."),
  dict(h="Documentos iniciais", items=["Certidão de óbito","Documentos dos herdeiros e do cônjuge","Escrituras, matrículas e documentos de veículos","Extratos bancários e dívidas do falecido"]),
  dict(h="Por que não adiar", txt="Sem inventário não é possível vender, transferir ou regularizar os bens — e as dívidas de impostos continuam crescendo."),
 ],
 ref="CPC, arts. 610, 611 e 659 · Resolução CNJ 35/2007",
 legenda="Perder alguém já é difícil. Deixar a herança parada torna tudo mais pesado.\n\nO inventário deve ser aberto em até 2 meses, e, se houver acordo entre os herdeiros, pode ser feito em cartório. Adiar costuma gerar multa, dívidas de IPTU e bens que não podem ser vendidos.\n\n➡️ Arraste e veja os documentos para começar.\n📌 Salve e compartilhe com a família.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#inventario #heranca #sucessoes #partilha #direitodefamilia "+HASHTAGS_BASE,
 reels="GANCHO: “Alguém da família faleceu e deixou bens?” · MEIO: prazo de 2 meses + cartório x Justiça + 4 documentos · FINAL: “Salva e manda no grupo da família.”"),

dict(id="P11", tipo="carrossel", area="Direito Bancário", titulo="Seguro embutido no financiamento? Pode ser venda casada.",
 sub="Você não é obrigado a contratar o seguro que o banco escolhe.",
 slides=[
  dict(h="O que é venda casada", txt="É condicionar a venda de um produto ou serviço à compra de outro. O Código de Defesa do Consumidor proíbe essa prática."),
  dict(h="O que diz o STJ", txt="Nos contratos bancários, o consumidor não pode ser obrigado a contratar seguro com a instituição financeira ou com a seguradora indicada por ela (Tema 972)."),
  dict(h="Onde costuma aparecer", items=["Financiamento de veículo","Financiamento imobiliário","Empréstimos e cartões","Abertura de conta"]),
  dict(h="Seus direitos", txt="É possível pedir o cancelamento e, conforme o caso, a devolução dos valores cobrados indevidamente."),
 ],
 ref="CDC, art. 39, I · STJ, REsp 1.639.320 (Tema 972)",
 legenda="Confira o seu contrato de financiamento: existe ali um “seguro” que você não pediu?\n\nO CDC proíbe a venda casada, e o STJ já decidiu que o banco não pode obrigar o cliente a contratar o seguro que ele indica.\n\n➡️ Arraste e veja onde essa prática costuma aparecer.\n📌 Salve e confira seus contratos hoje.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#vendacasada #financiamento #direitobancario #seguro #direitodoconsumidor "+HASHTAGS_BASE),

dict(id="P12", tipo="post", area="Direito do Consumidor", titulo="Carro com defeito que só apareceu depois da compra?",
 items=["Defeito oculto: o prazo para reclamar é de 90 dias, contados de quando o problema aparece","O fornecedor tem até 30 dias para resolver","Se não resolver: troca, devolução do valor ou abatimento no preço"],
 ref="CDC, arts. 18 e 26, II e § 3º",
 legenda="Comprou um carro e, semanas depois, surgiu um defeito que ninguém avisou?\n\nNo vício oculto, o prazo de 90 dias só começa a contar quando o defeito se manifesta. Se o problema não for resolvido em 30 dias, você pode escolher entre troca, devolução do dinheiro ou abatimento.\n\n📌 Salve antes da sua próxima compra.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#viciooculto #compradecarro #direitodoconsumidor #veiculos "+HASHTAGS_BASE),

# ---------------- SEMANA 3 ----------------
dict(id="P13", tipo="carrossel", area="Direito de Família", titulo="Mãe ou pai de criação pode constar no registro?",
 sub="O afeto também gera filiação.",
 slides=[
  dict(h="Filiação socioafetiva", txt="É o vínculo de pai ou mãe construído pelo convívio, pelo cuidado e pelo reconhecimento público — mesmo sem laço de sangue."),
  dict(h="Pais biológicos não são apagados", txt="O STF admite a multiparentalidade: o nome do pai ou da mãe socioafetivo pode ser incluído sem retirar o dos pais biológicos (Tema 622)."),
  dict(h="Em cartório ou na Justiça", txt="Em vida, para filhos a partir de 12 anos, o reconhecimento pode ser feito diretamente em cartório. Após o falecimento, o caminho é a ação judicial."),
  dict(h="Efeitos", items=["Nome no registro de nascimento","Direitos de herança","Inclusão dos avós socioafetivos"]),
 ],
 ref="STF, RE 898.060 (Tema 622) · Provimento CNJ 149/2023",
 legenda="Quem cria, cuida e ama também é pai e mãe — e o Direito reconhece isso.\n\nA filiação socioafetiva pode ser registrada, sem apagar os pais biológicos, garantindo nome, herança e todos os efeitos de filho.\n\n➡️ Arraste e entenda como funciona.\n💛 Marque alguém que tem uma mãe ou um pai de coração.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#paternidadesocioafetiva #maternidadesocioafetiva #familia #multiparentalidade #direitodefamilia "+HASHTAGS_BASE,
 reels="GANCHO: “Pai de criação pode entrar na certidão?” · MEIO: socioafetividade + multiparentalidade (Tema 622) + cartório x Justiça · FINAL: “Marca quem tem mãe ou pai de coração.”"),

dict(id="P14", tipo="carrossel", area="Direito Eclesiástico", titulo="Sua igreja está com estatuto e atas em dia?",
 sub="Organização jurídica também é cuidado com o ministério.",
 slides=[
  dict(h="Igreja é pessoa jurídica", txt="Organizações religiosas têm liberdade para se organizar, mas precisam de estatuto registrado em cartório, CNPJ ativo e diretoria eleita conforme o estatuto."),
  dict(h="Os riscos da desatualização", items=["Bloqueio de contas e dificuldade com bancos","Problemas para comprar ou registrar imóveis","Questionamentos sobre a imunidade tributária","Conflitos internos sem regra clara para resolver"]),
  dict(h="Checklist rápido", items=["Estatuto registrado e atualizado","Ata de eleição da diretoria vigente","Livro de atas em ordem","Regimento interno e regras de disciplina de membros"]),
  dict(h="Prevenir é melhor", txt="Um estatuto bem feito dá segurança a pastores, membros e à liderança, e evita disputas judiciais desgastantes."),
 ],
 ref="Código Civil, arts. 44, IV e § 1º, 45 e 46 · CF, art. 150, VI, “b”",
 legenda="Pastor, líder, tesoureiro: quando foi a última vez que o estatuto da sua igreja foi revisado?\n\nEstatuto desatualizado e atas fora de ordem podem travar contas, impedir a compra de imóveis e gerar conflitos difíceis de resolver.\n\n➡️ Arraste e confira o checklist.\n🙏 Compartilhe com a liderança da sua igreja.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#direitoeclesiastico #igreja #estatuto #terceirosetor #lideranca "+HASHTAGS_BASE),

dict(id="P15", tipo="post", area="Direito Previdenciário", titulo="O INSS negou ou cortou seu auxílio-doença?",
 items=["Você pode recorrer administrativamente em até 30 dias","Também é possível ir à Justiça, com nova perícia feita por médico do juízo","Se o direito for reconhecido, os valores atrasados podem ser pagos desde o pedido ou do corte"],
 ref="Lei 8.213/91, arts. 59 e 60 · Lei 9.784/99, art. 59",
 legenda="Perícia negada não é o fim da linha.\n\nO benefício por incapacidade temporária (antigo auxílio-doença) pode ser revisto por recurso no INSS ou pela Justiça, com nova perícia. E os atrasados podem ser pagos desde a data do pedido.\n\n📌 Salve e envie para quem está nessa situação.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#auxiliodoenca #inss #periciainss #previdenciario #beneficio "+HASHTAGS_BASE),

dict(id="S03", tipo="story", area="Quiz", titulo="Verdadeiro ou falso: a pensão acaba automaticamente quando o filho faz 18 anos.",
 enquete=["Verdadeiro","Falso"],
 resposta="FALSO! O fim da pensão depende de decisão judicial (Súmula 358 do STJ).",
 legenda="(Story) Use a figurinha de QUIZ ou ENQUETE. No story seguinte, revele: FALSO — Súmula 358 do STJ — e direcione para o post P18.",
 hashtags=""),

dict(id="P16", tipo="post", area="Direito Bancário", titulo="Golpe dentro da agência bancária: de quem é a responsabilidade?",
 items=["A segurança dentro da agência é dever do banco, não do cliente","O banco responde pelas fraudes praticadas por terceiros em suas operações e dependências","Comunique o banco imediatamente, registre boletim de ocorrência e guarde comprovantes"],
 ref="Súmula 479 do STJ · CDC, art. 14",
 legenda="Alguém se apresentou como funcionário, dentro da agência, e você caiu num golpe? A culpa não é sua.\n\nQuem tem o dever de controlar quem circula dentro da agência é o banco. Por isso, ele responde pelos prejuízos causados por fraudes nas suas dependências.\n\n📌 Compartilhe: esse golpe tem como alvo principal pessoas idosas.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#golpe #fraudebancaria #banco #idosos #direitobancario "+HASHTAGS_BASE),

dict(id="P17", tipo="post", area="Direito Imobiliário", titulo="Contrato de gaveta: quem não registra não é dono.",
 items=["A propriedade de imóvel só se transfere com o registro no Cartório de Imóveis","Sem registro, o imóvel pode ser penhorado por dívidas do vendedor ou vendido a outra pessoa","É possível regularizar: escritura, registro ou, em alguns casos, usucapião"],
 ref="Código Civil, arts. 1.227 e 1.245",
 legenda="Comprou um imóvel “no papel” e nunca registrou? Atenção!\n\nPara a lei, dono é quem está no registro do Cartório de Imóveis. Enquanto isso não acontece, o imóvel continua vulnerável a dívidas e problemas do antigo proprietário.\n\n📌 Salve e regularize o quanto antes.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#contratodegaveta #imovel #direitoimobiliario #usucapiao #escritura "+HASHTAGS_BASE),

dict(id="P18", tipo="post", area="Direito de Família", titulo="Filho fez 18 anos: a pensão acaba automaticamente?",
 items=["Não. O fim da pensão depende de decisão judicial, com direito de defesa do filho","Filhos que estudam (faculdade ou curso técnico) costumam manter a pensão, em regra até os 24 anos","Quem paga deve pedir a exoneração na Justiça — parar por conta própria gera dívida"],
 ref="Súmula 358 do STJ · Código Civil, art. 1.694",
 legenda="Muita gente para de pagar a pensão quando o filho completa 18 anos — e acaba com uma dívida enorme.\n\nPela Súmula 358 do STJ, o cancelamento da pensão do filho maior depende de decisão judicial. E quem está estudando, em regra, mantém o direito.\n\n📌 Salve e compartilhe.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#pensaoalimenticia #exoneracao #maioridade #direitodefamilia "+HASHTAGS_BASE),

# ---------------- SEMANA 4 ----------------
dict(id="P19", tipo="post", area="Associações e Cooperativas", titulo="Excluído de cooperativa ou associação sem direito de defesa?",
 items=["A exclusão de associado só é válida por justa causa prevista no estatuto","É obrigatório um procedimento que garanta defesa e recurso","Exclusão irregular pode ser anulada, com reintegração e, conforme o caso, indenização"],
 ref="Código Civil, art. 57 · Lei 5.764/71, arts. 33 a 35",
 legenda="Cooperativas e associações não podem excluir um membro “de uma hora para outra”.\n\nA lei exige motivo previsto no estatuto e um procedimento com direito de defesa. Sem isso, a exclusão pode ser anulada.\n\n💬 Faz parte de alguma cooperativa ou associação? Conta aqui.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#cooperativa #associacao #direitocivil #devidoprocesso "+HASHTAGS_BASE),

dict(id="P20", tipo="post", area="Direito do Consumidor", titulo="Acidente em corrida por aplicativo: quem responde?",
 items=["O passageiro é consumidor do serviço de transporte","Os tribunais têm reconhecido a responsabilidade da plataforma junto com o motorista","Guarde prints da corrida, boletim de ocorrência e todos os laudos médicos"],
 ref="CDC, arts. 7º, parágrafo único, 14 e 25",
 legenda="Você pediu uma corrida por aplicativo e se feriu em um acidente. E agora?\n\nO passageiro é consumidor, e a responsabilidade pelos danos pode alcançar toda a cadeia do serviço — inclusive a empresa do aplicativo.\n\n📌 Salve: a prova mais importante é o print da corrida.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#transporteporaplicativo #acidente #direitodoconsumidor #indenizacao "+HASHTAGS_BASE),

dict(id="P21", tipo="carrossel", area="Direito Previdenciário", titulo="Trabalhou na roça e na cidade? Conheça a aposentadoria híbrida.",
 sub="O tempo rural pode somar com o tempo urbano.",
 slides=[
  dict(h="Soma de períodos", txt="A aposentadoria híbrida permite somar o tempo de trabalho rural com o tempo de contribuição urbana para completar a carência."),
  dict(h="Idade exigida", txt="Exige a idade da aposentadoria urbana: 65 anos para homens e 62 anos para mulheres."),
  dict(h="Tempo rural antigo também conta", txt="O STJ decidiu que até o trabalho rural mais antigo, mesmo sem contribuições, pode ser somado (Tema 1007)."),
  dict(h="Para quem é ideal", items=["Quem começou na roça e depois foi para a cidade","Quem não completa 15 anos só como urbano","Quem teve o pedido negado por “falta de carência”"]),
 ],
 ref="Lei 8.213/91, art. 48, § 3º · STJ, Tema 1007",
 legenda="Começou a vida trabalhando no campo e depois foi para a cidade? Esse tempo não está perdido.\n\nNa aposentadoria híbrida, o trabalho rural soma com as contribuições urbanas — e, segundo o STJ, até o tempo rural mais antigo conta.\n\n➡️ Arraste e veja se é o seu caso.\n👨‍🌾 Marque alguém com essa história.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#aposentadoriahibrida #aposentadoria #inss #trabalhadorrural #previdenciario "+HASHTAGS_BASE,
 reels="GANCHO: “Trabalhou na roça quando era jovem? Isso pode contar na sua aposentadoria.” · MEIO: soma de tempos + 65/62 anos + Tema 1007 · FINAL: “Manda pra quem começou no campo.”"),

dict(id="P22", tipo="post", area="Direito do Consumidor", titulo="Consórcio vendido como “carro garantido em 7 dias”?",
 items=["Consórcio não é financiamento: a contemplação é por sorteio ou lance","Prometer contemplação imediata é publicidade enganosa","É possível pedir a rescisão e a restituição dos valores pagos — denuncie ao Procon e à polícia"],
 ref="CDC, arts. 6º, III e IV, 30 e 37 · Lei 11.795/2008",
 legenda="“Dá a entrada, adianta umas parcelas e o carro sai na semana que vem.” Cuidado!\n\nSe o contrato assinado é de consórcio, não existe contemplação garantida. Prometer isso é publicidade enganosa — e o consumidor pode ser ressarcido.\n\n📌 Compartilhe e evite que mais pessoas caiam nesse golpe.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#consorcio #golpe #publicidadeenganosa #procon #direitodoconsumidor "+HASHTAGS_BASE),

dict(id="S04", tipo="story", area="Dica rápida", titulo="Dica da semana: guarde TODOS os comprovantes, prints e protocolos.",
 dica="São eles que provam o seu direito.",
 legenda="(Story) Publique com a figurinha de LINK para o seu WhatsApp Business ou o site.",
 hashtags=""),

dict(id="P23", tipo="post", area="Direito de Família", titulo="Separou e o ex ficou morando sozinho no imóvel do casal?",
 items=["O imóvel comprado durante a união pertence aos dois e deve ser partilhado","Quem usa sozinho o bem comum pode ser obrigado a pagar aluguel ao outro","O pedido pode ser feito na ação de divórcio ou de dissolução de união estável"],
 ref="Código Civil, arts. 1.319 e 1.725",
 legenda="O relacionamento acabou, mas só um continuou usando a casa que pertence aos dois?\n\nA jurisprudência admite que o ex-companheiro que usa sozinho o imóvel comum pague aluguel ao outro, proporcional à sua parte, até a partilha ou venda do bem.\n\n📌 Salve e compartilhe.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#divorcio #uniaoestavel #partilha #direitodefamilia "+HASHTAGS_BASE),

dict(id="P24", tipo="post", area="Direito Administrativo", titulo="Seu imóvel vai ser desapropriado?",
 items=["A Constituição garante indenização justa, prévia e em dinheiro","Você pode discutir o valor oferecido pelo poder público, inclusive com perícia","Podem incidir correção monetária e juros sobre a diferença"],
 ref="CF, art. 5º, XXIV · Decreto-Lei 3.365/41",
 legenda="Obras de estradas e avenidas costumam exigir desapropriações. Mas o proprietário não é obrigado a aceitar qualquer valor.\n\nA Constituição garante indenização justa e prévia, e o valor oferecido pode ser contestado, inclusive com perícia judicial.\n\n📌 Salve e compartilhe com quem mora perto de obras públicas.\n\nConteúdo informativo. Cada caso exige análise individual.",
 hashtags="#desapropriacao #imovel #direitoadministrativo #indenizacao "+HASHTAGS_BASE),
]

CONTATO = dict(insta="@bretanejr", site="bretanejunioradv.com", email="bretanejunior@gmail.com", oab="OAB/SE 10.203")
