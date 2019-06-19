| Data | Versão | Descrição | Autor |
|---|---|---|---|
| 28/04/2019 | [1.0](https://github.com/requisitos-2019-1/Ribon/wiki/Especifica%C3%A7%C3%A3o-suplementar/9b8e76cb1cd3e12619ee3d6e88d6da700fbd0c8c) | Adicionando introdução, finalidade e escopo | Lucas Kishima |
| 28/04/2019 | 1.1 |  Adicionando Requisitos de usabilidade| Lucas kishima |
| 28/04/2019 | 1.2 |  Adicionando Requisitos de confiabilidade| Lucas kishima |
| 28/04/2019 | 1.3 |  Adicionando Requisitos de desempenho| Rafael Teodosio |
| 28/04/2019 | [1.4](https://github.com/requisitos-2019-1/Ribon/wiki/Especifica%C3%A7%C3%A3o-suplementar/87741a3b4d8a7315ec29d3875f6a333fdcf86fce) |  Adicionando Suportabilidade| Rafael Teodosio |
| 28/04/2019 | 1.5 |  Adicionando Restrições de Design| Rafael Teodosio |
| 28/04/2019 | 1.6 |  Adicionando Requisitos de Sistema de Ajuda| Rafael Teodosio |
| 28/04/2019 | 1.7 |  Adicionando Componentes Comprados| Rafael Teodosio |
| 28/04/2019 | [1.8](https://github.com/requisitos-2019-1/Ribon/wiki/Especifica%C3%A7%C3%A3o-suplementar/2141711acbae54e9a6adceba990b9626ec685e35) |  Adicionando Referências| Rafael Teodosio |
| 19/06/2019 | 1.9 |  Adicionando Requisitos de suportabilidade| Lucas kishima |
| 19/06/2019 | 2.0 |  Adicionando Requisitos de privacidade | Lucas kishima |
| 19/06/2019 | 2.1 |  Adicionando Requisitos de manutenibilidade | Lucas kishima |


# 1. Introdução
Este documento reúne e descreve os requisitos não-funcionais do sistema. Os requisitos não-funcionais são aqueles que não necessariamente estão relacionados com alguma funcionalidade do projeto, porém são necessários para o sucesso da aplicação. Tais requisitos descrevem não o que o software fará, mas como ele fará.  Dentre estes requisitos estão incluídos:
- Os atributos de qualidade do sistema a ser criado, incluindo requisitos de usabilidade, desempenho e suportabilidade.
- Outros requisitos como sistemas operacionais e ambientes, requisitos de compatibilidade e restrições de design.
 
## 1.1. Finalidade
Este documento tem como finalidade descrever os requisitos não-funcionais do sistema Ribon. Os requisitos listados nesta especificação suplementar não foram identificados imediatamente nas modelagens realizadas pelo grupo. 
## 1.2. Escopo
Esta especificação define os requisitos não-funcionais associados à qualidade do sistema e além disso, apresenta restrições de Design, os requisitos de sistemas de ajuda e de documentação de usuário online, os componentes comprados, as interfaces do sistema, as observações legais e os padrões aplicáveis à Ribon.
## 1.3. Definições Acrônimos e Abreviações
Disponíveis em [Léxicos](https://github.com/requisitos-2019-1/Ribon/wiki/L%C3%A9xicos).

# 2. Usabilidade
## 2.1. RNFU01
Facilidade de uso: O sistema deve ser fácil de ser utilizado, para que novos usuários aprendam rápido à como usar o mesmo e também não se sintam intimidados por um sistema complexo e de uso difícil.
- Importância: ​ Essencial.
## 2.2. RNFU02
O sistema deve possuir ícones intuitivos, que ajudem a guiar o usuário através do uso da aplicação.
- Importância: ​ Relevante.
## 2.3. RNFU03
O aplicativo deve mostrar um tutorial da aplicação para os novos usuários.
- Importância: ​ Relevante.
## 2.4. RNFU04
O sistema exigirá que o usuário possua conhecimentos mínimos acerca do uso de aplicações mobile.
- Importância: ​ Relevante.
# 3. Confiabilidade
## 3.1. RNFC01
O sistema deve ser capaz proteger as informações do usuário de maneira que minimize os riscos de roubo, dano, perda de informações, acesso não autorizado ou uso indevido de informações.
- Importância: ​ Essencial.
## 3.2. RNFC02
O sistema certificará os usuários que as doações feitas pelos mesmos realmente estão sendo realizadas.
- Importância: ​ Essencial.

# 4. Desempenho
## 4.1. RNFD01
Acesso constante à internet: O aplicativo Ribon tem que ter acesso constante à internet para que possam ser feitos todas as requisições e processamentos necessários para usar o aplicativo.
- Importância:​​ Essencial.
## 4.2. RNFD02
Armazenamento interno e memória: O celular tem que ser capaz de comportar e fazer os cálculos necessários para que o aplicativo funcione corretamente. Para isso tem que haver uma memória RAM suficiente para multitarefas e memória interna do HD para armazenamento de informações persistentes dos sistema.
- Importância:​​ Essencial.

# 5. Supportability
### 5.1 RNFS01
O aplicativo Ribon têm suporte apenas em dispositivos com versões superiores a Android 4.1 ou IOS 8.0 e que tenham acesso à internet.
- Importância: ​ Relevante.

### 5.2 RNFS02
O aplicativo Ribon deve tirar dúvidas e resolver os problemas do usuário ao utilizar o aplicativo de forma rápida e eficiente, para melhorar a experiência do usuário dentro da aplicação.
- Importância: ​ Essencial.
  
### 5.3 RNFS03
O aplicativo deve possuir respostas para perguntas frenquentes.
- Importância: ​ Relevante.
  
### 5.4 RNFS04
O aplicativo deve permitir que o usuário entre em contato com a equipe de suporte.
- Importância: ​ Essencial.
  
# 6. manutenibilidade
### 6.1 RNFM01
Ao realizar correção de bugs, não devem ser adicionados novos no sistema. As possíveis correções devem ser efetivas.
- Importância: ​ Essencial.
  
### 6.2 RNFM02
Ao realizar correção de bugs, não devem ser adicionados novos no sistema. As possíveis correções devem ser efetivas.
- Importância: ​ Relevante.
  
### 6.3 RNFM03
Devem ser realizadas melhorias no software, como adicionar novas funcionalidades ou remover as pouco utilizadas.
- Importância: ​ Essencial.
  
### 6.4 RNFM04
O aplicativo deve utilizar maneiras de prevenir que erros se tornem em falhas, haja vista que quanto mais tempo um erro demora para ser corrigido, mais caro é realizar manutenção do mesmo. 
- Importância: ​ Essencial.

# 7. Privacidade
### 7.1 RNFP01
O sistema deve proteger a empresa de questões legais, através de uma política de privacidade.
- Importância: ​ Essencial.

### 7.2 RNFP02
O sistema deve disponibilizar para conhecimento do usuário, todas as informações que ele coleta e transmite.
- Importância: ​ Essencial.

### 7.3 RNFP03
O sistema deve armazenar os dados do usuário de maneira segura.
- Importância: ​ Essencial.

### 7.4 RNFP04
O sistema deve permitir que o usuário escolha compartilhar suas informações ou não.
- Importância: ​ Essencial.

# 8. Restrições de Design
### 8.1 RNFRD01
O Aplicativo se adaptar ao tamanho da tela do dispositivo que o Usuário estiver utilizando. O padrão de cores para aplicação como objetivo proporcionar a sensação de calma e tranquilidade indo de acordo com o perfil do aplicativo. A disposição dos elementos e funcionalidades nas telas do aplicativo foram feitas de uma forma que o usuário tenha facilidade de usá-lo. O conjunto de telas do aplicativo do usuário foi criado de uma forma que destaca as histórias disponíveis possibilitando a Coleta de Ribons.
 
# 9. Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line
### 9.1 RNFSA01
O Aplicativo conta com um tutorial para auxiliar o usuário na utilização do aplicativo e solução de dúvidas, no funcionamento do sistema, e conta com um site dedicado a auxiliar no entendimento do app.

# 10. Componentes Comprados
### 10.1 RNFC01
O sistema Ribon utiliza histórias de terceiros para postar e coletar Ribons no aplicativo.
 
# 11. Interfaces
## 11.1. RNFI01
### Usuário
As interfaces apresentadas pela aplicação serão visualizadas através de um Celular.
## 11.2. RNFI02
### Hardware
O hardware deverá ser capaz de se conectar à internet.
## 11.3. RNFI03
### Software
Deverá ser apresentado de maneira simples e interativa, para que todos os tipos de Usuários consigam utilizar todo o software.
## 11.4. RNFI04
### Comunicação
A comunicação será feita através de notificações.


# 12. Referências
- https://github.com/victorhdcoelho/Requisitos-uber-2018.2/wiki/Especifica%C3%A7%C3%A3o-Suplementar#7-Requisitos-de-Sistema-de-Ajuda-e-de-Documenta%C3%A7%C3%A3o-de-Usu%C3%A1rio-On-line

- SERRANO, Maurício; SERRANO, Milene. Requisitos - Aula 13, 40 Slides. 1º/2019. Material apresentado para a disciplina de Requisitos de Software no curso de Engenharia de Software da UnB, FGA.
