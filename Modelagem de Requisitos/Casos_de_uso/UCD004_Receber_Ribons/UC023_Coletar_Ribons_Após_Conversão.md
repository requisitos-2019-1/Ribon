| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC023 - Coletar Ribons Após Conversão


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
Após convidar amigos, caso algum deles venha a utilizar o aplicativo por indicação, o usuário deve receber 500 Ribons.

# Principal(is) Ator(es)
Usuário, Convidado, Sistema

# Pre-condições (incluindo trigger)
* O convidado ter baixado o App através do link de convite, realizando o caso "UC028 - Utilizar App Mediante Convite".

# Fluxo básico de eventos
1. O caso inicia com o usuário realizando o caso "UC022 - Convidar Amigos"
1. O convidado então abre o link e começa a utilizar o aplicativo, realizando o caso "UC028 - Utilizar App Mediante Convite".
1. O sistema bonifica o usuário com 500 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O sistema bonifica o convidado com 200 Ribons, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
1. O usuário e convidado ter seus Ribons atualizados.
