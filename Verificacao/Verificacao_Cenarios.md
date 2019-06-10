| Data | Versão | Descrição | Autor |
| - | - | - | - |
| 31/05/2019 | 1.0 | Template Inicial | Henrique Martins |
| 05/06/2019 | 1.1 | Incrementando template com impacto de perguntas e Resultados numéricos | Guilherme de Lyra |
| 05/06/2019 | 1.2 | Incrementando template com contexto, justificativa e tipo (para perguntas)<br />tabela de relevâncias<br />tabela de validação geral<br />e adição de bibliografia | Guilherme de Lyra |
| 07/06/2019 | 1.3 | Adição de Impactos, Justificativas e Tipos | Henrique Martins, Victor Rodrigues |
| 07/06/2019 | 1.4 | Adição de respostas às perguntas | Henrique Martins |
| 08/06/2019 | 1.5 | Filtrando as perguntas e adicionando seus respectivos impactos, justificativas e tipos. | Henrique Martins, Guilherme de Lyra e Rafael Teodósio |

# Verificação - Inspeção [Cenários](https://github.com/requisitos-2019-1/Ribon/wiki/Cen%C3%A1rios)
## Perguntas
<!-- questao -->
| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :-----------: | :--: |
| 1 - O título do cenário indica uma ação? | Alto | Regra do modelo | Binário |
| 2 - O objetivo descreve a finalidade do cenário, em relação ao sistema? | Alto | Regra do modelo | Binário |
| 3 - O contexto/pré-condições descreve o que deva ter sido atingido previamente para que se realize o objetivo proposto pelo cenário atual, sem espaço para dúvidas? | Alto | Regra off-model | Binário |
| 4 - A lista de recursos realmente descrevem todos os recursos necessários para se atingir o objetivo do cenário? | Alto | Regra do modelo | Binário |
| 5 - Os termos específicos estão linkados com léxicos? | Médio | A linkagem facilita o acesso à um maior entendimento, ou esclarecimento, sobre o termo em questão | Numérico |
| 6 - As pós-condições explicam detalhadamente o que ocorre após os episódios se encerrarem? | Alto | Regra do modelo | Numérico |
| 7 - Os episódios são claros o suficiente para não deixarem dúvidas e/ou livre para interpretações? | Alto | É importante que seja claro para o desenvolvedor conseguir seguir os passo-a-passos sem ter indagações internas (o que pode resultar em tomadas de decisões que não acordem com o que se esperava daquela feature)  | Numérico |
| 8 - As restrições representam requisitos que devem ser cumpridos para o cenário ocorrer? | Alto | Regra do modelo | Binário |
| 9 - As exceções representam alguma situação que atrapalha o usuário de atingir o objetivo inicial? | Alto | Regra do modelo | Binário |
| 10 - O cenário está de acordo com o funcionamento real do produto? | Alto | Essa é a finalidade do modelo | Numérico |
| 11 - O cenário ajuda no entendimento do sistema em geral ou de alguma funcionalidade em específico? | Alto | Finalidade do modelo | Numérico |
<!-- fquestao -->
Obs: Perguntas binárias implicam em nota 0 ou 10

## Tabela
### Checklist

Obs: "*" indica que pergunta é binária

[Inspeção Henrique](inspecoes/henrique-martins/inspecao_cenarios.md)
[Inspeção Guilherme](inspecoes/guilherme-de-lyra/inspecao_cenarios.md)
[Inspeção Lucas](inspecoes/lucas-kishima/inspecao_cenarios.md)
[Inspeção Rafael](inspecoes/rafael-teodosio/inspecao_cenarios.md)
<!-- inicio -->
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
<!-- tabela -->
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
<!-- fim -->

### Relevâncias
| Artefato | Ranking |
| -------- | :-----: |
| CN001 - Coletar Ribon Diário | <li></li> | 
| CN002 - Comprar Ribons | <li></li> |
| CN003 - Convidar Amigos | <li></li> |
| CN004 - Criar Conta | <li></li> |
| CN005 - Doar Fortificação Alimentar | <li></li> |
| CN006 - Doar Água Potável | <li></li> |
| CN007 - Doar Ribons | <li></li> |
| CN008 - Escolher Causa | <li></li> |
| CN009 - Ler Histórias | <li></li> |
| CN010 - Ver Causas | <li></li> |
| CN011 - Verificar Comprovantes | <li></li> |
| CN012 - Visualizar ONGs | <li></li> |
| CN013 - Doar Medicamentos | <li></li> |
| CN014 - Doar Saúde Básica | <li></li> |

### Auditoria

| Auditor | Artefato | Perguntas | Data |
| --- | --- | --- | --- |
| Henrique | CN001 - Coletar Ribon Diário | todas | 08/06/2019 |
| Henrique | CN002 - Comprar Ribons | todas | 08/06/2019 |
| Henrique | CN003 - Convidar Amigos | todas | 08/06/2019 |
| Henrique | CN004 - Criar Conta | todas | 08/06/2019 |
| Henrique | CN005 - Doar Fortificação Alimentar | todas | 08/06/2019 |
| Henrique | CN006 - Doar Água Potável | todas | 08/06/2019 |
| Henrique | CN007 - Doar Ribons | todas | 08/06/2019 |
| Henrique | CN008 - Escolher Causa | todas | 08/06/2019 |
| Henrique | CN009 - Ler Histórias | todas | 08/06/2019 |
| Henrique | CN010 - Ver Causas | todas | 08/06/2019 |
| Henrique | CN011 - Verificar Comprovantes | todas | 08/06/2019 |
| Henrique | CN012 - Visualizar ONGs | todas | 08/06/2019 |
| Henrique | CN013 - Doar Medicamentos | todas | 08/06/2019 |
| Henrique | CN014 - Doar Saúde Básica | todas | 08/06/2019 |
| Rafael | CN001 - Coletar Ribon Diário | todas | 08/06/2019 |
| Rafael | CN002 - Comprar Ribons | todas | 08/06/2019 |
| Rafael | CN003 - Convidar Amigos | todas | 08/06/2019 |
| Rafael | CN004 - Criar Conta | todas | 08/06/2019 |
| Rafael | CN005 - Doar Fortificação Alimentar | todas | 08/06/2019 |
| Rafael | CN006 - Doar Água Potável | todas | 08/06/2019 |
| Rafael | CN007 - Doar Ribons | todas | 08/06/2019 |
| Rafael | CN008 - Escolher Causa | todas | 08/06/2019 |
| Rafael | CN009 - Ler Histórias | todas | 08/06/2019 |
| Rafael | CN010 - Ver Causas | todas | 08/06/2019 |
| Rafael | CN011 - Verificar Comprovantes | todas | 08/06/2019 |
| Rafael | CN012 - Visualizar ONGs | todas | 08/06/2019 |
| Rafael | CN013 - Doar Medicamentos | todas | 08/06/2019 |
| Rafael | CN014 - Doar Saúde Básica | todas | 08/06/2019 |
| Guilherme | CN001 - Coletar Ribon Diário | todas | 08/06/2019 |
| Guilherme | CN002 - Comprar Ribons | todas | 08/06/2019 |
| Guilherme | CN003 - Convidar Amigos | todas | 08/06/2019 |
| Guilherme | CN004 - Criar Conta | todas | 08/06/2019 |
| Guilherme | CN005 - Doar Fortificação Alimentar | todas | 08/06/2019 |
| Guilherme | CN006 - Doar Água Potável | todas | 08/06/2019 |
| Guilherme | CN007 - Doar Ribons | todas | 08/06/2019 |
| Guilherme | CN008 - Escolher Causa | todas | 08/06/2019 |
| Guilherme | CN009 - Ler Histórias | todas | 08/06/2019 |
| Guilherme | CN010 - Ver Causas | todas | 08/06/2019 |
| Guilherme | CN011 - Verificar Comprovantes | todas | 08/06/2019 |
| Guilherme | CN012 - Visualizar ONGs | todas | 08/06/2019 |
| Guilherme | CN013 - Doar Medicamentos | todas | 08/06/2019 |
| Guilherme | CN014 - Doar Saúde Básica | todas | 08/06/2019 |
| Lucas | CN001 - Coletar Ribon Diário | todas | 08/06/2019 |
| Lucas | CN002 - Comprar Ribons | todas | 08/06/2019 |
| Lucas | CN003 - Convidar Amigos | todas | 08/06/2019 |
| Lucas | CN004 - Criar Conta | todas | 08/06/2019 |
| Lucas | CN005 - Doar Fortificação Alimentar | todas | 08/06/2019 |
| Lucas | CN006 - Doar Água Potável | todas | 08/06/2019 |
| Lucas | CN007 - Doar Ribons | todas | 08/06/2019 |
| Lucas | CN008 - Escolher Causa | todas | 08/06/2019 |
| Lucas | CN009 - Ler Histórias | todas | 08/06/2019 |
| Lucas | CN010 - Ver Causas | todas | 08/06/2019 |
| Lucas | CN011 - Verificar Comprovantes | todas | 08/06/2019 |
| Lucas | CN012 - Visualizar ONGs | todas | 08/06/2019 |
| Lucas | CN013 - Doar Medicamentos | todas | 08/06/2019 |
| Lucas | CN014 - Doar Saúde Básica | todas | 08/06/2019 |

## Números:																																														
|   | Resultado |
| - | :---------: |
| Número de cenários: | 14 |
| Total de indicadores (cenários x Perguntas): | 154	|
| Taxa de erro de perguntas  (Σ Erros / Total de indicadores): | 67/154 = 0.435 |

## Léxicos importantes identificados:
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)
- [Causa](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX005_Causa.md)
- [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX006_Coletar.md)
- [Comprar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX007_Comprar.md)
- [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX010_Doar.md)
- [História](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX014_Historia.md)
- [Patrocinador](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX020_Patrocinador.md)
- [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usu%C3%A1rio.md)

## Validação Geral:
| Artefato | Nota Geral | Menção | Resultado |
| -------- | :--------: | :----: | :-------: |
| CN001 - Coletar Ribon Diário | 4.44 | MI | Reprovado | | 
| CN002 - Comprar Ribons | 4.44 | MI | Reprovado | |
| CN003 - Convidar Amigos | 4.44 | MI | Reprovado | |
| CN004 - Criar Conta | 4.44 | MI | Reprovado | |
| CN005 - Doar Fortificação Alimentar | 4.44 | MI | Reprovado | |
| CN006 - Doar Água Potável | 4.44 | MI | Reprovado | |
| CN007 - Doar Ribons | 4.44 | MI | Reprovado | |
| CN008 - Escolher Causa | 4.44 | MI | Reprovado | |
| CN009 - Ler Histórias | 4.44 | MI | Reprovado | |
| CN010 - Ver Causas | 4.44 | MI | Reprovado | |
| CN011 - Verificar Comprovantes | 4.44 | MI | Reprovado | |
| CN012 - Visualizar ONGs | 4.44 | MI | Reprovado | |
| CN013 - Doar Medicamentos | 4.44 | MI | Reprovado | |
| CN014 - Doar Saúde Básica | 4.44 | MI | Reprovado | |

## Bibliografia
> [Requisitos - Aula 10 (Maurício Serrano e Milene Serrano](https://aprender.ead.unb.br/pluginfile.php/348654/mod_resource/content/3/Requisitos%20-%20Aula%20010.pdf)
> [Discoverying Requirements - Ian Alexander, Ljerka Beus-Dukic](https://hientl.files.wordpress.com/2011/12/tnyc_discovering-require.pdf)