# Justificativa Argumentação

## Questões

| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :----------------------: | :--: |
| 1 - A escrita das proposições está coerente? | Alto | O entendimento da argumentação é essencial para que se possa resolver de forma devida os conflitos  | Numérico |
| 2 - Todos os vértices possuem rótulo? | Alto | Em se tratando de um modelo essencialmente visual, a correta identificação dos elementos é muito necessária | Binário |
| 3 - A argumentação possui mais de uma inferência? | Alto | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 4 - A argumentação possui mais de um conflito? | Alto | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 5 - A argumentação possui mais de uma preferência? | Alto | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 6 - A escrita das inferências está coerente? | Médio | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes| Numérico |
| 7 - As inferências relacionam, no mínimo, duas proposições? | Alto | Não é permitido ter uma inferência de uma proposição p1 sem que isso resulte, ao menos, numa proposição p2 | Binário |
| 8 - Os conflitos relacionam, no mínimo, duas proposições? | Alto | Não é permitido ter um conflito de uma proposição p1 sem que haja uma proposição p2 contrária | Binário |
| 9 - A escrita dos conflitos está coerente? | Médio | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes | Numérico |
| 10 - Os conflitos possuem solução? | Alto | É o propósito da argumentação | Binário |
| 11 - Os conflitos entre preferências e conflitos também apontam para a proposição preferida? | Alto | O conflito que aponta para a proposição que perdeu é a única forma de saber o resultado do conflito | Binário |
| 12 - As preferências relacionam duas proposições? | Alto | Não é permitido ter uma preferência de uma proposição p1 sem que haja uma proposição p2 | Binário |
| 13 - A argumentação possui conclusão? | Alto | É o propósito do modelo | Binário |
| 14 - O fluxo de inferência, conflito, preferência e conclusão está certo? | Alto | É necessário que esteja sistematizadamente organizado de acordo com o modelo para que se possa extrair de forma flúida as informações do mesmo | Numérico |
| 15 - A argumentação possui rastreabilidade? | Alto |  | Binário |
| 16 - Chegou a conclusão de forma verbal? | Alto | | Binário |
| 17 - Mais de uma pessoa participou da discussão? | Alto | | Numérico |
| 18 - Outra discordância gerou um novo argumento? | Baixo | | Binário |
| 19 - O novo argumento gerou conflito com o argumento preferido? | Alto | | Binário |
| 20 - Os participantes chegaram a uma conclusão? | Alto | "Uma das principais metas da argumentação é a resolução de conflitos" (Rahwan, 2005) | Binário |


[Inspeção Henrique Martins](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/henrique-martins/inspecao_argumentacao.md)

[Inspeção Victor Rodrigues](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/victor-rodrigues/inspecao_argumentacao.md)


# Consenso de Notas

| Argumentações   |1|2       |3  |4  |5 |6 |7       |8       |9   |10      |11      |12      |13 |14 |15 |16 |17 |18 |19 |20      |
| -----------     |-|---     |---|---|--|--|---     |---     |--- |--      |---     |---     |---|---|---|---|---|---|---|---     |
|A001_RichPicture |5|&#10003;|0  |4  |0 |0 |x       |&#10003;|0   |&#10003;|&#10003;|&#10003;|&#10003;|10 |x  |x  |0  |x  |x  |&#10003;|
|A002_Empresarial |6|&#10003;|0  |0  |0 |0 |&#10003;|x       |0   |x       |x       |x       |&#10003;|10 |x  |x  |0  |x  |x  |&#10003;|
|A003_Investidores|5|&#10003;|0  |4  |0 |0 |x       |&#10003;|0   |&#10003;|&#10003;|&#10003;|x  |10 |x  |x  |0  |x  |x  |&#10003;|


# Consenso de Justificativas

## A001_RichPicture

| | Justificativa |
|-| ------------- |
|1| Apesar de ser possível o entendimento, o texto está confuso e com erros gramaticais |
|3| Não possui inferência |
|4| Apesar de terem dois conflitos, não são o bastante para uma boa argumentação |
|5| Possui apenas uma preferência |
|6| Não possui inferência |
|7| Não possui inferência |
|9| Não possui escrita |
|15| A argumentação possui apenas data, não sendo suficiente para ser considerado rastreabilidade |
|16| Não há conclusão verbal |
|17| Não existe rastreabilidade que comprove o fato |
|18| Não há mais de uma discordância |
|19| Não aplicavel, não houveram novos argumentos gerados |

## A002_Empresarial

| | Justificativa |
|-| ------------- |
|1| Proposição com erros de coesão e falta de informações |
|3| Possui apenas uma inferência |
|4| Não possui conflitos |
|5| Não possui preferência |
|6| Não possui escrita |
|8| Não possui conflitos |
|9| Não possui conflitos |
|10| Não possui conflitos |
|11| Não possui conflitos |
|12| Não possui preferência |
|15| A argumentação possui apenas data, não sendo suficiente para ser considerado rastreabilidade|
|16| Não há conclusão verbal |
|17| Não existe rastreabilidade que comprove o fato |
|18| Não há mais discordância |
|19| Não aplicavel, não houveram novos argumentos gerados |

## A003_Investidores

| | Justificativa |
|-| ------------- |
|1| Apesar de ser possível o entendimento, o texto está confuso e com erros gramaticais |
|3| Não possui inferência |
|4| Apesar de terem dois conflitos, não são o bastante para uma boa argumentação |
|5| Possui apenas uma preferência |
|6| Não possui inferência |
|7| Não possui inferência |
|9| Não possui escrita |
|15| A argumentação possui apenas data, não sendo suficiente para ser considerado rastreabilidade |
|16| Não há conclusão verbal |
|17| Não existe rastreabilidade que comprove o fato |
|18| Não há mais de uma discordância |
|19| Não aplicavel, não houveram novos argumentos gerados |