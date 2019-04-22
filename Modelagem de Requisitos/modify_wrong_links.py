import re
import glob
from contextlib import suppress

url_base_path = 'https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%%20de%%20Requisitos/'
lexicos_path = 'Lexicos/'
cenarios_path = 'Cenarios/'

def hyper(st, filename):
    return '['+st+']('+url_base_path+lexicos_path+filename+')'
    
def sub(path, pat1, pat2):
    for filename in glob.iglob(path+'*.md', recursive=True):
        f = open(filename, 'r+')
        content = f.read()

        content = re.sub(pat1, pat2, content) 
            
        f.seek(0)
        f.truncate()
        f.write(content)
        f.close()

sub(lexicos_path, '[Moeda](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Project_Healthy_Children.md)', '[Moeda](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md)')
sub(cenarios_path, '[Moeda](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Project_Healthy_Children.md)', '[Moeda](https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Lexicos/Ribon.md)')
