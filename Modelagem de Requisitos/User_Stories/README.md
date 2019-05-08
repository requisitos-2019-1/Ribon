# Trabalho Final

* Chat em único PC acessado via SSH por outras máquinas
* Criar fila com nome baseado em protocolo, ao invés de /qualquernome, -> /chat-nome
    * Permissões:
        Ex:
            /chat-bruno
            * Owner - r+w
            * group - w
            * others - w
    
    * Mensagem precisa ter protocolo com segunte cabeçalho:
    MSG:
    ```
    FROM:TO:txt_msg
    ex -> Joao:Maria:Olá (joão cumprimenta maria)
    ```

    * Usar conjunto de threads ou thread única para <i>receive</i> e <i>send</i>
    
    * Sempre verificar ao tentar enviar mensagens, se fila de destinação existe & está livre

## No APP

* ^C (control+c): Não é para matar o processo, tratar sinal para quando for solicitado não sair, mas mostrar mensagem indicando que se deve utilizar outro atalho (ou mandar a mensagem "exit") 

* Implementar MSG_BROADCAST => o mesmo que 
    ```
    FROM:all:txt_msg
    ex -> Joao:all:Olá (joão todo mundo)
    ```

* Onde ficam as filas? : /dev/mqueue
    * Se tentar mandar mensagem pra alguém, mas a fila do mesmo estiver cheia, então guardar na fila interna para tentar de novo e mostrar mensagem para usuário
        - Usar thread para enviar mensagem


# Para segunda entrega...

* Implementar BROADCAST chefe de todos, tal que o 1º a entrar vira o chefe_de_todos, se sair para outro usuário da fila.

* Similar à uma sala de chat, onde as pessoas se comunicam com o "chefe" (sala) e a mensagem é repassada à todos presentes.


# Limites Gerais
max_msg_len = 500 chars

max_name_len = 10 chars