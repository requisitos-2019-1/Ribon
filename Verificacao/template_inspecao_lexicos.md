| Data | Versão | Descrição | Autor |
| - | - | - | - |
| 31/05/2019 | 1.0 | Template Inicial | Henrique Martins |
| 05/01/2019 | 1.1 | Incrementando template com impacto de perguntas e Resultados numéricos | Guilherme de Lyra |
| 05/01/2019 | 1.2 | Incrementando template com contexto, justificativa e tipo (para perguntas)<br />tabela de relevâncias<br />tabela de validação geral<br />e adição de bibliografia | Guilherme de Lyra |
| 09/05/2019 | 1.3 | Removendo perguntas que não agregam valor a verificação | Lucas kishima |
| 09/05/2019 | 1.4 | Melhorando perguntas | Lucas kishima |
| 09/05/2019 | 1.5 | Adicionando perguntas gerais | Lucas kishima |
| 09/05/2019 | 1.6 | Adicionando perguntas específicas | Lucas kishima |

# Verificação - Inspeção [Léxicos](https://github.com/requisitos-2019-1/Ribon/wiki/L%C3%A9xicos)

## Perguntas gerais:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 -De maneira geral, o léxico sozinho, é capaz de explicar o termo para uma pessoa que não faz parte do universo em questão?| Alto | Pois é um dos objetivos da modelagem | Binário |
| 2 - O léxico foi identificado corretamente, ou seja, ele é uma palavra com significado especial no universo do domínio?| Alto |  Por definição o léxico deve ser uma palavra importante naquele meio social | Binário |
| 3 - A noção é uma definição clara do léxico, ou seja, ela é capaz de explicar o significado daquele léxico no domínio analisado? | Alto | Pois é o objetivo principal da noção | numérico |
| 4 - O tipo do léxico foi classificado corretamente? | Alto | O tipo do léxico influencia completamente no entendimento do leitor | Binário |
| 5 - Foram identificados sinônimos para o léxico?| alto | É um dos conceitos propostos pelo modelo | Binário |
| 6 - Os sinônimos identificados ajudam o leitor a entender o significado daquele léxico? | alto | Os sinonimos identificados devem ser condizentes com o léxico. | Numérico |
| 7 - O léxico possui código identificador único?  | médio | Ajuda na rastreabilidade | Binário |
| 8 - O léxico possui links para outros léxicos que interage? | médio | Ajuda na rastreabilidade e também ajuda o leitor a entender as possíveis conexões entre os léxicos | Binário |


## Perguntas específicas:
De acordo com o tipo do léxico foram identificadas diferentes fatores que influenciam na qualidade do mesmo. Tendo em vista que as perguntas tragam resultados mais positivos para a verificação, foram utilizados fluxos alternativos de perguntas para cada tipo específico de léxico, o auditor responsável pela execução das mesmas deve escolher apenas um deles.


### Caso o léxico seja um sujeito:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| S1 - As noções explicam quem é o sujeito dentro daquele meio social? | alto | É um conceito de noção de sujeito | numérico |
| S2 - Os impactos mostram as ações aquele sujeito executa? | alto | É um conceito de impactos do sujeito no ambiente | numérico |

### Caso o léxico seja um verbo:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| V1 - As noções explicam quem realiza aquela ação? | alto | É um conceito de noção de verbo | numérico |
| V2 - As noções explicam quando aquela relação acontece? | médio| Ajuda no entendimento daquela ação |numérico |
| V3 - As noções explicam quais os procedimentos envolvidos com aquele processo? | médio | Ajuda no entendimento daquela ação | numérico |
| V4 - Os impactos mostram os possíveis reflexos daquela ação no domínio em questão? | alto |É um dos conceitos de impacto| numérico |
| V5 - Caso os impactos causem uma mudança de estado essas mudanças foram identificadas corretamente? | média | Ajuda no entendimento dos impactos daquela ação  | numérico |

### Caso o léxico seja um objeto:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| O1 - As noções definem o objeto?| alto | É um conceito de noção de estado | numérico |
| O2 - Caso o objeto se relacione com outros objetos, esses objetos foram identificados? | médio | ajuda no entendimento identificar com quais objetos ele se relaciona  | numérico |
| O3 - Os impactos relatam as possíveis ações que podem ser aplicadas à aquele objeto? | médio | ajuda a identificar ações que podem ser aplicadas ao objeto em questão. | numérico |

### Caso o léxico seja um estado:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| E1 - As noções mostram o que aquele estado significa no meio social analisado? | alto | É um conceito de noção de estado  | numérico |
| E2 - As noções indicam quais ações levaram ao estado em questão? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |
| E3 - Os impactos identificam outros estados possíveis? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |
| E4 - Os impactos identificam as possíveis ações que podem ocorrer a partir daquele estado? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |

## Tabela
### Checklist


| Léxicos de sujeito | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ---- | - | - | - | - | - | - | - | - | - | - |
| LX009 - Comunidade |  |  |  |  | | | | | | |
| LX012 - Evidence Action |  |  |  |  | | | | | | |
| LX013 - Fortificação Alimentar |  |  |  |  | | | | | | |
| LX017 - Living Goods |  |  |  |  | | | | | | |
| LX019 - ONG |  |  |  |  | | | | | | |
| LX020 - Patrocinador |  |  |  |  | | | | | | |
| LX025 - Project Healthy Children |  |  |  |  | | | | | | |
| LX028 - Schistosomiasis Control Initiative |  |  |  |  | | | | | | |
| LX031 - Usuário |  |  |  |  | | | | | | |


| Léxicos de verbo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - | - |
| LX006 - Coletar |  |  |  |  | | | | | | | | | |
| LX007 - Comprar |  |  |  |  | | | | | | | | | |
| LX010 - Doar |  |  |  |  | | | | | | | | | |


| Léxicos de objeto| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| ---- | - | - | - | - | - | - | - | - | - | - | - |
| LX001 - Água Potável |  |  |  |  | | | | ||||
| LX002 - Aplicativo |  |  |  |  |  | | | ||||
| LX003 - Aplicativo não Funciona |  |  |  |  |  | | | ||||
| LX004 - Card |  |  |  |  | | | | ||||
| LX005 - Causa |  |  |  |  | | | | ||||
| LX008 - Comprovante de Doações |  |  |  |  | | | | ||||
| LX011 - Doação |  |  |  |  | | | | ||||
| LX013 - Fortificação Alimentar |  |  |  |  | | | | ||||
| LX014 - História |  |  |  |  | | | | ||||
| LX018 - Medicamentos |  |  |  |  | | | | ||||
| LX022 - Presente Diário |  |  |  |  | | | | ||||
| LX026 - Ribon |  |  |  |  | | | | ||||
| LX029 - Smartphone |  |  |  |  | | | | ||||
| LX030 - Tutorial |  |  |  |  | | | | ||||

| Léxicos de estado | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - |
| LX003 - Aplicativo não Funciona |  |  |  |  |  | | | |||||
| LX015 - História Coletada |  |  |  |  | | | | |||||
| LX016 - História Expirada |  |  |  |  | | | | |||||
| LX023 - Presente Diário Coletado |  |  |  |  | | | | |||||
| LX024 - Problemas com o Smartphone |  |  |  |  | | | | |||||


## Bibliografia
> https://aprender.ead.unb.br/pluginfile.php/348654/mod_resource/content/3/Requisitos%20-%20Aula%20010.pdf
