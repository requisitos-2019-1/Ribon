| Data | Versão | Descrição | Autor |
| - | - | - | - |
| 31/05/2019 | 1.0 | Template Inicial | Henrique Martins |
| 05/01/2019 | 1.1 | Incrementando template com impacto de perguntas e Resultados numéricos | Guilherme de Lyra |
| 05/01/2019 | 1.2 | Incrementando template com contexto, justificativa e tipo (para perguntas)<br />tabela de relevâncias<br />tabela de validação geral<br />e adição de bibliografia | Guilherme de Lyra |
| 05/01/2019 | 1.3 | Adicionando mais perguntas (baseadas no grupo [Pinterest](http://www.joberth-rogers.ml/2018.2-Requisitos-Pinterest/pre_rastreabilidade_analise/))
| 31/05/2019 | 1.4 | Removendo perguntas duplicadas | Lucas kishima |
| 31/05/2019 | 1.5 | Melhorando perguntas | Lucas kishima |
| 31/05/2019 | 1.6 | Adicionando novas perguntas | Lucas kishima |
| 31/05/2019 | 1.7 | Adicionando justificativas dos impactos | Lucas kishima |

# Verificação - Inspeção [NFR Softgoal](https://github.com/requisitos-2019-1/Ribon/wiki/NFR-Softgoal)

## Questões Avaliadoras

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


## Auditorias Realizadas

* [Inspeção Rafael Teodosio](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/rafael-teodosio/inpecao_NFR.md)
* [Inspeção Lucas Kishima](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/lucas-kishima/inspeca_nfr.md)
* [Inspeção Henrique Martins](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/henrique-martins/inspecao_NFR.md)


## Consenso das Avaliações

| NFR              | 1*     | 2*     | 3*     | 4*      |5 | 6|7 |8 |9 | 10*    | 11 | 12 | 13*      | 14 |15*| 16 | 17*     | 18 |
| ---------------- | ------ | ------ | ------ | ------- |--|--|--|--|--| ------ | -- | -- | -------- | -- | - | -- | ------- | -- |
| Usabilidade      |&#10003;|&#10003;|&#10003;|X        |2 |7 |10|1 |1 |X       | NA | NA | X        | NA | X | NA | &#10003;| 10 |
| Desempenho       |&#10003;|&#10003;|&#10003;|X        |5 |6 |10|0 |0 |X       | NA | NA | &#10003; | 0  | X | NA | &#10003;|  5 |  
| Manutenibilidade |&#10003;|&#10003;|&#10003;|X        |7 |7 |8 |5 |8 |&#10003;| 10 | 10 | X        | NA | X | NA | &#10003;| 5  |
| Privacidade      |&#10003;|&#10003;|&#10003;|&#10003; |9 |8 |4 |9 |9 |X       | NA | NA | &#10003; | 10 | X | NA | &#10003;| 10 |
| Suportabilidade  |&#10003;|&#10003;|&#10003;|&#10003; |10|8 |7 |7 |5 |&#10003;| 10 |10  | &#10003; | 10 | X | NA | &#10003;| 10 |

[Justificativas das Avaliações (Consenso)](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/consenso/nfr.md)


### Relevâncias

| Artefato | Ranking |
| -------- | :-----: |
| A01 | <li>Ponto 1</li><br/><li>Ponto 2</li> |
| A02 | <li>Ponto 1</li><br/><li>Ponto 2</li> |


## Números:                                                                                                                                                                                        
|   | Resultado |
| - | :---------: |
| Número de NFRs: | |
| Total de indicadores (NFRs x Perguntas): |    |
| Taxa de erro de perguntas  (Σ Erros / Total de indicadores): |     |
| Total de pontos de erro com impacto<br /> (Σ Erros/ (questão alta *3) + (questão média *2) + (questão baixa *1)):| |

## Léxicos importantes identificados:
- <Léxico X> [x]
- <Léxico X> [x]
- <Léxico X> [x]

## Validação Geral:
| Artefato | Nota Geral | Menção | Resultado |
| -------- | :--------: | :----: | :-------: |
| Artefato01 | 5.55 | MM | Reprovado |
| Artefato02 | 4.44 | MI | Reprovado |
| Artefato03 | 7.77 | MS | Aprovado |

## Bibliografia
> [Requisitos Aula 20, Mauricio e Milene Serrano](https://aprender.ead.unb.br/pluginfile.php/348668/mod_resource/content/10/Requisitos%20-%20Aula%20020a.pdf)

> [Requisitos, Grupo Pinterest 2018.2](http://www.joberth-rogers.ml/2018.2-Requisitos-Pinterest/pre_rastreabilidade_analise/)
