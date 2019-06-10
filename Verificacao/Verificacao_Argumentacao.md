| Data | Versão | Descrição | Autor |
| ---- | - | - | - |
| 31/05/2019 | 1.0 | Template Inicial | Henrique Martins |
| 31/05/2019 | 1.1 | Criação da Verificação de Argumentação | Henrique Martins |
| 05/01/2019 | 1.2 | Incrementando template com impacto de perguntas e Resultados numéricos | Guilherme de Lyra |
| 05/01/2019 | 1.3 | Incrementando template com contexto, justificativa e tipo (para perguntas)<br />tabela de relevâncias<br />tabela de validação geral<br />e adição de bibliografia | Guilherme de Lyra |
| 05/01/2019 | 1.4 | Adicionando mais perguntas (baseadas no grupo [Pinterest](http://www.joberth-rogers.ml/2018.2-Requisitos-Pinterest/pre_rastreabilidade_analise/)) |
| 06/01/2019 | 1.5 | Refinando perguntas, adicionando tipos e tabelas de verificação | Henrique Martins, Guilherme de Lyra, Victor Rodrigues |
| 06/01/2019 | 1.6 | Adicionando impactos das perguntas, e justificando-os | Henrique Martins, Guilherme de Lyra |
# Verificação - Inspeção [Argumentação](https://github.com/requisitos-2019-1/Ribon/wiki/Argumenta%C3%A7%C3%A3o)

## Questões Avaliadoras

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
| 15 - A argumentação possui rastreabilidade? | Alto | A rastreabilidade é necessária para que se possa guardar informações importantes sobre a argumentação | Binário |
| 16 - Chegou a conclusão de forma verbal? | Alto | A conclusão verbal auxilia no entendimento da argumentação| Binário |
| 17 - Mais de uma pessoa participou da discussão? | Alto | Para que uma argumentação seja de qualidade, é preciso muitas pessoas | Numérico |
| 18 - Outra discordância gerou um novo argumento? | Baixo | Boa prática | Binário |
| 19 - O novo argumento gerou conflito com o argumento preferido? | Alto | Boa prática | Binário |
| 20 - Os participantes chegaram a uma conclusão? | Alto | "Uma das principais metas da argumentação é a resolução de conflitos" (Rahwan, 2005) | Binário |

Obs: Perguntas binárias implicam em nota 0 ou 10

## Auditorias Realizadas

[Inspeção - Henrique Martins](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/henrique-martins/inspecao_argumentacao.md)<br>
[Inspeção - Victor Rodrigues](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/victor-rodrigues/inspecao_argumentacao.md)


## Consenso das Avaliações
Obs: "*" indica que pergunta é binária

| Argumentações | 1 | 2      | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11     | 12     | 13     | 14  | 15  | 16  | 17  | 18  | 19  | 20     |
| -------------------   | - | ---    | --- | --- | --- | --- | --- | --- | --- | --- | ---    | ---    | ---    | --- | --- | --- | --- | --- | --- | ---    |
| A001_RichPicture      | 6 |&#10003;| 0   | 4   | 0   | x | 0   | 7   | x | 6   |&#10003;|&#10003;|&#10003;|10   | 4   | x | 5   | x | x |&#10003;|
| A002_Empresarial      | 4 |&#10003;| 3   | 0   | 0   | x | 6   | 0   | x | 0   | x    | x    |&#10003;|10   | 4   | x | 5   | x | x |&#10003;|
| A003_Investidores     | 5 |&#10003;| 0   | 4   | 0   | x | 0   | 7   | x | 6   |&#10003;|&#10003;|&#10003;|10   | 4   | x | 5   | x | x |&#10003;|

[Justificativas - Consenso](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/consenso/argumentacao.md)

## Números:																		
|   | Resultado |
| - | :---------: |
| Número de argumentações: | 3 |
| Total de indicadores (Argumentações x Perguntas): | 60 |
| Taxa de erro de perguntas  (Σ Erros / Total de indicadores): |	 |
| Total de pontos de erro com impacto<br /> (Σ Erros/ (questão alta *3) + (questão média *2) + (questão baixa *1)):| |

## Léxicos importantes identificados:
- [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)
- [Patrocinador](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX020_Patrocinador.md)


## Validação Geral:
| Artefato | Nota Geral | Menção | Resultado |
| -------- | :--------: | :----: | :-------: |
| A001_Richpicture | 4.6 | MI | Reprovado |
| A002_Empresarial | 3.1 | MI | Reprovado |
| A003_Investidores | 4.55 | MI | Reprovado |

## Bibliografia
> [Requisitos - Aula 04 (Maurício Serrano e Milene Serrano)](https://aprender.ead.unb.br/pluginfile.php/348647/mod_resource/content/3/Requisitos%20-%20Aula%2004.pdf)