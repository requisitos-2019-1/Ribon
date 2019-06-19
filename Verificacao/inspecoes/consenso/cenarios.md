# Justificativas Cenários

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

Após a reunião, viu-se necessária a inclusão da pergunta 11: "O nome do cenário remete à uma funcionalidade? (por exemplo, poderia se tornar um botão?)" (Ex: "foi implementada a funcionalidade 'coletar ribon diário'")

<!-- &#10003; -->

| Cenários (Consenso)                 | 1*| 2*| 3*| 4*| 5 | 6 | 7 | 8*| 9*| 10 | 11 |
| ----------------------------------- | - | - | - | - | - | - | - | - | - | -- | -- |
| CN001 - Coletar Ribon Diário        | &#10003; |     X    | &#10003; |    X     |    10    |    8    |  7 |    X     |    X     | 8  | &#10003; |
| CN002 - Comprar Ribons              | &#10003; |     X    |     X    | &#10003; |    10    |    10   | 10 |    X     |    X     | 10 | &#10003; |
| CN003 - Convidar Amigos             | &#10003; |     X    |     X    | &#10003; |    10    |    5    | 8  |    X     |    X     | 6  | &#10003; |
| CN004 - Criar Conta                 | &#10003; |     X    | &#10003; | &#10003; |    10    |    0    | 0  |    X     |    X     | 5  | &#10003; |
| CN005 - Doar Fortificação Alimentar | &#10003; | &#10003; |     X    | &#10003; |    10    |    8    | 10 |    X     |    X     | 10 | &#10003; |
| CN006 - Doar Água Potável           | &#10003; | &#10003; |     X    | &#10003; |    10    |    8    | 10 |    X     |    X     | 10 | &#10003; |
| CN007 - Doar Ribons                 | &#10003; | &#10003; |     X    | &#10003; |    10    |    8    | 10 |    X     |    X     | 10 | &#10003; |
| CN008 - Escolher Causa              | &#10003; | &#10003; | &#10003; | &#10003; |    10    |    0    | 10 | &#10003; |    X     | 7  | &#10003; |
| CN009 - Ler Histórias               | &#10003; |     X    |     X    |     X    |    10    |    6    | 8  | &#10003; |    X     | 6  | X |
| CN010 - Ver Causas                  | &#10003; | &#10003; | &#10003; | &#10003; |    10    |    10   | 8  | &#10003; |    X     | 8  | &#10003; |
| CN011 - Verificar Comprovantes      | &#10003; | &#10003; |     X    | &#10003; |    10    |    10   | 8  | &#10003; |    X     | 9  | X |
| CN012 - Visualizar ONGs             | &#10003; |     X    | &#10003; | &#10003; |    10    |    10   | 9  | &#10003; |    X     | 9  | &#10003; |
| CN013 - Doar Medicamentos           | &#10003; | &#10003; |     X    | &#10003; |    10    |    8    | 10 |    X     |    X     | 10 | &#10003; |
| CN014 - Doar Saúde Básica           | &#10003; | &#10003; |     X    | &#10003; |    10    |    8    | 10 |    X     |    X     | 10 | &#10003; |

## Justificativas

| | Critérios |
|-| --------  |
|1| Foi analisado que todos os cenários atendem à esta pergunta |
|2| Percebeu-se um padrão dos cenários 1 até 4, onde os objetivos eram as réplicas das ações, sendo assim, os objetivos possuíam um fim em si mesmo, sem levar em conta nenhum objetivo a mais relacionado ao sistema. |
|3| <ul><li><b>Comprar Ribons:</b><li>O ideal seria substituir "possuir limite (...)" por "operadora aprovar compra"</li></li><li><b>Doações (em geral):</b><li>Deve-se adicionar, como pré-condição, que o usuário escolha qual causa irá doar.</li></li></ul> |
|4| <ul><li><b>Coletar Ribons Diários:</b><li>Ribon deveria ser um recurso</li></li><li><b>Ler Histórias:</b><li>História deveria ser um recurso não um ator</li></li></ul> |
|5| Todos estavam de acordo em relação à nota. |
|6| Os Cenário CN004,CN008 não possuem pós-condições |
|7| O cenário CN004 não possue episódios |
|8| Somente os cenários CN008,CN009,CN010,CN011,CN012 possuem restrições quem representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| Os cenários CN003,CN004,CN009 possuem falhas que dificultam o entendimento do sistema em geral |
|11|Os Cenários CN009, CN011 não são funcionalidades
