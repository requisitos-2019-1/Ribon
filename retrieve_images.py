import subprocess
import re
import glob
import urllib.parse
import sys

from contextlib import suppress

url_base_path = r'https://github.com/requisitos-2019-1/Ribon/blob/master/'
lexicos_path = 'Lexicos'
cenarios_path = 'Cenarios'
casos_path = 'Casos_de_uso'
us = 'User_Stories'
nfr = 'NFR'
base = 'Modelagem de Requisitos/'

def encode_url(string):
    return urllib.parse.quote(string)

def retrieve(path, depth=1, ext='.md'):
    end = '/*'*depth+ext
    for current_filename in glob.iglob(base+path+end, recursive=True):
        url = url_base_path+encode_url(current_filename)
        img_name = current_filename.split('/')[-1].split('.')[0]
        path_to_save = 'vis/'+path+'/'+img_name+'.png'
        print(path_to_save)
        subprocess.run(["firefox-esr", "--headless", "--screenshot", 'vis/'+path+'/'+img_name+'.png', url])

retrieve(us)
retrieve(nfr, ext='.png')
retrieve(lexicos_path)
retrieve(cenarios_path)
retrieve(casos_path, depth=2)