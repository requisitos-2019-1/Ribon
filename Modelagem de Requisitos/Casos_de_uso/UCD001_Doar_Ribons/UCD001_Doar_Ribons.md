| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 28/4/2019 | 1.0 | Adicionando diagrama | Guilherme de Lyra |


# UCD001 - Doar Ribons

![diagrama](Doar_Ribons.png)

Versão 1.0.

# Descrição
Através do aplicativo Ribon, o usuário é capaz de doar os Ribons que coletou para as causas que desejar, podendo, por exemplo, com 110 Ribons, doar 8 dias de fortificação alimentar.

# Principal(is) Ator(es)
Usuário, ONG

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md) instalado.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) desejar [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doar.md) [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md) suficientes pra cada [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md).

# Fluxo principal (happy day)
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário realiza o caso "UC002 - Abrir Menu de Doações".
1. O usuário realiza o caso "UC003 - Selecionar Causa".
1. O usuário seleciona alguma causa, realizando algum desses casos:
    - "UC004 - Selecionar Água Potável"
    - "UC005 - Selecionar Fortificação alimentar"
    - "UC006 - Selecionar Saúde Básica"
    - "UC007 - Selecionar Medicamentos"
1. O usuário decide doar uma quantidade X de Ribons para a causa selecionada, realizando o caso "UC008 - Doar a Quantidade de Ribons Desejada".
1. O sistema realiza o caso "UC009 - Atualizar Quantidade de Ribons".
1. A ONG realiza o caso "UC010 - Receber Doação".
1. O caso de uso termina.

# Fluxos alternativos
## Variação 1:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário realiza o caso "UC001 - Visualizar Quantidade de Ribons".
1. O fluxo continua a partir do 3º passo do fluxo principal.
    
# Exceções (narrando a possibilidade de voltar ao fluxo principal, ou como isso é impedido)

## Exceção 1 - Sem Conexão com Internet:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário realiza o caso "UC002 - Abrir Menu de Doações".
1. O usuário realiza o caso "UC003 - Selecionar Causa".
1. O usuário seleciona alguma causa, realizando algum desses casos:
    - "UC004 - Selecionar Água Potável"
    - "UC005 - Selecionar Fortificação alimentar"
    - "UC006 - Selecionar Saúde Básica"
    - "UC007 - Selecionar Medicamentos"
1. O usuário decide doar uma quantidade X de Ribons para a causa selecionada
1. O usuário é notificado de que a doação não foi concluída mediante falta de conexão à internet.
1. O usuário deve reconectar-se à internet para tentar de novo.

## Exceção 2 - Sem Ribons Suficiente:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário realiza o caso "UC002 - Abrir Menu de Doações".
1. O usuário realiza o caso "UC003 - Selecionar Causa".
1. O usuário seleciona alguma causa, realizando algum desses casos:
    - "UC004 - Selecionar Água Potável"
    - "UC005 - Selecionar Fortificação alimentar"
    - "UC006 - Selecionar Saúde Básica"
    - "UC007 - Selecionar Medicamentos"
1. O usuário decide doar uma quantidade X de Ribons para a causa selecionada
1. O usuário é notificado de que a doação não foi concluída mediante falta de Ribons.
1. O usuário deve realizar algum passo em "UCD002 - Coletar Ribons" para então tentar de novo.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
## Pós-sucesso:
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) é descontado de seu saldo de [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode compartilhar sua [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode conhecer mais sobre o Instituto Bancorbrás.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode voltar para a página anterior e [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doar.md) novamente.
## Pós-falha (o que deve ser verdade mesmo em alguns cenarios de exceção):
- Quantidade de Ribons inalteradas.
- Usuario poder voltar para pagina anterior e tentar novamente.
- Usuario ser informado do motivo que a doação falhou.

# Casos de Uso neste Diagrama
| ID  | Caso de Uso |
| ---------- | ------- |
| UC001 | Visualizar Quantidade de Ribons |
| UC002 | Abrir Menu de Doações |
| UC003 | Selecionar Causa |
| UC004 | Selecionar Água Potável |
| UC005 | Selecionar Fortificação alimentar |
| UC006 | Selecionar Saúde Básica |
| UC007 | Selecionar Medicamentos |
| UC008 | Doar a Quantidade de Ribons Desejada |
| UC009 | Atualizar Quantidade de Ribons |
| UC010 | Receber Doação |

# Possíveis Requisitos Não Funcionais que se aplicam à esse caso de uso
| ID  | RNF |
| ---------- | ------- |
| RU01 | Facilidade de Uso |
| RU02 | Ícones Intuitivos |
| RU04 | Conhecimentos Mínimos |
| RD01 | Acesso à Internet |
| RI04 | Comunicação |

# Cenários Envolvidos
| ID  | Cenário |
| ---------- | ------- |
| CN005 | Doar Fortificação Alimentar |
| CN006 | Doar Água Potável |
| CN007 | Doar Ribons |
| CN008 | Escolher Causa |
| CN013 | Doar Medicamentos |
| CN014 | Doar Saúde Básica |
