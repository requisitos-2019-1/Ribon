# TEMPLATE QUALITATIVO DE DIAGRAMAS DE CASOS DE USO

## Casos de Uso
* Fazer os 20% casos importantes (considerando cenarios positivos) e depois os 80% de exceções etc (principio de pareto)
* Fazer tabela de casos de uso
    - ID | Nome | Principal ator | Complexidade | Prioridade
 
* Cada passo deve ser/mostrar uma ação
    - Um caso de uso é uma história, histórias que não andam pra frente são chatas (e ruins de ler); Então, cada passo no diagrama de Casos de Uso deve mostrar algum progresso em direção ao objetivo
* Manter de 6 a 10 passos
* Evitar "se"/"mas", considerar o "valido" primeiro ("se o acesso for autorizado, entao ~" -- corrigido seria -> "apos acesso, ~")
* Pensar sobre perspectiva do usuario final (login nao é um objetivo por exemplo)
* Descrever o ~flow na descrição, nao no diagrama em si
* Nomear o caso de uso com um Verbo (se for possivel encaixar "Eu quero" antes do nome, provavelmente ta certo)
* Primeiro fazer cenarios, depois aglomerar cenarios similares e bolar o diagrama
    - há 5 tipos de cenários
        1. a forma comum de atingir o objetivo
        2. fluxos alternativos até o objetivo
        3. recuperando-se de eventos excepcionais pra atingir o objetivo
        4. lidando com exceções irrecuperaveis de forma segura
        5. exceções que não serão tratadas

* (Diagrama de ?) Casos de uso resultam em algo externo ao sistema/produto (? nao sei)



## Ator
Normalmente uma entidade que atua com um certo papel; não é uma pessoa em si

    ex certo:
        Paypal, vendedor, comprador, usuário, gerente

    ex errado:
        Joao, Maria


    

## Relacionamentos
Existem 5 tipos de relacionamentos 

| Tipo de Relacionamento | Descrição | Sintaxe [PlantUML](http://plantuml.com/use-case-diagram) |
| ------------- |:-------------:| ------ |
| Associação entre ator e caso de uso | <li> Um ator tem de estar associado à 1 ou vários casos de uso</li><br><li> Multiplos atores podem estar associado à 1 unico caso de uso </li> | ator -- (caso)  |
| Generalização de um ator | <li> Filho herda todos os casos de uso do pai, e tem ao menos um caso de uso que o pai nao tem |   pai <\|-- filho  |
| Extend entre dois casos de uso | <li> A extensão (filho) depende do extendido (pai)</li><br><li>O extendido tem de ser completo por si so (nao depende do comportamento do filho)</li><br><li>Pode ser opcional</li> |   (pai) <.. (filho) : << extends >>  |
| Include entre dois casos de uso | <li> Caso base é incompleto sem o caso incluído</li><br><li>O caso a ser incluido é obrigatorio e não opcional</li> |  (marido) ..> (mulher) : << includes >>  |
| Generalização de um caso de uso | <li>Mesma coisa que generalização de atores</li> | pai <\|-- filho |


## Bibliografia

### Livros
------
- https://ieeecs-media.computer.org/media/education/swebok/swebok-v3.pdf
- https://hientl.files.wordpress.com/2011/12/tnyc_discovering-require.pdf

### Links
------
#### Dicas sobre casos de uso em geral
- https://www.uml-diagrams.org/use-case-diagrams.html
- https://creately.com/blog/diagrams/use-case-diagram-tutorial/
- https://creately.com/blog/diagrams/use-case-diagram-relationships/
- https://www.wikihow.com/Write-a-Use-Case
- http://www.gatherspace.com/use-case-examples/
- http://casecomplete.com/lessons/writing-use-cases
- https://knowhow.visual-paradigm.com/uml/10-use-case-diagram-tips/
- https://stackoverflow.com/questions/1696927/whats-is-the-difference-between-include-and-extend-in-use-case-diagram
#### Referências sobre PlantUML
- https://www.codeproject.com/Articles/1278703/UML-Made-Easy-with-PlantUML-VS-Code
- http://plantuml.com/use-case-diagram
- https://www.mitrais.com/news-updates/lets-meet-plantuml/
- https://real-world-plantuml.com/?type=usecase
