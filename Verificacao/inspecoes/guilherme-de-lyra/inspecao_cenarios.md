# Justificativas Cenários
# AUDITOR: Guilherme de Lyra

| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 - O título do cenário indica uma ação? | Alto | Regra do modelo | Binário |
| 2 - O objetivo descreve a finalidade do cenário, em relação ao sistema? | Alto | Regra do modelo | Binário |
| 3 - O contexto/pré-condições descreve o que deva ter sido atingido previamente para que se realize o objetivo proposto pelo cenário atual, sem espaço para dúvidas? | Alto | Regra do modelo | Binário |
| 4 - A lista de recursos realmente descrevem todos os recursos necessários para se atingir o objetivo do cenário? | Alto | Regra do modelo | Binário |
| 5 - Os termos específicos estão linkados com léxicos? | Médio | A linkagem facilita o acesso à um maior entendimento, ou esclarecimento, sobre o termo em questão | Numérico |
| 6 - As pós-condições explicam detalhadamente o que ocorre após os episódios se encerrarem? | Alto | Regra do modelo | Numérico |
| 7 - Os episódios são claros o suficiente para não deixarem dúvidas, e estão de acordo com o funcionamento real do produto? | Alto | É importante que seja claro para o desenvolvedor conseguir seguir os passo-a-passos sem ter indagações internas (o que pode resultar em tomadas de decisões que não acordem com o que se esperava daquela feature)  | Numérico |
| 8 - As restrições representam requisitos que devem ser cumpridos para o cenário ocorrer? | Alto | Regra do modelo | Binário |
| 9 - As exceções representam alguma situação que atrapalha o usuário de atingir o objetivo inicial? | Alto | Regra do modelo | Binário |
| 10 - O cenário ajuda no entendimento do sistema em geral ou de alguma funcionalidade em específico? | Alto | Finalidade do modelo | Numérico |

<!-- &#10003; -->

| Cenários (Guilherme de Lyra)                 | 1*| 2*| 3*| 4*| 5 | 6 | 7 | 8*| 9*| 10 |
| ----------------------------------- | - | - | - | - | - | - | - | - | - | -- | -- |
| CN001 - Coletar Ribon Diário        | &#10003;  | X  | &#10003;  | &#10003;  | 10 | 8 | 10 | &#10003; | &#10003; | 9 |
| CN002 - Comprar Ribons              | &#10003;  | X  | &#10003;  | &#10003;  | 10  | 10  | 10  | &#10003;  | &#10003;  |  10  |
| CN003 - Convidar Amigos             | &#10003;  | X | X | &#10003;  |   10 | 5 |  9 | X | &#10003;  |   8  |
| CN004 - Criar Conta                 | &#10003;  | &#10003; | &#10003;  | &#10003; | 10  | 0  | 0 | &#10003;  | X | 5 |
| CN005 - Doar Fortificação Alimentar | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 10 | 10 | &#10003; | &#10003; |  10 |
| CN006 - Doar Água Potável           | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 10 | 10 | &#10003; | &#10003; |  10 |
| CN007 - Doar Ribons                 | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 10 | 10 | &#10003; | &#10003; |  10 |
| CN008 - Escolher Causa              | &#10003;  | &#10003; | &#10003;  | &#10003;  | 10  | 0 |  10 | &#10003;  | &#10003;  | &#10003; | 9 |
| CN009 - Ler Histórias               | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 5 | 10 | &#10003;  | X | 10 |
| CN010 - Ver Causas                  | &#10003;  | &#10003; | &#10003; | &#10003;  | 10  | 10  | 8 | &#10003;  | &#10003; | 10 |
| CN011 - Verificar Comprovantes      | &#10003;  | &#10003; | X | &#10003;  | 10  | 10 | 10 | &#10003;  | &#10003; | 10 |
| CN012 - Visualizar ONGs             | &#10003;  | X | 10  | &#10003;  | 10  | 10 | 10  | &#10003;  | &#10003; | 10 |
| CN013 - Doar Medicamentos           | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 10 | 10 | &#10003; | &#10003; |  10 |
| CN014 - Doar Saúde Básica           | &#10003;  | &#10003; | &#10003; | &#10003; | 10  | 10 | 10 | &#10003; | &#10003; |  10 |

## CN001 - Coletar Ribon Diário

| | Justificativa |
|-| ------------- |
|2| Não descreve o objetivo em relação ao sistema (um exemplo: coletar presente diário para que se dõe; coletar para que se receba os bonus por dias consecutivos etc) |
|6| Poderia haver um detalhamento maior sobre, por exemplo, quantos ribons a mais se ganha ao frequentar o app diariamente. |
|11| Replico a ponderação acima. O modelo pecou ao não explicar suficientemente bem como funciona os bônus por acessos consecutivos.

## CN002 - Comprar Ribons

| | Justificativa |
|-| ------------- |
|2| Não descreve o objetivo em relação ao sistema (um exemplo: comprar ribons para doar para uma causa X) |

## CN003 - Convidar Amigos

| | Justificativa |
|-| ------------- |
| 2 | Não descreve o objetivo em relação ao sistema (um exemplo: convidar amigos para utilizarem o aplicativo; convidar amigos para ser bonificado com ribons; convidar amigos para fazer grupo de doações) |
| 3 | O contexto implica que o usuário deva estar logado para convidar amigos, o que não é verdade. |
| 6 | A segunda pós-condição implica que independentemente da conversão do convidado ou não, o usuário deve ser bonificado com 500 ribons, o que não é verdade. |
| 7 | Os episódios estão bem descritos, entretanto, há um excesso de utilização do termo "aplicativo", o que pode causar dúvidas em quem estiver lendo sobre quando é que o autor do documento está se referindo aos aplicativos externos (ex: whatsapp), onde o app Ribon será compartilhado, e o aplicativo Ribon em si. |
| 8 | Novamente, o autor implica que há de se ter uma conta para convidar amigos, o que não é verdade. |
| 10 | Com exceção dessa forçação múltiplas vezes referente à contas e redes sociais, o cenário é ajuda no entendimento do sistema em geral. |


## CN004 - Criar Conta

| | Justificativa |
|-| ------------- |
|6| Não há pós-condições. |
|7| Poderia-se destrinchar melhor cada opção de criação de conta (inclusive, em fluxos alternativos). Não há sensação de evolução no passo-a-passo. Além disso, é inverossímil, pois não é necessário nem ter email, nem conta Google e nem conta Facebook. Basta baixar o aplicativo e utilizar.|
|9| Pessoa não ter e-mail ou conta no Google/Facebook não é uma exceção. |
|10| Faltou esclarecer sobre o ponto acima sobre a questão 7, entretanto, a nota dada diz respeito ao elucidamento parcial provido pelo cenário no tocante às outras possibilidades de criação de conta (que não sejam simplesmente entrar no app.) |

## CN008 - Escolher Causa

| | Justificativa |
|-| ------------- |
|6| Não há pós-condições. |
|10| Embora não hajam pós-condições, o cenário explica bem como funciona o sistema de escolher causas para se doar |

## CN009 - Ler Histórias

| | Justificativa |
|-| ------------- |
|6| O texto implica que o usuário deve realizar todos os episódios para poder coletar os ribons, o que não é verdade.|
|9| Doação (e, doravante, sistema que realiza doações) não é inerente à leitura de histórias, logo, "falha no sistema que realiza doações" não é uma exceção válida. |

## CN010 - Ver Causas

| | Justificativa |
|-| ------------- |
|7| O último episódio não ficou muito claro (até por não ser verossímil) |

## CN011 - Verificar Comprovantes

| | Justificativa |
|-| ------------- |
|3| Esse provavelmente é o contexto de #Ler Histórias...|

## CN012 - Visualizar ONGs

| | Justificativa |
|-| ------------- |
|2| Não descreve o objetivo em relação ao sistema. |
