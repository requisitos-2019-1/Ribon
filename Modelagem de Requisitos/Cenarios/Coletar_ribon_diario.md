| Data       | Versão | Descrição                           | Autor             |
| ---------- | ------ | ----------------------------------- | ----------------- |
| 17/04/2019 | 1.0    | Criação do cenario                  | Victor Rodrigues  |
| 22/04/2019 | 1.1    | Adicionando espisódios              | Victor Rodrigues  |
| 22/04/2019 | 1.2    | Linkando léxicos                    | Victor Rodrigues  |
| 22/04/2019 | 1.3    | Modificando Contexto e Pós-Condição | Guilherme de Lyra |
| 22/04/2019 | 1.4    | Padronizando MarkDown               | Victor Rodrigues  |

# Título: [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Coletar.md) [Presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Presente_diario.md)

## Objetivo: 

- Descrever as etapas de coleta do [presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Presente_diario.md) por parte do [usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md).

## Contexto: 
- Local: Qualquer
- Tempo: Qualquer horário após 00:00 (ou seja, pode [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Coletar.md) 23:59 e depois 00:01)

## Pré-Condição:

  * [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md) instalou o [app](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Aplicativo.md).
  * [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) deseja [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Coletar.md) [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Moeda_Ribon.md).

## Atores: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Usu%C3%A1rio.md) e [presente diário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Presente_diario.md).

## Recursos: 

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Smartphone.md)
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Aplicativo.md)
- Conexão com a internet

## Episódios: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) abre o [App](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Aplicativo.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) identifica icone de [Presente](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Doação.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) coleta o [Presente](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Doação.md).

## Pós-Condições: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) recebe [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Moeda_Ribon.md).
- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) recebe mais [Ribons](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Moeda_Ribon.md) a cada dia consecutivo coletando

## Restrições: 

- [Usuário](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Usuário.md) só pode [Coletar](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Coletar.md) uma vez ao dia.

## Exceções:

- [Celular](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Smartphone.md) deixa de funcionar 
- [Aplicativo](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/Lexicos/Aplicativo.md) trava 
- Falha na internet 
- Falha no sistema que realiza doações.
