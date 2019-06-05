import subprocess
import re
import glob
import urllib.parse
import sys

from contextlib import suppress

url_base_path = r'https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/'
lexicos_path = 'Lexicos'
cenarios_path = 'Cenarios'
casos_path = 'Casos_de_uso'
us = 'User_Stories'
nfr = 'NFR'
base = 'Modelagem de Requisitos/'
# subprocess.run(["firefox-esr", "--headless", "--screenshot", "shot.png", "https://dev.webonomic.nl"])

def encode_url(string):
    return urllib.parse.quote(string)

def retrieve(path, depth=1, ext='.md'):
    end = '/*'*depth+ext
    print(base+path+end)
    for current_filename in glob.iglob(base+path+end, recursive=True):
        print(current_filename)

retrieve(us)