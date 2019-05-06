| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/04/2019 | 1.0 | Adicionando diagrama | Henrique Martins |
| 06/05/2019 | 1.1 | Arrumando diagrama | Henrique Martins |


# UCD003 - Visualizar ONGs

![diagrama](Visualizar_ONGs.png)

Versão 1.0.

# Descrição
Através do aplicativo Ribon, o usuário é capaz de visualizar as ONGs parceiras da Ribon, suas informações e suas áreas de atuação.
# Principal(is) Ator(es)
Usuário

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) instalado.

# Fluxo principal (happy day)
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário realiza o caso "UC002 - Abrir Menu de Doações".
1. O usuário realiza o caso "UC018 - Ver Causas".
1. O usuário realiza o caso "UC003 - Selecionar Causa".
1. O usuário pode, além doar Ribons, visualizar as ONGs disponíveis
1. O caso de uso termina.

# Fluxos alternativos
## Variação 1:
1. O caso se inicia quando o usuário está no próprio perfil.
1. O usuário clica em uma das causas disponíveis
1. O fluxo continua a partir do 5º passo do fluxo principal.

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
## Pós-sucesso:
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) deve poder ver as [ONGs](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX019_Ong.md) e suas informações.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) pode, se desejar, doar[Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).

# Casos de Uso neste Diagrama
| ID  | Caso de Uso |
| ---------- | ------- |
| UC002 | Abrir Menu de Doações |
| UC003 | Selecionar Causa |
| UC008 | Doar a Quantidade de Ribons Desejada |
| UC018 | Ver Causas |
| UC019 | Verificar Comprovantes |
| UC020 | Visualizar ONGs |


# Possíveis Requisitos Não Funcionais que se aplicam à esse caso de uso
| ID  | RNF |
| ---------- | ------- |
| RU01 | Facilidade de Uso |
| RU02 | Ícones Intuitivos |
| RU04 | Conhecimentos Mínimos |
| RD01 | Acesso à Internet |
| RI04 | Comunicação |

# Cenários Envolvidos
| ID  | Cenário |
| ---------- | ------- |
| CN007 | Doar Ribons |
| CN008 | Escolher Causa |
| CN010 | Ver Causas |
| CN011 | Verificar Comprovantes |
| CN012 | Visualizar ONGs |
