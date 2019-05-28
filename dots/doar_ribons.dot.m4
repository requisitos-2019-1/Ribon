graph doar_ribons {
   define(`soft_goal', `image="cloud1.png", shape=none')
   define(`goal', `shape=ellipse, color=pink, style=filled')
   define(`task', `shape=hexagon,color=darkseagreen,style=filled')
   define(`resource', `shape=square,color=lightblue,style=filled')
   define(`actor', `shape=circle,color=khaki1,style=filled')
##############################
# declaração de "variaveis"  #
##############################
    "Ribons Sejam Doados" [goal]
        "Possuir Ribons" [goal]
            "Comprar Ribons" [task]
                "Possuir Cartão de crédito." [resource]

                "Escolher quantidade de Ribons" [task]
                    "Escolher 21.5k Ribons" [task]
                    "Escolher 12.5k Ribons" [task]
                    "Escolher 6.5k Ribons" [task]

                "Preencher dados de Pagamento" [task]

                "Confirmar compra" [task]

            "Coletar Ribons Diários" [task]

            "Ler Histórias" [task]
                "Coletar Ribons dispostos pela história"[task]
                "Boa História"[soft_goal]
        
        "Escolher Causa"[task]
            "Selecionar Doação"[task]
            "Escolher quantidade de Ribons à ser doados"[task]
                "Ribons"[resource]
            "Confirmar Doação"[task]
        
        "Confiabilidade"[soft_goal]
            "Certificado de Doação"[goal]

###########################
# construção das relaçoes #
###########################
    "Ribons Sejam Doados" -- "Possuir Ribons"[label="makes"]
        "Possuir Ribons" -- "Comprar Ribons"
            "Comprar Ribons" -- "Possuir Cartão de crédito."

            "Comprar Ribons" -- "Escolher quantidade de Ribons"
                "Escolher quantidade de Ribons" -- "Escolher 21.5k Ribons"
                "Escolher quantidade de Ribons" -- "Escolher 12.5k Ribons"
                "Escolher quantidade de Ribons" -- "Escolher 6.5k Ribons"

            "Comprar Ribons" -- "Preencher dados de Pagamento"

            "Comprar Ribons" -- "Confirmar compra"
        "Possuir Ribons" -- "Coletar Ribons Diários"
        "Possuir Ribons" -- "Ler Histórias"
            "Ler Histórias" -- "Coletar Ribons dispostos pela história"
            "Ler Histórias" -- "Boa História"

    "Ribons Sejam Doados" -- "Escolher Causa"
        "Escolher Causa" -- "Escolher quantidade de Ribons à ser doados"
            "Escolher quantidade de Ribons à ser doados" -- "Ribons"
        "Escolher Causa" -- "Selecionar Doação"
        "Escolher Causa" -- "Confirmar Doação"

    "Ribons Sejam Doados" -- "Confiabilidade"
        "Confiabilidade" -- "Certificado de Doação"
}

