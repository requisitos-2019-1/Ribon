| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC009 - Atualizar Quantidade de Ribons


![diagrama](Receber_Ribons.png)

Versão 1.0.

# Breve Descrição
Após usuário coletar Ribons de alguma forma, o Sistema atualiza quantos Ribons o usuário têm disponível.

# Principal(is) Ator(es)
Usuário, Sistema

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md) instalado.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) coletar [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md) suficientes pra cada [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md).

# Fluxo básico de eventos
1. O usuário realiza qualquer um dos casos-triggers abaixo:
    * "UC023 - Coletar 500 Ribons Após Conversão"
    * "UC024 - Coletar Presente Diário"
    * "UC014 - Coletar 100 Ribons"
    * "UC025 - Comprar Ribons"
1. O sistema aumenta a quantidade de Ribons que o usuário têm, realizando o caso "UC009 - Atualizar Quantidade de Ribons".
1. O caso de uso termina.


# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
1. O usuário têm a quantidade de Ribons devida
