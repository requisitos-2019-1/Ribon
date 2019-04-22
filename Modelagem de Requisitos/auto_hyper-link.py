import re
import glob
from contextlib import suppress

url_base_path = 'https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem de Requisitos/'
lexicos_path = 'Lexicos/'
cenarios_path = 'Cenarios/'
title_re = re.compile('(?<=Título: ).*')
sinonimos_re = re.compile('(?<=Sinônimos:).*', re.DOTALL)

def hyper(st, filename):
    return '['+st+']('+url_base_path+lexicos_path+filename+')'
    
def sub(path, current_filename, all_files):
    for filename in glob.iglob(path+'*.md', recursive=True):
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

        sub(cenarios_path, current_filename, all_files)
        sub(lexicos_path, current_filename, all_files)
        # for filename in glob.iglob(cenarios_path+'*.md', recursive=True):
        #     if (filename != current_filename):
        #         f2 = open(filename, 'r+')
        #         content = f2.read()
        #         for sin in all_files:
        #             rg_str = r'(?<![_/[])'+sin+r'((?!(.md))(?!\)))'
        #             # >>> la = re.compile('(?<![_/])word((?!(.md))(?!\)))', re.IGNORECASE)

        #             rgx = re.compile(rg_str, re.IGNORECASE)
                    
        #             content = re.sub(rgx, hyper(sin, current_filename.split('/')[1]), content) 
                    
        #         f2.seek(0)
        #         f2.truncate()
        #         f2.write(content)
        #         f2.close()



#>>> z = '''
#... mywordLLD
#... myword@ld
#... myword.dff
#... '''
#>>> la = re.compile('word(?!@)', re.IGNORECASE)
#>>> k = re.sub(la, 'oinc', z.rstrip())
#>>> k
# (?<!a)b matches a "b" that is not preceded by an "a",
# (?<!_)wor
