| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 28/4/2019 | 1.0 | Adicionando caso | Guilherme de Lyra |


# UC008 - [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Doar.md) a Quantidade de [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Ribon.md)s Desejada


![diagrama]([Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Doar.md)_Ribons.png)

Versão 1.0.

# Breve Descrição
Através do Menu Doações, o [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Usuário.md) decide selecionar alguma [Causa](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Causa.md) e [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Doar.md) uma quantidade de [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Ribon.md)s.


# Principal(is) Ator(es)
[Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Usuário.md)

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md) instalado.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) desejar [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doar.md) [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md) suficientes pra cada [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md).

# Fluxo básico de eventos
1. O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Usuário.md) realiza algum dos casos abaixo:
    - "UC004 - Selecionar [Água potável](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Agua_potavel.md)"
    - "UC005 - Selecionar [Fortificação alimentar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Fortificacao_alimentar.md)"
    - "UC006 - Selecionar [Saúde básica](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Saude_basica.md)"
    - "UC007 - Selecionar [Medicamentos](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Medicamentos.md)"
1. O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Usuário.md) decide [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Doar.md) uma quantidade X de [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Ribon.md)s para a [Causa](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/Lexicos/Causa.md) selecionada.
1. O caso de uso termina.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) é descontado de seu saldo de [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode compartilhar sua [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doação.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode conhecer mais sobre o Instituto Bancorbrás.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode voltar para a página anterior e [Doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Doar.md) novamente.