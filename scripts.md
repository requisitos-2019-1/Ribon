# Scripts

- [auto-hyper-link](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/auto_hyper-link.py)
- [modify-wrong-links](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/v2_modify_wrong_links.py)
- [auto-generate-template-from-uml](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/auto_generate_template_from_plantuml.py)
- [display-verification](https://github.com/requisitos-2019-1/Ribon/blob/master/display_verification.py)
- [retrieve-images](https://github.com/requisitos-2019-1/Ribon/blob/master/retrieve_images.py)
- [crop-backlog](https://github.com/requisitos-2019-1/Ribon/blob/master/test_crop_backlog.py)
- [add-header](https://github.com/requisitos-2019-1/Ribon/blob/master/add_header.py)
- [plot-verificacao](https://github.com/requisitos-2019-1/Ribon/blob/master/plot_verificacao.py)
- [fix-html](https://github.com/requisitos-2019-1/Ribon/blob/gh-pages/fix_html.py)

## AUTO HYPER LINK
Depois de se definir quais são os arquivos dos léxicos, o programa passa por todos os arquivos markdowns desejados e, ao encontrar uma palavra que seja um léxico (ou um sinônimo de um léxico), automaticamente hyperlinka-a pro léxico

## MODIFY WRONG LINKS
Após rodar o script acima com bugs, seria necessário consertar manualmente muitos arquivos. Para evitar-se isso, foi utilizar o script "modify_wrong_links" que consertou-os tranquilamente

## AUTO GENERATE TEMPLATE FROM PLANTUML
Através do arquivo Plantuml, gera-se um arquivo markdown praticamente pronto (incluindo já a tabela de versionamento, com nome de quem fez o arquivo, data que foi criado

Exemplo de template gerado
![template gerado](https://github.com/requisitos-2019-1/Ribon/blob/master/vis/Casos_de_uso/UC001_Visualizar_Quantidade_de_Ribons.png)

## DISPLAY VERIFICATION

![display](https://github.com/requisitos-2019-1/Ribon/blob/master/display.png)

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
![orig](https://github.com/requisitos-2019-1/Ribon/blob/master/.imgs/boxed-backlog.png)
Com isso, utilizei o script "test_crop_backlog" pra detectar cada linha da tabela, e criar uma imagem disso.
![crop](https://github.com/requisitos-2019-1/Ribon/blob/master/cropped/US005.png)
Após isso tudo, pra não ficar uma imagem muito solta (ou seja, sem saber o que é cada coluna etc), utilizei o script "add_header" pra adicionar o cabeçalho da tabela em cada linha.
![head](https://github.com/requisitos-2019-1/Ribon/blob/master/vis/Backlog/US005.png)

## PLOT VERIFICAÇÃO
Para extrair dados relevantes, utilizei o script "plot_verificacao" para automaticamente bolar gráficos à partir das tabelas markdowns.
![plot](https://github.com/requisitos-2019-1/Ribon/blob/master/casos_grade.png)

## FIX HTML
Como o software de prototipação Pencil não dá suporte pra hyperlinks (qualquer link que saia do prototipo), foi necessário uma gambiarra: criar paginas pra cada link necessário, e depois, atualizar no html gerado o link verdadeiro.

[Link do prototipo, com Backward-To e Forward-From.](https://requisitos-2019-1.github.io/Ribon/index.html)