| Data       | Versão | Descrição                              | Autor             |
| ---------- | ------ | -------------------------------------- | ----------------- |
| 17/04/2019 | 1.0    | Criação do cenario                     | Rafael Teodosio   |
| 22/04/2019 | 1.1    | Correção do objetivo e nome do cenário | Victor Rodrigues  |
| 22/04/2019 | 1.2    | Adiconando espisódios                  | Victor Rodrigues  |
| 22/04/2019 | 1.3    | Modificando episódios e Pós-Condições  | Guilherme de Lyra |
| 22/04/2019 | 2.0    | Absorvendo cenário 002.1               | Victor Rodrigues  |
| 18/06/2018 | 2.1    | Adicionando Requisitos                 | Henrique Martins  |
| 22/06/2019 | 1.2    | Arrumando Erros                     | Henrique Martins  |

# Titulo: [Comprar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX007_Comprar.md) [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).

## Objetivo:
Descrever as etapas da compra de [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md) por parte do [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md), para que ele possa [doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX010_Doar.md) para alguma [causa](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX005_Causa.md).

## Contexto/Pré-condição:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) instalou o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) deseja [Comprar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX007_Comprar.md) [Moeda](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)s [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) possui [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md) de crédito com limite superior ao da compra.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) possui conexão com a internet.

## Atores:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) e [Ribon](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).

## Recursos:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md)
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)
- Conexão com a internet
- Possuir [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md) de crédito.

## Episódios:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) abre [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) navega para aba "perfil".
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) arrasta a tela pra baixo.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) seleciona [Card](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md) "Compre [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)!"
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) escolhe algum dos pacotes de contribuição (6500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)/R$7.9, 12500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)/R$14.9, 21500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)/R$23.9).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) seleciona o botão "Contribuir".
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) preenche os dados de Email, Número do [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md), Nome no [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md), Validade (MM/AA) e Código CVV.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) seleciona o botão "Efetuar [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX011_Doação.md)".
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) realiza a compra.

## Pós-Condições:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe os [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) é levado à uma tela que informa que:
  * A empresa recebeu a [Doação](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX011_Doação.md)
  * O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) já recebeu os [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe notificação/alerta na barra de notificações informando que possui mais de 6200 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md)
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe recibo de pagamento no email cadastrado
- Caso seja a primeira compra, [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe email informando que a onta fora criada
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) pode selecionar o botão "Voltar para o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)"
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) pode [Comprar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX007_Comprar.md) novos [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).

## Restrições:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) possui limite no [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md) de crédito.

## Exceções:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md) deixa de funcionar
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) trava
- Falha na internet
- Falha no [Sistema](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) que realiza compra
- Dados do [Cartão](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX004_Card.md) errados.

## Requisitos:

- [RF11](https://github.com/requisitos-2019-1/Ribon/blob/master/Requisitos/Requisitos_Funcionais.md#RF11)
