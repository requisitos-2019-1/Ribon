| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 28/4/2019 | 1.0 | Adicionando diagrama | Guilherme de Lyra |


# UCD002 - Receber Ribons

![diagrama](Receber_Ribons.png)

Versão 1.0.

# Descrição
Através do aplicativo Ribon, o usuário é capaz de receber Ribons através de várias formas, seja lendo histórias, sendo usuário assíduo (e portanto coletando presentes diários), comprando o quanto quiser ou seja convidando amigos!

# Principal(is) Ator(es)
Usuário, Convidado, 

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md) instalado.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) desejar receber [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).

# Fluxo principal
## Presente Diário:
1. O caso inicia com o usuário abrindo o App.
1. O usuário identifica o ícone de Presente.
1. O usuário coleta o Presente.
1. O sistema bonifica o usuário com a quantidade de Ribons devida, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.
## Comprar Ribons:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário seleciona o botão Perfil.
1. O usuário é redirecionado ao menu de Perfil com sucesso.
1. O usuário seleciona o botão "Compre ribons!"
1. O usuário é redirecionado para a página de pacotes.
1. [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) escolhe algum dos pacotes de contribuição (6500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md)/R$7.9, 12500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md)/R$14.9, 21500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md)/R$23.9).
1. [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) seleciona o botão "Contribuir".
1. O usuário é redirecionado para página onde deve preencher dados de seu cartão de crédito.
1. [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) preenche os dados de Email, Número do [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Card.md), Nome no [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Card.md), Validade (MM/AA) e Código CVV.
1. [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) seleciona o botão "Efetuar [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md)".
1. O usuário finaliza a compra.
1. O sistema bonifica o convidado com quantos Ribons ele comprou, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.
## Ler História:
1. O caso se inicia quando o usuário inicia o aplicativo, ou então, quando o usuário está em um menu diferente do Menu Principal (de Histórias) e seleciona o botão Histórias.
1. O usuário é direcionado ao menu de Histórias com sucesso.
1. O usuário vislumbra diante de si as histórias disponíveis para leitura.
1. O usuário clica no botão "Coletar"
1. O sistema bonifica o usuário com 100 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.
## Convidar Amigos:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário seleciona o botão Perfil.
1. O usuário é redirecionado ao menu de Perfil com sucesso.
1. O usuário seleciona o botão "Convide amigos" ou "Compartilhar".
1. O convidado começa a utilizar o aplicativo através do link enviado pelo usuário.
1. O sistema bonifica o usuário com 500 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O sistema bonifica o convidado com 200 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.

# Casos de Uso neste Diagrama
| ID  | Caso de Uso |
| ---------- | ------- |
| UC009 | Atualizar Quantidade de Ribons |
| UC011 | Abrir Menu de Histórias |
| UC012 | Selecionar História |
| UC014 | Coletar 100 Ribons |
| UC021 | Abrir Perfil |
| UC022 | Convidar Amigos |
| UC023 | Coletar Ribons Após Conversão |
| UC024 | Coletar Presente Diário |
| UC025 | Comprar Ribons |
| UC026 | Escolher Pacote de Contribuição |
| UC027 | Preencher Dados de Cartão de Crédito |
| UC028 | Utilizar App Mediante Convite |
| UC029 | Finalizar Compra |

# Cenários Envolvidos
| ID  | Cenário |
| ---------- | ------- |
| CN001 | Coletar Ribon Diário |
| CN002 | Comprar Ribons |
| CN003 | Convidar Amigos |
| CN009 | Ler Histórias |
