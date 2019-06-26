# distribuição de temas



Módulo II - Pré-rastreabilidade (2 pessoas)

    Rich-Picture

        principais = [bahia]

        "convidados" = {}

    Argumentação

        principais = [henrique]

        "convidados" = {}

    5W2H

        principais = []

        "convidados" = {}





Módulo III - Elicitação (4 pessoas)

    Story Telling

        principais = [victor]

        "convidados" = {}

    Observação/Análise de Protocolo

        principais = [kishima]

        "convidados" = {}

    Introspecção

        principais = []

        "convidados" = {}

    Questionário

        principais = [guilherme]

        "convidados" = {}

    MoSCoW

        principais = []

        "convidados" = {}

    First Things First

        principais = [henrique]

        "convidados" = {}





Módulo IV - Modelagem (7 pessoas)

    Modelagem Inicial

        Cenários

            principais = [bahia]

            "convidados" = {}

        Léxicos

            principais = [kishima]

            "convidados" = {guilherme}

    Modelagem Tradicional

        Casos de uso

            principais = [guilherme]

            "convidados" = {}

        Especificação suplementar

            principais = [bahia]

            "convidados" = {}

    Modelagem Ágil

        Backlog de Produto

            principais = [victor]

            "convidados" = {}

        Critérios de aceitação

            principais = [victor]

            "convidados" = {}

    Modelagem Intencional

        NFR Softgoal

            principais = [kishima]

            "convidados" = {bahia}

        iStar

            principais = []

            "convidados" = {guilherme}



Módulo V - Análise (3 pessoas)

    Verificação

        principais = [guilherme, bahia, henrique]

        "convidados" = {Victor}





Módulo VI - Pós-Rastreabilidade (3 pessoas)

    Pós-Rastreabilidade

        principais = [guilherme, victor, henrique]

        "convidados" = {bahia}





# apresentação final

apresentação - 30s

    iai eu sou x vou falar de y

modulo 2 - 30s

    richpicture/bahia = 15s

    argumentação/henrique = 15s

modulo 3 - 1m20s

    storytelling/victor = 10s

    protocolo/kishima = 20s

    questionario/guilherme = 10s

    ftf/henrique = 15s

modulo 4 - 6min05s

    cenarios/bahia = 50s

    lexicos/kishima = 40s

        lexicos/guilherme = 10s

    casos de uso/guilherme = 50s

    espec supl/bahia = 50s

    backlog/victor = 50s

    criterios/victor = 50s

    nfr/kishima = 50s

    istar/guilherme = 15s

modulo 5 - 3m20s

    verificação

        guilherme = 1m20s

        henrique = 1m30s

        bahia = 30s

modulo 6 - 2m40s

    pós-rastreabilidade

        guilherme = 40s

        victor = 1m

        henrique = 1m



tempo total:

    bahia = 30s+50s+50s+30s = 2m40s

    kishima = 40s+40s+50s = 2m10s

    victor = 20s+50s+50s+60s = 3m

    guilherme = 15s+10s+50s+10s+90s+60s = 3m55s

    henrique = 30s+15s+90s+60s = 3m15s





# roteiro de falas 



## guilherme



questionario

    Embora a estrutura do questionario estivesse relativamente boa, não teve muita adesão -- apenas 14 pessoas responderam, portanto não deu

    pra tirar muitos insights positivos dele



casos de uso

    foi um modulo bastante interessante. foi o primeiro modulo que começamos a trabalhar mais como um time inteiro (e nao 5 times em um, como 

    os proefssores disseram). nele, definimos um template qualitativo, para que houvesse uma padronização na qualidade (obviamente)

    além disso, fizemos 2 distinções importantes, que à priori nao parecia obvio: o que é Diagrama e o que é Caso de uso

    foram aproximadamente 30 casos de uso distintos, e 4 diagramas.

    além disso, pro desenvolvimento desse modulo, utilizamos uma ferramenta chamada Plantuml, bem similar ao Dot do Graphviz

    e através do arquivo plantuml, ja geravamos um template praticamente pronto. 



verificação

    pegamos perguntas do airbnb, uber e pinterest; então, reunimo-nos os 5 membros e fomos refatorando e adicionando perguntas,

    pois varias delas eram superficiais. entao em vez de atestarmos se algo existia, atestavamos a qualidade da coisa que existia

    à cada pergunta existia um impacto, uma justificativa do impacto e um 

                                        tipo (sendo numerico [subjetivo] ou binario [objetivo, referenciando-se as regras do modelo])

    cada verificação foi feita individualmente, e, depois, faziamos a tabela consenso que seria o merge das opinioes. doravante

    nao existia voto vencido nem voto medio, alguma das partes haveria de se convencer o porque de nota X ser atribuida, e, depois, há

    a justificativa dessa mesma nota.

    além disso, criei um display interativo cujo qual gerava automaticamente a tabela markdown, e, apos isso, um script que gerava

    gráficos importantes.



pós rastreabilidade

    bom, foi na pós rastreabilidade que o protótipo foi desenvolvido. nele, botoes azuis indicam mudança de fluxo (troca de telas etc), 

    vermelhos indicam dropdowns com os requisitos relacionados àquele botão, e amarelos indicam links externos (no github)

    além disso, foi adicionado uma nova feature para levantarmos requisitos da mesma: um jogo, onde o usuário consumiria ads constantemente, e, portanto

    receberia ribons por isso

    ao total, foram 198 telas desenvolvidas.

    vale ressaltar que uma gambiarra foi necessaria ja que a ferraamenta utrilizada nao permitia hyperlinks, então os hyperlinks eram gerados via

    script





## bahia

RICHPICTURE(MAX 10s): 

    Junto com a argumentação os richpictures não estavam com uma qualidade aceitavel, 
    mas como foi dito anteriormente, a prioridade foi para outros artefatos
    cujo grupo acredita agregar mais valor.

CENARIOS(MAX 50s): 

    os Cenários foi um dos modelos selecionados para receber melhorias com base nas verificações 
    realizadas foram identificados algums problemas recorrentes que eram propagados em todos eles que foram as Exceções e as Restrições
    As exceções não estavam representando alguma situação que atrapalhava o usuário de atingir o objetivo inicial e 
    As restrições não representavam requisitos que deveriam ser cumpridos para o cenário ocorrer alem disso foi definido que 
    Os objetivos deveriam descrever a finalidade do cenário, EM RELAÇÃO AO SISTEMA. Isso tambem acarretou na modificação dos objetivos
    da maioria dos cenários. Após a revisão dos trabalhos realizados, foram identificados mais 4 cenários.

ESPECIFICAÇ O SUPLEMENTAR(MAX 15s): 
   
    A especificação suplementar nas versões anteriores estava incompleta e simples,
    com base no feedback dos professores foi possivel incrementa-lá para que estivesse de acordo com a realidade dos requisitos não-funcionais
    existentes na aplicação. (KISHIMA FALA).

NFR DESEMPENHO E USABILIDADE(MAX 35s): 

    O NFR Frameowork foi um dos trabalhos mais fracos, e com base na verificação estava nitida a qualidade baixa deles.

    Usabilidade: a maior critica sobre eles eram que eles estavam muito rasos com poucos níveis de contribuição e o conceito de operacionalização estava errado.
    nesse novo modelo fica nítido o avanço em relação aos niveis de comtribuição e operacionalizações.

    Desempenho: Aqui é onde o impacto das versões é maior com conta da simplicidade da primeira versão, onde na versão atual possui um numero maior de
    contribuições e operacionalizações porpocionando assim uma riquesa maior de detalhes.

VERIFICAÇÃO (MAX 30s) :

POS-RASTREABILIDADE???(MAX 30s):

    O Backward-from dos requisitos não-funcionais estavam incompletos na parte de elicitação, algums estavam Modelados mas não Elicitados
    então foi realizada a Elicitação desses requisitos e adicionados a tabela, deixando a tabela com ao menos um requisito elicitado e modelado.



## kishima



## henrique



## victor
