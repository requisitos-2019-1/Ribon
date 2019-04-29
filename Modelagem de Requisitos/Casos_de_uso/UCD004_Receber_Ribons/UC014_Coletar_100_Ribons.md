| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 28/4/2019 | 1.0 | Adicionando caso | Henrique Martins |
| 29/4/2019 | 1.1 | Modificando Fluxo | Guilherme de Lyra |

# UC014 - Coletar 100 Ribons


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
O usuário coleta 100 Ribons ao clicar no botão de "Coletar" em cada história

# Principal(is) Ator(es)
Usuário, Sistema

# Pre-condições
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.

# Fluxo básico de eventos
1. O caso se inicia quando o realiza o caso "UC011 - Abrir Menu de Histórias".
1. O usuário clica no botão "Coletar"
1. O sistema bonifica o usuário com 100 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.


# Pós-condições
1. O usuário deverá ter 100 Ribons a mais.
1. A história não pode permitir que o usuário colete Ribons novamente
