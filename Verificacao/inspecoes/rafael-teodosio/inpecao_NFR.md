# Justificativas - NFR
# AUDITOR: Rafael Teodosio


| Questão | Impacto | Justificativa do impacto | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 - O foco do modelo é demonstrar o cumprimento do NFR Softgoal e as possíveis alternativas para o cumprimento do mesmo? | alto| É um dos principais objetivos do modelo | Binário |
| 2 - Os NFR Softgoals são decompostos em sub-softgoals mais específicos?  | alto | Para facilitar o entendimento de um Softgoal é recomendado a decomposição dele em outros mais específicos | Binário |
| 3 - No grafo de representação os conceitos do Framework, seus relacionamentos e priorizações estão em conformidade com a representação visual proposta pelo modelo?  | alto | O modelo proposto pelo Framework permite uma distinção objetiva dos conceitos, relacionamentos e priorizações | Binário |
| 4 - O NFR contém pelo menos mais que três níveis de contribuições? | alto | Modelos muito rasos não possibilitam um bom entendimento do NFR softgoal e das alternativas para o cumprimento do mesmo | Binário |
| 5 - As contribuições identificadas foram corretamente aplicadas?  | alto | Para possibilitar uma boa avaliação dos impactos das decisões | Numérico |
| 6  - O conceito de softgoal foi aplicado corretamente, ou seja, eles são constituídos por requisitos não funcionais ou critérios de qualidade?  | alto | Os conceitos do framework devem ser utilizados de maneira correta | Numérico |
| 7 -  No grafo de representação está padronizado o uso de adjetivos ou substantivos para os Softgoals?  | alto | estar em conformidade com os padrões estabelecidos pelo modelo | Numérico |
| 8 - O conceito de Operacionalização foi aplicado corretamente, ou seja, eles são constituídos por técnicas de desenvolvimento ou requisitos funcionais?  | alto | Os conceitos do framework devem ser utilizados de maneira correta | Numérico |
| 9 - No grafo de representação está padronizado o uso de verbos de ação paras as Operacionalizações?  | alto | estar em conformidade com os padrões estabelecidos pelo modelo | Numérico |
| 10 - Foram identificadas argumentos(Claims)?  | médio | O não uso de claims não é suficiente para avaliar um modelo como ruim, porém o uso do mesmo agrega valor ao modelo | Binário |
| 11 - O conceito de Claim foi aplicado corretamente, ou seja, eles são constituídos por argumentos, razões ou justificativas a favor ou contra as interdependências ?  | alto | Os conceitos do framework devem ser utilizados de maneira correta | Numérico |
| 12 - No grafo de representação está padronizado o uso de Linguagem natural paras os Claims?  | alto | estar em conformidade com os padrões estabelecidos pelo modelo | Numérico |
| 13 - Foram identificadas interdependências implícitas entre os softgoals?  | médio | O não uso de interdependências implícitas não é suficiente para avaliar um modelo como ruim, porém o uso do mesmo agrega valor ao modelo | Binário |
| 14 - As interdependências implícitas entre os softgoals foram corretamente utilizadas?  | alto | Os conceitos do framework devem ser utilizados de maneira correta | Numérico |
| 15 - Foram identificadas priorizações?  | médio | O não uso de priorizações não é suficiente para avaliar um modelo como ruim, porém o uso do mesmo agrega valor ao modelo | Binário |
| 16 - Os Softgoals foram priorizados corretamente?  | alto | Os conceitos do framework devem ser utilizados de maneira correta | Numérico |
| 17 - É possível identificar as decisões e suas alternativas?  | alto | é de extrema importância para o modelo poder visualizar as decisões tomadas e suas alternativas| Binário |
| 18 - A propagação do impacto das decisões foi realizada corretamente, ou seja, respeitando as restrições impostas pelos tipos das contribuições?  | alto | Para determinar se o NFR Softgoal foi cumprido ou não | Numérico |

| NFR | 1* | 2* | 3* | 4* | 5 | 6 | 7 | 8 | 9 | 10* | 11 | 12 | 13* | 14 | 15* | 16 | 17* | 18 |
| --- | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Usabilidade | &#10003; | X | X | X | 2 | 7 | 10 | 7 | 1 | X | NA  | NA  | X  |  NA | X  |  NA  | &#10003;   |  10 |   
| Desempenho | &#10003; | X | X | X | 5 | 7 | 10 | 2 | 0 | X | NA  | NA  | &#10003;  | 0 | X  | NA  |&#10003;   | 5  |     
| Manutenibilidade | &#10003; | X | X | X | 2 | 7 | 10 | 8 | 7 | &#10003;  | 10 |  10 | X | NA  | X  | NA | &#10003;  | 5  |   
| Privacidade | &#10003; |  &#10003; | &#10003; | &#10003; | 8 | 10 | 10 | 10 | 10 |  X |  NA | NA  | &#10003;  | 10 |  X | NA   | &#10003;   | 10  |   
| Suportabilidade | &#10003; |  &#10003; | &#10003; | &#10003; | 10 | 10 | 10 | 10 | 8 | &#10003;  | 10  | 10  | &#10003; | 10  | X  |  NA  |  &#10003; | 10  |

## Usabilidade

| | Justificativa |
|-| ------------- |
|1| O foco do modelo são os Softgoals
|2| Os sub-softgoals são relativos
|3| Os conceitos não estão em conformidade com a representação visual proposta pelo modelo
|4| Não possui mais do que 3 niveis de contribuições
|5|O modelo juntou contribuições "SOME+" com "AND/OR", isso não é permitido
|6|são constituídos por requisitos não funcionais ou critérios de qualidade, mas muito simplorios
|7|está padronizado o uso de adjetivos ou substantivos para os Softgoals
|8|algumas das operacionalizações não são constituídas por técnicas de desenvolvimento ou requisitos funcionais
|9|somente uma operacionalização é um verbo
|10|não utilizados
|11|Não Avaliado(NA)
|12|Não Avaliado(NA)
|13|não possui interdependências implícitas entre os softgoals
|14|Não Avaliado(NA)
|15|não foram identificadas priorizações
|16|Não Avaliado(NA)
|17|É possível identificar as decisões e suas alternativas
|18|A propagação do impacto das decisões foi realizada corretamente

## Desempenho

| | Justificativa |
|-| ------------- |
|1|O foco do modelo são os Softgoals
|2|Os sub-softgoals são relativos
|3|Os conceitos não estão em conformidade com a representação visual proposta pelo modelo
|4|Não possui mais do que 3 niveis de contribuições
|5|Uso de "Makes" erronios, deveriam ser "Helps"
|6|são constituídos por requisitos não funcionais ou critérios de qualidade, mas muito simplorios
|7|está padronizado o uso de adjetivos ou substantivos para os Softgoals
|8|praticamente todas as operacionalizações não são constituídas por técnicas de desenvolvimento ou requisitos funcionais
|9|não há verbo para as operacionalizações
|10|não utilizados
|11|Não Avaliado(NA)
|12|Não Avaliado(NA)
|13|possui interdependências implícitas entre os softgoals
|14|Não foram corretamente utilizadas
|15|não foram identificadas priorizações
|16|Não Avaliado(NA)
|17|É possível identificar as decisões e suas alternativas
|18|propagação errada por conta do uso dos "Unknown" incorretamente

## Manutenibilidade

| | Justificativa |
|-| ------------- |
|1|O foco do modelo são os Softgoals
|2|Os sub-softgoals são relativos
|3|Os conceitos não estão em conformidade com a representação visual proposta pelo modelo
|4|Não possui mais do que 3 niveis de contribuições
|5|O modelo juntou contribuições "SOME+" com "AND/OR", isso não é permitido
|6|são constituídos por requisitos não funcionais ou critérios de qualidade, mas muito simplorios
|7|está padronizado o uso de adjetivos ou substantivos para os Softgoals
|8|algumas das operacionalizações não são constituídas por técnicas de desenvolvimento ou requisitos funcionais
|9|4 das 6 operacionalizações são verbos
|10|O modelo faz uso de Claims
|11|o conceito foi aplicado corretamente
|12|está padronizado o uso de Linguagem natural paras os Claims
|13|não possui interdependências implícitas entre os softgoals
|14|Não Avaliado(NA)
|15|não foram identificadas priorizações
|16|Não Avaliado(NA)
|17|É possível identificar as decisões e suas alternativas
|18|propagação errada por conta do uso dos "Unknown" incorretamente

## Privacidade

| | Justificativa |
|-| ------------- |
|1|O foco do modelo são os Softgoals
|2|Os sub-softgoals são específicos
|3|Os conceitos estão em conformidade com a representação visual proposta pelo modelo
|4|Possui mais do que 3 niveis de contribuições
|5|Uso de "Makes" erronios, deveriam ser "Helps"
|6|são constituídos por requisitos não funcionais ou critérios de qualidade.
|7|está padronizado o uso de adjetivos ou substantivos para os Softgoals
|8|O conceito de softgoal foi aplicado corretamente
|9|todas as operacionalizações fazem o uso de verbos de ação.
|10|não utilizados
|11|Não Avaliado(NA)
|12|Não Avaliado(NA)
|13|possui interdependências implícitas entre os softgoals
|14|foram corretamente utilizadas
|15|não foram identificadas priorizações
|16|Não Avaliado(NA)
|17|É possível identificar as decisões e suas alternativas
|18|A propagação do impacto das decisões foi realizada corretamente

## Suportabilidade

| | Justificativa |
|-| ------------- |
|1|O foco do modelo são os Softgoals
|2|Os sub-softgoals são específicos
|3|Os conceitos estão em conformidade com a representação visual proposta pelo modelo
|4|Possui mais do que 3 niveis de contribuições
|5|O modelo está correto
|6|são constituídos por requisitos não funcionais ou critérios de qualidade.
|7|está padronizado o uso de adjetivos ou substantivos para os Softgoals
|8|O conceito de softgoal foi aplicado corretamente
|9|quase todas as operacionalizações fazem o uso de verbos de ação.
|10|O modelo faz uso de Claims
|11|o conceito foi aplicado corretamente
|12|está padronizado o uso de Linguagem natural paras os Claims
|13|possui interdependências implícitas entre os softgoals
|14|foram corretamente utilizadas
|15|não foram identificadas priorizações
|16|Não Avaliado(NA)
|17|É possível identificar as decisões e suas alternativas
|18|A propagação do impacto das decisões foi realizada corretamente
