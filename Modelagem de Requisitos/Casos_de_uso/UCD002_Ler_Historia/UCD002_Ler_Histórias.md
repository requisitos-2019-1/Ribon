| Data       | Versão  | Descrição       | Autor            |
| ---------- | ------- | --------------- | ---------------- |
| 29/4/2019 | 1.0 | Adicionando diagrama | Henrique Martins |


# UCD002 - Ler História

![diagrama](Ler_Historia.png)

Versão 1.0.

# Descrição
Através do aplicativo Ribon, o usuário é capaz de ler histórias motivadoras
# Principal(is) Ator(es)
Usuário

# Pre-condições (incluindo trigger)
- O [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ter conexão com a Internet.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) ter [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md) instalado.

# Fluxo principal (happy day)
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. Usuário escolhe uma das histórias disponíveis para ler.
1. O caso de uso termina.

# Fluxos alternativos
## Variação 1:
1. O caso se inicia quando o usuário está em um menu diferente do Menu Principal (de Histórias).
1. O fluxo continua a partir do 2º passo do fluxo principal.
    
# Exceções (narrando a possibilidade de voltar ao fluxo principal, ou como isso é impedido)

## Exceção 1 - Sem Conexão com Internet:
1. O caso se inicia quando o usuário inicia o aplicativo e está no Menu Principal (de Histórias).
1. O usuário é notificado de que não há conexão à internet.
1. O usuário poderá ler apenas uma parte da história
1. O aplicativo não irá mostrar novas histórias

# Garantias/Pós-condições (o que deve ser verdade apos o final do caso de uso)
## Pós-sucesso:
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode compartilhar [história](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Historia.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode coletar 100 [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode conhecer mais sobre o Instituto Bancorbrás.
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) pode visitar site de origem da [história](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Historia.md).
## Pós-falha (o que deve ser verdade mesmo em alguns cenarios de exceção):
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usuário.md) deve ser informado que não há conexão com Internet

# Casos de Uso neste Diagrama
| ID  | Caso de Uso |
| ---------- | ------- |
| UC011 | Abrir Menu de Histórias |
| UC012 | Selecionar História |
| UC013 | Compartilhar História |
| UC014 | Coletar 100 Ribons |
| UC015 | Visitar Site de Origem da História |
| UC016 | Saber mais sobre Patrocinador |


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
| CN009 | Ler Histórias |