| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC028 - Utilizar App Mediante Convite


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
Após o usuário convidar alguém, este vêm a utilizar o app através do link recebido.

# Principal(is) Ator(es)
Usuário, Convidado

# Pre-condições (incluindo trigger)
* O usuário ter convidado alguém

# Fluxo básico de eventos
1. O usuário realiza o caso "UC022 - Convidar Amigos"
1. O convidado começa a utilizar o aplicativo através do link enviado pelo usuário.
1. O caso de uso termina.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
1. O usuário e o convidado devem ser bonificados, realizando o caso "UC023 - Coletar Ribons Após Conversão"
