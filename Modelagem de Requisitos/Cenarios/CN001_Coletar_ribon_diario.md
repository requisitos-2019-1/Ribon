| Data       | Versão | Descrição                           | Autor             |
| ---------- | ------ | ----------------------------------- | ----------------- |
| 17/04/2019 | 1.0    | Criação do cenario                  | Victor Rodrigues  |
| 22/04/2019 | 1.1    | Adicionando espisódios              | Victor Rodrigues  |
| 22/04/2019 | 1.2    | Linkando léxicos                    | Victor Rodrigues  |
| 22/04/2019 | 1.3    | Modificando Contexto e Pós-Condição | Guilherme de Lyra |
| 22/04/2019 | 1.4    | Padronizando MarkDown               | Victor Rodrigues  |
| 18/06/2019 | 1.5    | Adicionando Requisitos              | Henrique Martins  |

# Título: [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX006_Coletar.md) [Presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX022_Presente_diario.md)

## Objetivo: 

- Descrever as etapas de coleta do [presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX022_Presente_diario.md) por parte do [usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md).

## Contexto: 
- Local: Qualquer
- Tempo: Qualquer horário após 00:00 (ou seja, pode [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX006_Coletar.md) 23:59 e depois 00:01)

## Pré-Condição:

  * [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md) instalou o [app](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
  * [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) deseja [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX006_Coletar.md) [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).

## Atores: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md) e [presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX022_Presente_diario.md).

## Recursos: 

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md)
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md)
- Conexão com a internet

## Episódios: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) abre o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) identifica icone de [Presente](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX011_Doação.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) coleta o [Presente](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX011_Doação.md).

## Pós-Condições: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) recebe mais [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX026_Ribon.md) a cada dia consecutivo coletando

## Restrições: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX031_Usuário.md) só pode [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX006_Coletar.md) uma vez ao dia.

## Exceções:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX029_Smartphone.md) deixa de funcionar 
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) trava 
- Falha na internet 
- Falha no [Sistema](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/LX002_Aplicativo.md) que realiza doações.

## Requisitos

- [RF7](https://github.com/requisitos-2019-1/Ribon/wiki/Backward-From)
- [RF36](https://github.com/requisitos-2019-1/Ribon/wiki/Backward-From)
- [RF37](https://github.com/requisitos-2019-1/Ribon/wiki/Backward-From)
