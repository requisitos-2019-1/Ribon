| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC022 - Convidar Amigos


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
Após abrir o perfil, o usuário convida amigos (através do Telegram, Whatsapp etc) para utilizarem o aplicativo, também.

# Principal(is) Ator(es)
Usuário

# Pre-condições (incluindo trigger)
Nenhuma.

# Fluxo básico de eventos
1. O caso se inicia quando o usuário realiza o caso "UC021 - Abrir Perfil".
1. O usuário seleciona o botão "Convide amigos" ou "Compartilhar".
1. O caso de uso termina.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
1. Acaso algum dos convidados venha a utilizar o aplicativo, o usuário deve ser bonificado com 500 Ribons, realizando o caso "UC023 - Coletar Ribons Após Conversão".
1. Acaso algum dos convidados venha a utilizar o aplicativo, o convidado deve ser bonificado com 200 Ribons, realizando o caso "UC023 - Coletar Ribons Após Conversão".
