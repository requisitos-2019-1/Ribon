import re
import glob
from contextlib import suppress

lexicos_path = 'Lexicos/'
cenarios_path = 'Cenarios/'
casos_path = 'Casos_de_uso/'

    
def sub(path, pat1, pat2):
    path = path+'*.md' if path != casos_path else path+'/**/*.md'

    for filename in glob.iglob(path, recursive=True):
        f = open(filename, 'r+')
        content = f.read()

        content = re.sub(pat1, pat2, content) 
            
        f.seek(0)
        f.truncate()
        f.write(content)
        f.close()

sub(lexicos_path, 'Modelagem%%20de%%20Requisitos', r'Modelagem%20de%20Requisitos')
sub(cenarios_path, 'Modelagem%%20de%%20Requisitos', r'Modelagem%20de%20Requisitos')
sub(casos_path, 'Modelagem%%20de%%20Requisitos', r'Modelagem%20de%20Requisitos')
