# Scripts

## AUTO GENERATE TEMPLATE FROM PLANTUML
Através do arquivo Plantuml, gera-se um arquivo markdown praticamente pronto (incluindo já a tabela de versionamento, com nome de quem fez o arquivo, data que foi criado etc)

## AUTO HYPER LINK
Depois de se definir quais são os arquivos dos léxicos, o programa passa por todos os arquivos markdowns desejados e, ao encontrar uma palavra que seja um léxico (ou um sinônimo de um léxico), automaticamente hyperlinka-a pro léxico

## MODIFY WRONG LINKS
Após rodar o script acima com bugs, seria necessário consertar manualmente muitos arquivos. Para evitar-se isso, foi utilizar o script "modify_wrong_links" que consertou-os tranquilamente

## FIX HTML
Como o software de prototipação Pencil não dá suporte pra hyperlinks (qualquer link que saia do prototipo), foi necessário uma gambiarra: criar paginas pra cada link necessário, e depois, atualizar no html gerado o link verdadeiro.

## DISPLAY VERIFICATION

Uma tela intuitiva onde aparece, em cima, o artefato a ser avaliado (onde você pode dar zoom, mover etc), e, embaixo, o tema do artefato, o nome do artefato, e a pergunta de fato os botões:
- Binário:
    - X: nota 0
    - V: nota 10
- Numérico:
    - sr: nota 0
    - ii: nota 2
    - mi: nota 4
    - mm: nota 6
    - ms: nota 8
    - ss: nota 10
    - input field para adicionar a nota que quiser
- Justificativa:
    - Antes de atribuir a nota de fato, é possível escrever uma justificativa do porquê a nota fora atribuída.

Dessa forma, ao se avaliar, é gerado uma tabela em Markdown praticamente perfeita (precisa de pouquíssimos ajustes).

Para se adquirir as imagens das paginas de cada artefato, foi utilizado o script "Retrieve Images":

### Retrieve Images
Pesquisa todos os arquivos markdown no repositorio, e utiliza uma feature do firefox para tirar print da tela inteira.

### Crop Backlog
No caso do backlog, os artefatos não possuíam páginas únicas. Para tanto, modifiquei o html da pagina para que a tabela inteira se tornasse visível, e, após isso, tirei o print da página inteira.
Com isso, utilizei o script "test_crop_backlog" pra detectar cada linha da tabela, e criar uma imagem disso.
Após isso tudo, pra não ficar uma imagem muito solta (ou seja, sem saber o que é cada coluna etc), utilizei o script "add_header" pra adicionar o cabeçalho da tabela em cada linha.

## PLOT VERIFICAÇÃO
Para extrair dados relevantes, utilizei o script "plot_verificacao" para automaticamente bolar gráficos à partir das tabelas markdowns.
