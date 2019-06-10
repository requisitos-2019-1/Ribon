# Justificativas - Cenários
# AUDITOR: Henrique Martins


| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 - O título do cenário indica uma ação? | Alto | Regra do modelo | Binário |
| 2 - O objetivo descreve a finalidade do cenário, em relação ao sistema? | Alto | Regra do modelo | Binário |
| 3 - O contexto/pré-condições descreve o que deva ter sido atingido previamente para que se realize o objetivo proposto pelo cenário atual, sem espaço para dúvidas? | Alto | Regra do modelo | Binário |
| 4 - A lista de recursos realmente descrevem todos os recursos necessários para se atingir o objetivo do cenário? | Alto | Regra do modelo | Binário |
| 5 - Os termos específicos estão linkados com léxicos? | Médio | A linkagem facilita o acesso à um maior entendimento, ou esclarecimento, sobre o termo em questão | Numérico |
| 6 - As pós-condições explicam detalhadamente o que ocorre após os episódios se encerrarem? | Alto | Regra do modelo | Numérico |
| 7 - Os episódios são claros o suficiente para não deixarem dúvidas, e estão de acordo com o funcionamento real do produto | Alto | É importante que seja claro para o desenvolvedor conseguir seguir os passo-a-passos sem ter indagações internas (o que pode resultar em tomadas de decisões que não acordem com o que se esperava daquela feature)  | Numérico |
| 8 - As restrições representam requisitos que devem ser cumpridos para o cenário ocorrer? | Alto | Regra do modelo | Binário |
| 9 - As exceções representam alguma situação que atrapalha o usuário de atingir o objetivo inicial? | Alto | Regra do modelo | Binário |
| 10 - O cenário ajuda no entendimento do sistema em geral ou de alguma funcionalidade em específico? | Alto | Finalidade do modelo | Numérico |

| Cenários (Henrique)                 | 1*| 2*| 3*| 4*| 5 | 6 | 7 | 8*| 9*| 10 |
| ----------------------------------- | - | - | - | - | - | - | - | - | - | -- |
| CN001 - Coletar Ribon Diário        | &#10003; | x | x | &#10003; | 10 | 10 | 7 | x | &#10003; | 8 | 
| CN002 - Comprar Ribons              | &#10003; | x | &#10003; | &#10003; | 10 | 10 | 10 | x | &#10003; | 10 | 
| CN003 - Convidar Amigos             | &#10003; | x | x | &#10003; | 10 | 10 | 6 | x | &#10003; | 10 | 
| CN004 - Criar Conta                 | &#10003; | x | &#10003; | &#10003; | 10 | 0 | 5 | &#10003; | &#10003; | 8 | 
| CN005 - Doar Fortificação Alimentar | &#10003; | x | x | &#10003; | 10 | 10 | 10 | x | &#10003; | 10 | 
| CN006 - Doar Água Potável           | &#10003; | x | x | &#10003; | 10 | 10 | 10  | x | &#10003; | 10 | 
| CN007 - Doar Ribons                 | &#10003; | x | &#10003; | &#10003; | 10 | 10 | 10 | x | &#10003; | 10 | 
| CN008 - Escolher Causa              | &#10003; | x | x | &#10003; | 10 | 0 | 10 | &#10003; | &#10003; | 8 | 
| CN009 - Ler Histórias               | &#10003; | x | x | &#10003; | 10 | 10 | 10 | &#10003; | &#10003; | 10 | 
| CN010 - Ver Causas                  | &#10003; | x | &#10003; | &#10003; | 10 | 10 | 10 | &#10003; | &#10003; | 10 | 
| CN011 - Verificar Comprovantes      | &#10003; | x | x | &#10003; | 10 | 10 | 6 | &#10003; | &#10003; | 10 | 
| CN012 - Visualizar ONGs             | &#10003; | x | x | &#10003; | 10 | 10 | 10 | &#10003; | &#10003; | 10 | 
| CN013 - Doar Medicamentos           | &#10003; | x | x | &#10003; | 10 | 10 | 10 | x | &#10003; | 10 | 
| CN014 - Doar Saúde Básica           | &#10003; | x | x | &#10003; | 10 | 10 | 10 | x | &#10003; | 10 | 

## CN001 - Coletar Ribon Diário

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O que está escrito no contexto não é verdade |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| O conjunto de episódios não é claro o suficiente, podendo acarretar em dúvidas |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário poderia ter episódios mais bem escritos |


## CN002 - Comprar Ribons

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O contexto respeita a regra de de descrição |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN003 - Convidar Amigos

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos, além do último não ser verdade |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| O episódio "Usuário puxa a tela para cima" está atribuindo uma obrigação ao aplicativo, o que não é permitido |
|8| A última restrição não representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN004 - Criar Conta

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O contexto respeita a regra de de descrição |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Não possui pós-condições |
|7| Os episódios não condizem com a realidade do aplicativo |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| Os episódios não condizem com a realidade do aplicativo, afetando o entendimento do mesmo |


## CN005 - Doar Fortificação Alimentar

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN006 - Doar Água Potável

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN007 - Doar Ribons

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O contexto respeita a regra de de descrição |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN008 - Escolher Causa

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Não possui pós-condições |
|7| Os episódios estão detalhados e claros |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário poderia ter episódios mais bem escritos |


## CN009 - Ler Histórias

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN010 - Ver Causas

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O contexto respeita a regra de de descrição |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN011 - Verificar Comprovantes

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| O que está escrito no contexto não é verdade |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| O episódio "Usuário puxa a tela para cima" está atribuindo uma obrigação ao aplicativo, o que não é permitido |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN012 - Visualizar ONGs

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Todas as restrições representam requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN013 - Doar Medicamentos

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |


## CN014 - Doar Saúde Básica

| | Justificativa |
|-| ------------- |
|1| O título respeita a regra de indicar uma ação |
|2| O objetivo não descreve em relação ao sistema |
|3| Nem todos os contextos/pré-condições estão escritos |
|4| Todos os recursos necessários foram listados |
|5| Todos os termos estão linkados com os léxicos  |
|6| Todas as pós-condições explicam detalhadamente o que dever ocorrer em seguida |
|7| Os episódios estão detalhados e claros |
|8| Nenhuma das restrições representa requisitos necessários para a ocorrência do cenário |
|9| Todas as exceções respeitam a regra |
|10| O cenário ajuda no entendimento do sistema em geral |
