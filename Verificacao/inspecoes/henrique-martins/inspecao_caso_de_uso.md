# Justificativas - Casos de Uso
# AUDITOR: Henrique Martins


| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :----------------------: | :--: |
| 1. O nome do ator revela seu papel no sistema? | Alto | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes | Binário |
| 2. Os nomes dos casos de uso são construidas em voz ativa, e utilizam o tempo presente?<br />(ex.: "Sistema valida a quantia informada" em vez de "A quantia informada deve ser validada pelo sistema"). | Alto | Regra do modelo | Binário |
| 3. O nome do caso de uso é de fácil compreensão? | Médio | É importante clareza para se entender a abstração geral sobre o caso de uso | Numérico |
| 4. Quando ocorre relacionamentos entre casos de usos, estes relacionamentos são:<br />Relacionamento de Inclusão ,<br />Relacionamento de Extensão ,<br />Relacionamento de Generalização? | Alto | Regra do modelo | Binário |
| 5. No diagrama, ao menos um caso de uso se relaciona com um ator? | Alto | Regra do modelo | Binário |
| 6. Nos relacionamentos de inclusão, o caso base é incompleto sem o caso que está sendo incluído? | Alto | Regra do Modelo | Binário |
| 7. Nos relacionamentos de extensão, o caso extendido (ou, caso base) é completo por si só? | Alto | Regra do modelo | Binário |
| 8. Nos relacionamentos de generalização, este é usado para funcionalidades que foram re-usadas? | Alto | Regra do modelo | Binário |
| 9. Possui descrição dos atores? | Baixo | Informações extras que possam ajudar a elucidar são bem-quistas | Binário |
| 10. Possui descrição dos casos de usos, com o fluxo<br />principal e os alternativos descritos? | Alto | O objetivo, num documento completo, é que se haja no mínimo 3 cenários (podendo-se [estender para até 5](https://hientl.files.wordpress.com/2011/12/tnyc_discovering-require.pdf), página 120): <li>O caminho padrão para se atingir o objetivo</li><li>Fluxos alternativos</li><li>Fluxos de exceção (que podem ou não ser recuperados)</li><br />Sendo assim, não é exatamente uma regra do modelo, mas uma boa prática necessária | Numérico |
| 11. A descrição de caso de uso é a de um caso de uso representado no diagrama? | Alto | Regra do Modelo | Binário |
| 12. São evitados termos sem quantificação precisa, como "muito", "pouco", "adequado", "claro", "fácil" "longo" "curto", "rápido" "etc"? | Médio | Casos de uso são, via de regra, orientados à elementos mensuráveis | Numérica |
| 13. São evitados termos que indicam opção, como "possivelmente", "alternativamente", "no caso", "se", etc, sem especificar um fluxo alternativo? | Médio | Os casos de uso hão de ser concretos, e suas variações condicionais devem se tornar outros casos de uso | Numérico |
| 14. Os termos passiveis de mais de uma interpretação constam em glossário, com clara definição? | Alto | Auxilia no entendimento, sendo, portanto, uma boa prática necessária. | Numérico |
| 15. Uma vez utilizado um termo, ele é mantido para referenciar-se ao mesmo elemento? | Baixo | Para evitar interpretações dúbias | Numérico |
| 16. São evitados termos que indicam a prematura especificação de interface, tais como "checar", "botão" etc? | Médio | É importante não entrar numa operacionalização excessiva já que foge um pouco do propósito do diagrama | Numérico |
| 17. As funcionalidades se restringem ao quê o sistema deve fazer e não em como, evitando a definição explicita de código na especificação? | Médio | Boa prática, pois evita operacionalização excessiva | Binário |
| 18. A descrição evita requisitos de negócio sem ação direta ao sistema? | Médio | Normalmente regras de negócio implicam em requisitos não-funcionais, e estes últimos não têm espaço no modelo. <br/> Logo, normalmente, é uma questão de regra de modelo. | Binário |
| 19. Os nomes dos casos de uso são numeradas para que possibilitem a rastreabilidade? | Médio | Boa prática | Binário |
| 20. Os nomes dos casos de uso procuram ser objetivas, evitando redundâncias ou presença de informações evidentemente desnecessárias? | Baixo | Boa prática | Numérico |

| Casos de Uso | 1*| 2*| 3 | 4*| 5*| 6*| 7*| 8*| 9*| 10 | 11*| 12 | 13 | 14 | 15 | 16 | 17*| 18*| 19*| 20 |
| ------------ | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|     UC001    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC002    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC003    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC004    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC005    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC006    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC007    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC008    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC009    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC010    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC011    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC012    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC013    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC014    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC015    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC016    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC018    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC019    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC020    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC021    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC022    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC023    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC024    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC025    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC026    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |
|     UC027    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC028    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 10 | &#10003; | &#10003; | &#10003; | 10 |
|     UC029    | &#10003; | x | 10 | &#10003; | &#10003; | &#10003; | &#10003; | &#10003; | x | 10 |  &#10003; | 10 | 10 | 10 | 10 | 7 | x | &#10003; | &#10003; | 10 |

## UC001

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC002

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC003

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC004

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o card" na descrição, o que não é permitido |
|17| Possui "seleciona o card" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC005

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o card" na descrição, o que não é permitido |
|17| Possui "seleciona o card" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC006

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o card" na descrição, o que não é permitido |
|17| Possui "seleciona o card" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC007

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| O caso de uso não extende nenhum outro caso, portanto essa regra não foi desrespeitada |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o card" na descrição, o que não é permitido |
|17| Possui "seleciona o card" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC008

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC009

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC010

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC011

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Não há nenhum relacionamento de inclusão, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC012

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC013

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "clica no botão" na descrição, o que não é permitido |
|17| Possui "clica no botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC014

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC015

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "clica no nome" na descrição, o que não é permitido |
|17| Possui "clica no nome" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC016

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| O caso de uso não inclui nenhum outro caso, portanto essa regra não foi desrespeitada |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "clica no botão" na descrição, o que não é permitido |
|17| Possui "clica no botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC018

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC019

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "clica em algum dos comprovantes" na descrição, o que não é permitido |
|17| Possui "clica em algum dos comprovantes", dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC020

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC021

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC022

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC023

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC024

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "identifica o ícone" na descrição, o que não é permitido |
|17| Possui "identifica o ícone" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC025

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC026

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC027

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC028

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Os termos não permitidos são evitados |
|17| As funcionalidades se restringem ao quê o sistema deve fazer somente |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |

## UC029

| | Justificativa |
|-| ------------- |
|1| O nome do ator revela seu papel no sistema |
|2| O nome do caso de uso está no infinitivo |
|3| O nome do caso de uso é simples e de fácil compreensão |
|4| Todos os relacionamentos entre casos de usos segue a regra |
|5| Ao menos um caso de uso se relaciona com um ator |
|6| Todos os relacionamentos de inclusão respeitam essa regra |
|7| Todos os relacionamentos de extensão respeitam essa regra |
|8| Não há nenhum relacionamento de generalização, portanto essa regra não foi desrespeitada |
|9| Os atores não possuem descrição |
|10| Os fluxos necessários foram escritos |
|11| O caso de uso está representado no diagrama |
|12| Nenhum dos termos proibidos aparecem |
|13| Nenhum dos termos proibidos aparecem |
|14| Os termos estão disponíveis nos léxicos |
|15| Todos os termos são mantidos |
|16| Possui "seleciona o botão" na descrição, o que não é permitido |
|17| Possui "seleciona o botão" na descrição, dizendo como o sistema deve funcionar, o que não é permitido |
|18| A descrição evita requisitos de negócio |
|19| O nome do caso de uso possui um número que o identifica |
|20| O nome do caso de uso é claro, simples e objetivo |