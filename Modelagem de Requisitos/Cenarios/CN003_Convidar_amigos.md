| Data       | Versão | Descrição                                  | Autor           |
| ---------- | ------ | ------------------------------------------ | --------------- |
| 17/04/2019 | 1.0    | Criação do cenario                         | Rafael Teodosio |
| 22/04/2019 | 1.1    | Modificação nos espisódios e pós-condições | Rafael Teodosio |
| 18/06/2018 | 1.2    | Adicionando Requisitos                     | Henrique Martins  |
| 22/06/2019 | 1.3    | Arrumando Erros                     | Henrique Martins  |

# Título: Convidar amigos para o [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)

## Objetivo:

- Descrever as etapas para convidar os amigos para [doar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX010_Doar.md) junto com o [usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md).

## Contexto/Pré-condição:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) instalou o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).

## Atores:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) e Amigos.

## Recursos:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md)
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)
- Conexão com a internet

## Episódios:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) abre [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) navega para aba "Perfil"
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) puxa tela para cima.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) seleciona a opção de "Convidar Amigos".
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) seleciona como compartilhar.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) compartilha o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).

## Pós-Condições:

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) pode compartilhar em outro [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) deve receber 500 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md) se o convidado passar a usar o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).

## Restrições:

- Conexão com internet.
- Possuir redes sociais.

## Exceções:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md) deixa de funcionar
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) trava
- Falha na internet
- Falha no [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- Falha nos [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)s que foram compartilhados.

## Requisitos:

- [RF42](https://github.com/requisitos-2019-1/Ribon/blob/master/Requisitos/Requisitos_Funcionais.md#RF42)
