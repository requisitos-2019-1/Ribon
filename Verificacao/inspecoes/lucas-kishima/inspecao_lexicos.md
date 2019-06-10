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
| 9 - As noções explicam quem é o sujeito dentro daquele meio social? | alto | É um conceito de noção de sujeito | numérico |
| 10 - Os impactos mostram as ações aquele sujeito executa? | alto | É um conceito de impactos do sujeito no ambiente | numérico |

### Caso o léxico seja um verbo:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 9 - As noções explicam quem realiza aquela ação? | alto | É um conceito de noção de verbo | numérico |
| 10 - As noções explicam quando aquela relação acontece? | médio| Ajuda no entendimento daquela ação |numérico |
| 11 - As noções explicam quais os procedimentos envolvidos com aquele processo? | médio | Ajuda no entendimento daquela ação | numérico |
| 12 - Os impactos mostram os possíveis reflexos daquela ação no domínio em questão? | alto |É um dos conceitos de impacto| numérico |
| 13 - Caso os impactos causem uma mudança de estado essas mudanças foram identificadas corretamente? | média | Ajuda no entendimento dos impactos daquela ação  | numérico |

### Caso o léxico seja um objeto:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 9 - As noções definem o objeto?| alto | É um conceito de noção de estado | numérico |
| 10 - Caso o objeto se relacione com outros objetos, esses objetos foram identificados? | médio | ajuda no entendimento identificar com quais objetos ele se relaciona  | numérico |
| 11 - Os impactos relatam as possíveis ações que podem ser aplicadas à aquele objeto? | médio | ajuda a identificar ações que podem ser aplicadas ao objeto em questão. | numérico |

### Caso o léxico seja um estado:

| Questão | Impacto | Justificativa | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 9 - As noções mostram o que aquele estado significa no meio social analisado? | alto | É um conceito de noção de estado  | numérico |
| 10 - As noções indicam quais ações levaram ao estado em questão? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |
| 11 - Os impactos identificam outros estados possíveis? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |
| 12 - Os impactos identificam as possíveis ações que podem ocorrer a partir daquele estado? | médio | Ajuda no entendimento do estado mas não é de suma importância | numérico |

## Tabela
### Checklist


| Léxicos de sujeito | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ---- | - | - | - | - | - | - | - | - | - | - |
| LX009 - Comunidade | &#10003; | &#10003; | 10 | &#10003;| &#10003; |8|&#10003; | &#10003;|10 |-|
| LX012 - Evidence Action | &#10003; | &#10003; | 10 | &#10003; |x |- |&#10003; | &#10003;|10|10|
| LX017 - Living Goods | &#10003; | &#10003; | 10 | &#10003; |x |- |&#10003; |&#10003; |10 |10 |
| LX019 - ONG | &#10003; | &#10003; | 10 | &#10003; |&#10003; |10| &#10003;| &#10003;|10|10|
| LX020 - Patrocinador | &#10003; | &#10003; |10|&#10003;|&#10003;|10|&#10003; |&#10003; |10|10|
| LX025 - Project Healthy Children | &#10003; | &#10003; |10 |&#10003; | x | -|&#10003; |&#10003; |10 |10 |
| LX028 - Schistosomiasis Control Initiative | &#10003; | &#10003; | 10 | &#10003; | x | - |&#10003; |&#10003; |10 |10 |
| LX031 - Usuário | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 8 |&#10003; |&#10003; | 10| 10 |


| Léxicos de verbo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - | - |
| LX006 - Coletar | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 10 |&#10003; |&#10003; | 0|0 |0 |0 |0 |
| LX007 - Comprar | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 8 |&#10003; | &#10003;| 10|10 |0 |10 |10 |
| LX010 - Doar | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 10 | &#10003;|&#10003; |0 | 0 | 0 |10 | - |


| Léxicos de objeto| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| ---- | - | - | - | - | - | - | - | - | - | - | - |
| LX001 - Água Potável | &#10003; | &#10003; | 10 | &#10003; | &#10003;| 10 | &#10003;| &#10003; | &#10003;|x|6|
| LX002 - Aplicativo | &#10003; | &#10003;  | 8 | &#10003; | &#10003; |10|&#10003;|&#10003;|&#10003;|x|6|
| LX004 - Card | x | &#10003; | &#10003; |&#10003; | &#10003; |5|&#10003; |&#10003; |10|0|5|
| LX005 - Causa | &#10003; | &#10003; | 0 | &#10003; | &#10003; |5|&#10003; |&#10003; |0|10|10|
| LX008 - Comprovante de Doações | &#10003; | &#10003; | 10 | &#10003; | &#10003;  | 10 | &#10003; |&#10003; |10|10|10|
| LX011 - Doação | &#10003; | &#10003; | 0 | &#10003; |&#10003; |10|&#10003; |&#10003; |6|10|10|
| LX013 - Fortificação Alimentar | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 10 |&#10003; |&#10003; |10|10|10|
| LX014 - História | &#10003; | &#10003; | 10 | &#10003; |&#10003;  |10|&#10003; |&#10003; |10|-|10|
| LX018 - Medicamentos | &#10003; | &#10003; | 10 | &#10003; |&#10003;  |10 |&#10003; |&#10003; |10|10|10|
| LX022 - Presente Diário | &#10003; | &#10003; | 10 | &#10003; | &#10003;  | 10 |&#10003; |&#10003; |10|10|10|
| LX026 - Ribon | &#10003; | &#10003; | 10 | &#10003; | &#10003;  | 10 |&#10003; | &#10003;|10|10|10|
| LX029 - Smartphone | &#10003; | &#10003; | 0 | &#10003; | &#10003; | 10 |&#10003; |&#10003; |9|10|10|
| LX030 - Tutorial | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 10 |&#10003; |&#10003; |10|10|5|

| Léxicos de estado | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - |
| LX003 - Aplicativo não Funciona | &#10003; | x | 10 | &#10003; | &#10003;  | 10 | &#10003; |&#10003;|10|0|0|10|
| LX015 - História Coletada | &#10003; | &#10003; | 6 | &#10003; | &#10003; | 6 |&#10003; |&#10003; |&#10003;|10|10|0|5|
| LX016 - História Expirada | &#10003; | &#10003; | 8 | &#10003; | &#10003; | 10 |&#10003; |&#10003; |10|10|0|10|
| LX023 - Presente Diário Coletado | &#10003; | &#10003; | 10 | &#10003; | &#10003; | 8 | &#10003; |&#10003; |10|10|10|10|
| LX024 - Problemas com o Smartphone | &#10003; | &#10003; | 0 | &#10003; | &#10003; | 10 | &#10003;|&#10003; |0|10|0|10|

## LX001
| | Justificativa |
|-| ------------- |
|11| Um dos impactos seria o objeto é doado |

## LX002
| | Justificativa |
|-| ------------- |
|3| está um pouco mal escrita, o termo meio deve ser substituído |
|11| Faltam mais impactos |

## LX003
| | Justificativa |
|-| ------------- |
|2| Aplicativo não funciona não é um termo especial |

## LX004
| | Justificativa |
|-| ------------- |
|6| Apenas esse sinonimo, não ajuda muito no entendimento. |
|11|  Não foi relatado todas as possíveis ações.|


## LX005
| | Justificativa |
|-| ------------- |
|3| não é uma definição, as noções são apenas exemplos.|
|6| Ong não é um sinônimo de causa|

## LX007
| | Justificativa |
|-| ------------- |
|6| Poderia ter mais sinônimos. |

## LX009
| | Justificativa |
|-| ------------- |
|6| poderia ter mais sinonimos |
|11| explicação da definição não foi muito boa. |


## LX011
| | Justificativa |
|-| ------------- |
|3| não é uma definição clara , não explica bem o significado no léxico |


## LX014
| | Justificativa |
|-| ------------- |
|12| Falta a história não poder ser colhida novamente. |


## LX015
| | Justificativa |
|-| ------------- |
|3| poderia ter mais noções |
|6| poderia ter mais sinônimos |
|12| Falta a história não poder ser colhida novamente. |

## LX016
| | Justificativa |
|-| ------------- |
|3| esta boa, porém poderia ter mais noções. |

## LX023
| | Justificativa |
|-| ------------- |
|6| poderia ter mais sinônimos. |

## LX024
| | Justificativa |
|-| ------------- |
|3| não é bem uma definição, mas apenas exemplos dela.|

## LX028
| | Justificativa |
|-| ------------- |
|5| Apenas 2 das 10 contribuições estão corretas,não se deve utilizar contribuições OR, AND juntas com "++" |

## LX029
| | Justificativa |
|-| ------------- |
|3| deveria ter uma descrição bem parecida com a forma de um dicionário.|
|9| poderia ter sido escrito um pouco melhor |

## LX030
| | Justificativa |
|-| ------------- |
|11|  Faltam ações sobre o objeto |

## LX031
| | Justificativa |
|-| ------------- |
|6|  poderia ter mais sinônimos. |
|9|  não foram utilizados verbos de ações para descrever as operacionalizações. |


## Bibliografia
> https://aprender.ead.unb.br/pluginfile.php/348654/mod_resource/content/3/Requisitos%20-%20Aula%20010.pdf