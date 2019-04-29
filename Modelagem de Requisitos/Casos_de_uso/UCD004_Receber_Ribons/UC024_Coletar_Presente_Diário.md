| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC024 - Coletar Presente Diário


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
O usuário seleciona o ícone de presente, recebendo a cada dia consecutivo mais Ribons; Iniciando a partir de 25, dobrando a cada dia e chegando ao limite de 150.

# Principal(is) Ator(es)
Usuário

# Pre-condições (incluindo trigger)
1. Usuário não ter coletado nesse dia.
1. Conexão com Internet

# Fluxo básico de eventos
1. O caso inicia com o usuário abrindo o App.
1. O usuário identifica o ícone de Presente.
1. O usuário coleta o Presente.
1. O sistema bonifica o usuário com a quantidade de Ribons devida, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.


# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
1. Usuário recebe Ribons.
1. Usuário recebe mais Ribons a cada dia consecutivo coletando
