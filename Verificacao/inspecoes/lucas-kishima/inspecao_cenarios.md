# Justificativas Argumentação
# AUDITOR: Lucas kishima

## Perguntas

| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 - O título do cenário indica uma ação? | Alto | Regra do modelo | Binário |
| 2 - O objetivo descreve a finalidade do cenário, em relação ao sistema? | Alto | Regra do modelo | Binário |
| 3 - O contexto/pré-condições descreve o que deva ter sido atingido previamente para que se realize o objetivo proposto pelo cenário atual, sem espaço para dúvidas? | Alto | Regra off-model | Binário |
| 4 - A lista de recursos realmente descrevem todos os recursos necessários para se atingir o objetivo do cenário? | Alto | Regra do modelo | Binário |
| 5 - Os termos específicos estão linkados com léxicos? | Médio | A linkagem facilita o acesso à um maior entendimento, ou esclarecimento, sobre o termo em questão | Numérico |
| 6 - As pós-condições explicam detalhadamente o que ocorre após os episódios se encerrarem? | Alto | Regra do modelo | Numérico |
| 7 - Os episódios são claros o suficiente para não deixarem dúvidas, e estão de acordo com o funcionamento real do produto? | Alto | É importante que seja claro para o desenvolvedor conseguir seguir os passo-a-passos sem ter indagações internas (o que pode resultar em tomadas de decisões que não acordem com o que se esperava daquela feature)  | Numérico |
| 8 - As restrições representam requisitos que devem ser cumpridos para o cenário ocorrer? | Alto | Regra do modelo | Binário |
| 9 - As exceções representam alguma situação que atrapalha o usuário de atingir o objetivo inicial? | Alto | Regra do modelo | Binário |
| 10 - O cenário ajuda no entendimento do sistema em geral ou de alguma funcionalidade em específico? | Alto | Finalidade do modelo | Numérico |



| Cenários                            | 1*| 2*| 3*| 4*| 5 | 6 | 7 | 8*| 9*| 10 |
| ----------------------------------- | - | - | - | - | - | - | - | - | - | -- |
| CN001 - Coletar Ribon Diário        | &#10003;  | &#10003; | x | &#10003;  | 10 | 6 | 10 | &#10003; | x | 5 |
| CN002 - Comprar Ribons              | &#10003; | &#10003; | x | &#10003;  | 10 |  10 | 10  | x | x | 7 |
| CN003 - Convidar Amigos             | &#10003; | &#10003;  | x | &#10003; |  10 | 5 | 10 | 5 | x | 6 |
| CN004 - Criar Conta                 | &#10003; | &#10003;  | x | &#10003;  | 10  | 0 | 0  | 3  | x  | 6 |
| CN005 - Doar Fortificação Alimentar | &#10003; | &#10003;  | x  | &#10003;  | 10  | 10 | 10  | 10 | x | 8   |
| CN006 - Doar Água Potável           | &#10003; | &#10003;  | x  | &#10003;  | 10  | 10 | 10  | 10 | x |  7  |
| CN007 - Doar Ribons                 | &#10003; | &#10003;  | x  | &#10003;  |  10 | 8  | 10 | 10  | x |  8  |
| CN008 - Escolher Causa              | &#10003; | &#10003;  | x | x | 10  | 0 | 10 | 5 | 8 | 5  |
| CN009 - Ler Histórias               | x | x | x | x | 10  |  3 | 8 | 10  | x | 3 |
| CN010 - Ver Causas                  | &#10003; | &#10003;  | x | x  | 10  | 5 | 10 | 10 | x | 7 |
| CN011 - Verificar Comprovantes      | &#10003; | &#10003;  | x | x | 10  | 10  | 10  | 10  | x | 7 |
| CN012 - Visualizar ONGs             | &#10003; | &#10003;  | x  | &#10003; | 10  | 10  | 6 | 10 | x | 7 |
| CN013 - Doar Medicamentos           | &#10003; | &#10003;  | x | &#10003;  | 10  | 10 | 10 | 10 | x | 8 |
| CN014 - Doar Saúde Básica           | &#10003; | &#10003;  | x | &#10003;  | 10  | 10 | 10 | 10 | x | 8 |

## CN001 - Coletar Ribon Diário
| | Justificativa |
|-| ------------- |
|2|  O objetivo de coletar o presente diário não é descrevar as etapas de coleta, mas sim como de fato realizar a coleta do mesmo. |
|3|  Uma das pré-condições não listas é que o presente diário já não tenha sido coletado.|
|6| Uma das pós-condições da coleta é que o presente diário mude seu estado para coletado e não permita novas coletas|
|7| Faltam cenários para descrever as situações de falha, como por exemplo o usuário tente coletar o presente diário novamente |
|9| O aplicativo trava???, estão mal escritas. Além disso erro no sistema de doação não é uma exceção |
|10| pois falha em 5 perguntas |

## CN002 - Comprar Ribons
| | Justificativa |
|-| ------------- |
|3| A restrição de que o usuário possua limite em seu cartão para a entrega, não é o unico critério para aprovação da compra pela operadora |
|8| A restrição de que o usuário possua limite em seu cartão para a entrega, não é o unico critério para aprovação da compra pela operadora |
|9| O aplicativo trava??? |
|10| pois falha em 3 perguntas |

## CN003 - Convidar Amigos
| | Justificativa |
|-| ------------- |
|3|  O usuário não precisa estar logado. |
|6|  O usuário só recebe os ribons, caso o amigo aceite o convite. |
|8| O usuário não precisa ter redes sociais |
|9| O aplicativo trava???, falha no app não seria a mesma coisa?, estão muito mal escritas.|
|10| pois falha em 4 perguntas |

## CN004 - Criar Conta
| | Justificativa |
|-| ------------- |
|3| As pré-condições, como ter o aplicativo instalado não foram escritas. |
|6| Não possui pós-condições |
|8| Pessoa não precisa inserir nem email ou senha|
|9| Pessoa não ter e-mail e Pessoa não ter conta no Google ou Facebook, não são exceções. Além disso está mal escrito.|
|10| pois falha em 4 perguntas |

## CN005 - Doar Fortificação Alimentar
| | Justificativa |
|-| ------------- |
|3| O usuário deve possuir ribons, além disso ele deve desejar doar pra aquela causa específica. |
|9|O aplicativo trava???, falha no app não seria a mesma coisa?, estão muito mal escritas.|
|10| pois falha em 2 perguntas |

## CN006 - Doar Água Potável
| | Justificativa |
|-| ------------- |
|3| O usuário deve possuir ribons, além disso ele deve desejar doar pra aquela causa específica. |
|6| O usuário pode conhecer mais sobre o patrocinador |
|9|O aplicativo trava???, estão mal escritas.|
|10| pois falha em 3 perguntas |

## CN007 - Doar Ribons
| | Justificativa |
|-| ------------- |
|3| O usuário precisa escolher a causa antes de realizar a doação|
|9|O aplicativo trava???, estão mal escritas.|
|10| pois falha em 2 perguntas |

## CN008 - Escolher Causa
| | Justificativa |
|-| ------------- |
|3| não possui nenhuma pré-condição |
|4| causa não seria um recurso |
|6|Não possui pós-condições|
|8| não é necessário estar logado|
|9| estão mal escritas.|
|10| pois falha em 5 perguntas |

## CN009 - Ler Histórias
| | Justificativa |
|-| ------------- |
|1| A professora sugeriu alteração para visualizar histórias|
|2| não para leitura, mas para visualização|
|3| O usuários navegar para a aba Histórias, sites de terceiros compartilhem histórias com a ribon.|
|4| faltou o recurso História|
|6| compartilhar histórias e ir a página da história devem ser pós condições.|
|7| Ler deve ser substituido por visualizar|
|9|O aplicativo trava???, estão mal escritas. Além disso erro no sistema de doação não é uma exceção|
|10| pois falha em 7 perguntas |

## A0010_Ver Causas
| | Justificativa |
|-| ------------- |
|3| não possui nenhuma pré-condição |
|5| O usuário pode ver informações sobre a causa |
|9| estão mal escritas |
|10| pois falha em 3 perguntas |

## A0011_Verificar Comprovantes
| | Justificativa |
|-| ------------- |
|3| Usuário desejar ler Histórias/notícias não é uma pré condição, abrir o arquivo é uma pré condição, possuir acesso a internet. |
|4| causa não seria um recurso |
|9| O aplicativo trava???, estão mal escritas. Além disso erro no sistema de doação não é uma exceção |
|10| pois falha em 3 perguntas |

## A0012_Visualizar ONGs
| | Justificativa |
|-| ------------- |
|3|O usário possuir acesso a internet, o usuário clicar em info sobre a causa, ou clicar na causa na página de perfil|
|7| tambem são cenários, o usuário navega pra aba doações, usuário clica em info na causa.             |
|9|  O aplicativo trava???, falha no app não seria a mesma coisa?, estão muito mal escritas. |
|10| pois falha em 3 perguntas |

## A0013_Doar Medicamentos
| | Justificativa |
|-| ------------- |
|3|O usuário deve possuir ribons, além disso ele deve desejar doar pra aquela causa específica.|
|9|O aplicativo trava???, estão mal escritas.|
|10| pois falha em 2 perguntas |

## A0014_Doar Saúde Básica  
| | Justificativa |
|-| ------------- |
|3|O usuário deve possuir ribons, além disso ele deve desejar doar pra aquela causa específica.|
|9|O aplicativo trava???, estão mal escritas.|
|10| pois falha em 2 perguntas |
