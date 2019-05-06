import os, fnmatch, re

lexicos_path = 'Lexicos/'
cases_path = 'Casos_de_uso/'
cenarios_path = 'Cenarios/'

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

replaces = ['LX001_Agua_potavel.md', 'LX002_Aplicativo.md', 'LX003_Aplicativo_nao_Funciona.md', 'LX004_Card.md', 'LX005_Causa.md', 'LX006_Coletar.md', 'LX007_Comprar.md', 'LX008_Comprovante_de_doaçoes.md', 'LX009_Comunidade.md', 'LX010_Doar.md', 'LX011_Doação.md', 'LX012_Evidence_Action.md', 'LX013_Fortificacao_alimentar.md', 'LX014_Historia.md', 'LX015_Historia_coletada.md', 'LX016_Historia_expirada.md', 'LX017_Living_Goods.md', 'LX018_Medicamentos.md', 'LX019_Ong.md', 'LX020_Patrocinador.md', 'LX021_Perfil.md', 'LX022_1_Presente_Diário(Descontinuado).md', 'LX022_Presente_diario.md', 'LX023_Presente_diario_coletado.md', 'LX024_Problemas_com_o_Smartphone.md', 'LX025_Project_Healthy_Children.md', 'LX026_1_Moeda_Ribon(Descontinuado).md', 'LX026_Ribon.md', 'LX027_Saude_basica.md', 'LX028_Schistosomiasis_Control_Initiative.md', 'LX029_Smartphone.md', 'LX030_Tutorial_do_app.md', 'LX031_Usuário.md']

for replace_w_this in replaces:
    find_this = re.sub('\d', '', replace_w_this)
    find_this = find_this.replace('LX_', '')

    findReplace(lexicos_path, find_this, replace_w_this, "*.md")
    findReplace(cases_path, find_this, replace_w_this, "*.md")
    findReplace(cenarios_path, find_this, replace_w_this, "*.md")
