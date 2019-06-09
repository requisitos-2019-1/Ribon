# Justificativas - NFR
# AUDITOR: Henrique Martins


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
| Usabilidade | &#10003; | &#10003; | &#10003; | x | 3 | 10 | 10 | 8 | 2 | x | 10 | 10 | x | 10 | x | 10 | &#10003; | 10 |  
| Desempenho | &#10003; | &#10003; | &#10003; | x | 6 | 10 | 10 | 0 | 0 | x | 10 | 10 | x | 10 | x | 10 | &#10003; | 7 | 
| Manutenibilidade | &#10003; | &#10003; | &#10003; | x | 2 | 10 | 7 | 5 | 2 | &#10003; | 10 | 10 | x | 10 | x | 10 | &#10003; | 6 | 
| Privacidade | &#10003; | &#10003; | &#10003; | &#10003; | 7 | 10 | 2 | 10 | 8 | x | 10 | 10 | x | 10 | x | 10 | &#10003; | 10 |  
| Suportabilidade | &#10003; | &#10003; | &#10003; | &#10003; | 10 | 10 | 5 | 10 | 5 | &#10003; | 10 | 10 | x | 10 | x | 10 | &#10003; | 10 | 

## Usabilidade

| | Justificativa |
|-| ------------- |
|1| O foco do modelo é o NFR Softgoal |
|2| Os NFR Softgoals são decompostos em sub-softgoals |
|3| Os relacionamentos e priorizações estão em conformidade |
|4| O NFR contém apenas 3 níveis de contribuição |
|5| Em muitos casos, juntou contribuições SOME+ com AND/OR, o que não é permitido |
|6| É construído por requisito não-funcional |
|7| Todos os softgoals seguem o padrão |
|8| Uma das operacionalizações não é um requisito funcional (rápida transação entre as telas) |
|9| Apenas uma operacionalização usa verbo de ação |
|10| Não há nenhum Claim |
|11| Não há Claim, portanto não há erro |
|12| Não há Claim, portanto não há erro |
|13| Não foram identificadas interdependências implícitas |
|14| Não há nenhuma interdependência implícita, portanto não há erro |
|15| Não foram identificadas priorizações implícitas |
|16| Não há nenhuma priorizações, portanto não há erro |
|17| É possível fazer as identificações necessárias |
|18| Os impactos estão corretos |

## Desempenho

| | Justificativa |
|-| ------------- |
|1| O foco do modelo é o NFR Softgoal |
|2| Os NFR Softgoals são decompostos em sub-softgoals |
|3| Os relacionamentos e priorizações estão em conformidade |
|4| O NFR contém apenas 2 níveis de contribuição |
|5| Vários usos de "makes", quando o correto seria "helps" |
|6| É construído por requisito não-funcional |
|7| Todos os softgoals seguem o padrão |
|8| Nenhum das operacionalizações é um requisito funcional |
|9| Nenhuma operacionalização usa verbo de ação |
|10| Não há nenhum Claim |
|11| Não há Claim, portanto não há erro |
|12| Não há Claim, portanto não há erro |
|13| Não foram identificadas interdependências implícitas |
|14| Não há nenhuma interdependência implícita, portanto não há erro |
|15| Não foram identificadas priorizações implícitas |
|16| Não há nenhuma priorizações, portanto não há erro |
|17| É possível fazer as identificações necessárias |
|18| Ocorreram alguns erros com o "unknown" |

## Manutenibilidade

| | Justificativa |
|-| ------------- |
|1| O foco do modelo é o NFR Softgoal |
|2| Os NFR Softgoals são decompostos em sub-softgoals |
|3| Os relacionamentos e priorizações estão em conformidade |
|4| O NFR contém apenas 3 níveis de contribuição |
|5| Em muitos casos, juntou contribuições SOME+ com AND/OR, o que não é permitido. Além disso, vários usos de "makes", quando o correto seria "helps" |
|6| É construído por requisito não-funcional |
|7| Apenas um softgoal não segue o padrão |
|8| Metade das operacionalizações não é um requisito funcional |
|9| Apenas uma operacionalização usa verbo de ação |
|10| Há um Claim |
|11| O Claim é constituído por um argumento |
|12| O Claim está escrito em linguagem natural |
|13| Não foram identificadas interdependências implícitas |
|14| Não há nenhuma interdependência implícita, portanto não há erro |
|15| Não foram identificadas priorizações implícitas |
|16| Não há nenhuma priorizações, portanto não há erro |
|17| É possível fazer as identificações necessárias |
|18| Ocorreram alguns erros com o "unknown" |

## Privacidade

| | Justificativa |
|-| ------------- |
|1| O foco do modelo é o NFR Softgoal |
|2| Os NFR Softgoals são decompostos em sub-softgoals |
|3| Os relacionamentos e priorizações estão em conformidade |
|4| O NFR contém mais do que 3 níveis de contribuição |
|5| Alguns usos de "makes" ao invés de "helps" |
|6| É construído por requisito não-funcional |
|7| Apenas um softgoal segue o padrão estabelecido |
|8| Todas as operacionalizações são requisitos funcionais |
|9| Apenas duas operacionalizações não usam verbo de ação |
|10| Não há nenhum Claim |
|11| Não há Claim, portanto não há erro |
|12| Não há Claim, portanto não há erro |
|13| Não foram identificadas interdependências implícitas |
|14| Não há nenhuma interdependência implícita, portanto não há erro |
|15| Não foram identificadas priorizações implícitas |
|16| Não há nenhuma priorizações, portanto não há erro |
|17| É possível fazer as identificações necessárias |
|18| Os impactos estão corretos |

## Suportabilidade

| | Justificativa |
|-| ------------- |
|1| O foco do modelo é o NFR Softgoal |
|2| Os NFR Softgoals são decompostos em sub-softgoals |
|3| Os relacionamentos e priorizações estão em conformidade |
|4| O NFR contém mais do que 3 níveis de contribuição |
|5| Não foram encontrados erros nas contribuições |
|6| É construído por requisito não-funcional |
|7| Dois softgoals não seguem o padrão estabelecido |
|8| Todas as operacionalizações são requisitos funcionais |
|9| Metade das operacionalizações não usam verbo de ação |
|10| Há um Claim |
|11| O Claim é constituído por um argumento |
|12| O Claim está escrito em linguagem natural |
|13| Não foram identificadas interdependências implícitas |
|14| Não há nenhuma interdependência implícita, portanto não há erro |
|15| Não foram identificadas priorizações implícitas |
|16| Não há nenhuma priorizações, portanto não há erro |
|17| É possível fazer as identificações necessárias |
|18| Os impactos estão corretos |

