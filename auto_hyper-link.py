import re
import glob
from contextlib import suppress

url_base_path = r'https://github.com/requisitos-2019-1/Ribon/blob/master/'
backward_path = 'pós-rastreabilidade/Backward/'
forward_path = 'pós-rastreabilidade/Forward/'
lexicos_path = 'Modelagem de Requisitos/Lexicos/'
title_re = re.compile('(?<=Título: ).*')
sinonimos_re = re.compile('(?<=Sinônimos:).*', re.DOTALL)

def hyper(st, filename):
    return '['+st+']('+url_base_path+lexicos_path+filename+')'
    
def sub(path, current_filename, all_files):
    path = path+'*.md'
    for filename in glob.iglob(path, recursive=True):
            if (filename != current_filename):
                f2 = open(filename, 'r+')
                content = f2.read()
                for sin in all_files:
                    rg_str = r'(?<![_/[])'+sin+r'((?!(.md))(?!\)))'
                    # >>> la = re.compile('(?<![_/])word((?!(.md))(?!\)))', re.IGNORECASE)

                    rgx = re.compile(rg_str, re.IGNORECASE)
                    
                    content = re.sub(rgx, hyper(sin, current_filename.split('/')[1]), content) 
                    
                f2.seek(0)
                f2.truncate()
                f2.write(content)
                f2.close()

for current_filename in glob.iglob(lexicos_path+'*.md', recursive=True):
    if not re.search('Descontinuado', current_filename):
        print(current_filename)
        f = open(current_filename).read()
        title = title_re.findall(f)[0]
        
        with suppress(Exception):
            sinonimos = sinonimos_re.findall(f)[0].replace('\n', '').replace('.', '').split('- ')
            sinonimos = list(filter(None, sinonimos))

        all_files = [title] + sinonimos

        sub(forward_path, current_filename, all_files)
        sub(backward_path, current_filename, all_files)
