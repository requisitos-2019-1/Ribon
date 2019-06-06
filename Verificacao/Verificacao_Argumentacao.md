| Data | Versão | Descrição | Autor |
| ---- | - | - | - |
| 31/05/2019 | 1.0 | Template Inicial | Henrique Martins |
| 31/05/2019 | 1.1 | Criação da Verificação de Argumentação | Henrique Martins |
| 05/01/2019 | 1.2 | Incrementando template com impacto de perguntas e Resultados numéricos | Guilherme de Lyra |
| 05/01/2019 | 1.3 | Incrementando template com contexto, justificativa e tipo (para perguntas)<br />tabela de relevâncias<br />tabela de validação geral<br />e adição de bibliografia | Guilherme de Lyra |
| 05/01/2019 | 1.4 | Adicionando mais perguntas (baseadas no grupo [Pinterest](http://www.joberth-rogers.ml/2018.2-Requisitos-Pinterest/pre_rastreabilidade_analise/))


# Verificação - Inspeção [Argumentação](https://github.com/requisitos-2019-1/Ribon/wiki/Argumenta%C3%A7%C3%A3o)
## Perguntas

| Questão | Impacto | Contexto | Justificativa | Tipo |
| ------- | :-----: | :------: | :-----------: | :--: |
| 1 - A escrita das proposições está coerente? | alto/médio/baixo | | | |
| 2 - Todos os vértices possuem rótulo? | alto/médio/baixo | | | |
| 3 - A argumentação possui mais de uma inferência? | alto/médio/baixo | | | |
| 4 - A argumentação possui mais de um conflito? | alto/médio/baixo | | | |
| 5 - A argumentação possui mais de uma preferência? | alto/médio/baixo | | | |
| 6 - A escrita das inferências está coerente? | alto/médio/baixo | | | |
| 7 - As inferências relacionam, no mínimo, duas proposições? | alto/médio/baixo | | | |
| 8 - Os conflitos relacionam, no mínimo, duas proposições? | alto/médio/baixo | | | |
| 9 - A escrita dos conflitos está coerente? | alto/médio/baixo | | | |
| 10 - Os conflitos possuem solução? | alto/médio/baixo | | | |
| 11 - Os conflitos entre preferências e conflitos também apontam para a proposição preferida? | alto/médio/baixo | | | |
| 12 - As preferências relacionam duas proposições? | alto/médio/baixo | | | |
| 13 - A argumentação possui conclusão? | alto/médio/baixo | | | |
| 14 - O fluxo de inferência, conflito, preferência e conclusão está certo? | alto/médio/baixo | | | |
| 15 - A argumentação possui rastreabilidade? | alto/médio/baixo | | | |
| 16 - Chegou a conclusão de forma verbal | Alta | | | |
| 17 - Mais de uma pessoa participou da discussão | Alta | | | |
| 18 - Teve uma inferência de argumentos | Alta | | | |
| 19 - Argumentos diferentes geraram conflitos | Alta | | | |
| 20 - Chegou-se a uma preferência para um dos argumentos | Alta | | | |
| 21 - Outra discordância gerou um novo argumento | Baixa | | | |
| 22 - O novo argumento gerou conflito com o argumento preferido | Alta | | | |
| 23 - Os participantes chegaram a uma conclusão | Alta | | | |

## Tabela
### Checklist

| Argumentação | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| RichPicture | &#10003; | &#10003; |   | &#10003; |   |   |   | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |  |  |
| Empresarial | &#10003; | &#10003; |   |   |   | &#10003; | &#10003; |   |   |   |   |   | &#10003; |   |  |
| Investidores | &#10003; | &#10003; |   | &#10003; |   |   |   | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |   |  |

### Relevâncias

| Artefato | Ranking |
| -------- | :-----: |
| A01 | <li>Ponto 1</li><br/><li>Ponto 2</li> | 
| A02 | <li>Ponto 1</li><br/><li>Ponto 2</li> | 

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