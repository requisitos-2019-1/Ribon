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
## Perguntas

| Questão | Impacto | Contexto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :------: | :----------------------: | :--: |
| 1 - A escrita das proposições está coerente? | Alto | | O entendimento da argumentação é essencial para que se possa resolver de forma devida os conflitos  | Numérico |
| 2 - Todos os vértices possuem rótulo? | Alto | | Em se tratando de um modelo essencialmente visual, a correta identificação dos elementos é muito necessária | Binário |
| 3 - A argumentação possui mais de uma inferência? | Alto | | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 4 - A argumentação possui mais de um conflito? | Alto | | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 5 - A argumentação possui mais de uma preferência? | Alto | | Para que seja um modelo de alta qualidade, é importante que possua muitas camadas | Numérico |
| 6 - A escrita das inferências está coerente? | Médio | | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes| Numérico |
| 7 - As inferências relacionam, no mínimo, duas proposições? | Alto | | Não é permitido ter uma inferência de uma proposição p1 sem que isso resulte, ao menos, numa proposição p2 | Binário |
| 8 - Os conflitos relacionam, no mínimo, duas proposições? | Alto | | Não é permitido ter um conflito de uma proposição p1 sem que haja uma proposição p2 contrária | Binário |
| 9 - A escrita dos conflitos está coerente? | Médio | | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes | Numérico |
| 10 - Os conflitos possuem solução? | Alto | | É o propósito da argumentação | Binário |
| 11 - Os conflitos entre preferências e conflitos também apontam para a proposição preferida? | Alto | | O conflito que aponta para a proposição que perdeu é a única forma de saber o resultado do conflito | Binário |
| 12 - As preferências relacionam duas proposições? | Alto | | Não é permitido ter uma preferência de uma proposição p1 sem que haja uma proposição p2 | Binário |
| 13 - A argumentação possui conclusão? | Alto | | É o propósito do modelo | Binário |
| 14 - O fluxo de inferência, conflito, preferência e conclusão está certo? | Alto | | É necessário que esteja sistematizadamente organizado de acordo com o modelo para que se possa extrair de forma flúida as informações do mesmo | Numérico |
| 15 - A argumentação possui rastreabilidade? | Alto | |  | Binário |
| 16 - Chegou a conclusão de forma verbal | Alto | | | Binário |
| 17 - Mais de uma pessoa participou da discussão | Alto | | | Numérico |
| 18 - Outra discordância gerou um novo argumento | Baixo | | | Binário |
| 19 - O novo argumento gerou conflito com o argumento preferido | Alto | | | Binário |
| 20 - Os participantes chegaram a uma conclusão | Alto | "Uma das principais metas da argumentação é a resolução de conflitos" (Rahwan, 2005) | | Binário |

## Tabela
### Checklist
<!-- &#10003; -->
| Argumentação      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| ----------------- | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| A001_RichPicture  |   | <!-- &#10003; -->  |   |   |   |   | <!-- &#10003; -->  | <!-- &#10003; -->  |   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |  
| A002_Empresarial  |   | <!-- &#10003; -->  |   |   |   |   | <!-- &#10003; -->  | <!-- &#10003; -->  |   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |  
| A003_Investidores |   | <!-- &#10003; -->  |   |   |   |   | <!-- &#10003; -->  | <!-- &#10003; -->  |   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   |    | <!-- &#10003; -->   | <!-- &#10003; -->   | <!-- &#10003; -->   |  
### Relevâncias

| Artefato | Ranking |
| -------- | :-----: |
| A001_RichPicture | <li>Ponto 1</li><br/><li>Ponto 2</li> | 
| A002_Empresarial | <li>Ponto 1</li><br/><li>Ponto 2</li> | 
| A003_Investidores | <li>Ponto 1</li><br/><li>Ponto 2</li> |
### Verificação
#### Glossário

| expressão | significado |
| --- | --- |
| & | se refere aos artefatos |
| # | se refere às perguntas |
| &todos | todos os artefatos foram analisados |
| #todas | todas as perguntas foram analisadas |
| &1..3  | todos os artefatos de 1 até 3 foram analisados |
| #1..8 | todas as perguntas de 1 até 8 foram analisadas |

#### Auditoria V1
| Auditor | &Artefato (#Perguntas) |
| --- | --- |
| Henrique | &Richpicture (#todas) | &Investidores (#1..3) | 
| Guilherme | &Investidores (#1..3) |

#### Auditoria V2
| Auditor | Artefato | Perguntas |
| --- | --- | --- |
| Henrique | Richpicture | todas |
| Henrique | Investidores | 1, 2, 3 |
| Guilherme | Investidores | 1, 2, 3 |

#### Auditoria V3
| Artefato     | Auditor (#Perguntas, Data) |
| ------------ | ------- |
| Richpicture  | Henrique (#todas, 31/05/2019) |
| Investidores | Henrique (#1..3, 31/02/2019) <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(#5..8, 35/02/2019)<br />Guilherme (#1..3, 31/02/2019) |

## Qualidade do Modelo

### Critérios de qualidade:
 - Reprovação em no máximo um critério - <b>Qualidade Alta</b>
 - Reprovação em 2 ou 5 critérios - <b>Qualidade Média</b>
 - Reprovação em mais de 5 critérios - <b>Qualidade Baixa</b>

 ## Análise dos Modelos:

 ### Qualidade Baixa
  - <b>Argumentação RichPicture</b>
    - A argumentação não possui inferências
    - A argumentação possui apenas uma preferência
    - A argumentação não possui rastreabilidade

  - <b>Argumentação Empresarial</b>
    - A argumentação possui apenas uma inferência
    - A argumentação não possui conflitos
    - A argumentação não possui preferência
    - A argumentação não possui rastreabilidade

  - <b>Argumentação Investidores</b>
    - A argumentação não possui inferências
    - A argumentação possui apenas uma preferência
    - A argumentação não possui rastreabilidade

 ### Qualidade Média
  - Não houve argumentação com número de reprovações entre 2 e 5.

 ### Qualidade Alta
  - Não houve argumentação com 1 reprovação ou menos

## Números:																																														
|   | Resultado |
| - | :---------: |
| Número de argumentações: | |
| Total de indicadores (Argumentações x Perguntas): |	|
| Taxa de erro de perguntas  (Σ Erros / Total de indicadores): |	 |
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
> https://aprender.ead.unb.br/pluginfile.php/348647/mod_resource/content/3/Requisitos%20-%20Aula%2004.pdf