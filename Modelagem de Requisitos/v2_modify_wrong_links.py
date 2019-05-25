import os, fnmatch, re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

url_base_path = r'https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos'
rfs = r'https://github.com/requisitos-2019-1/Ribon/wiki/MoSCoW'
rnfs = r'https://github.com/requisitos-2019-1/Ribon/wiki/Especifica%C3%A7%C3%A3o-suplementar'

def findReplace(directory, filePattern, pattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            # print(filename)
            if pattern.match(filename):
                link = url_base_path + filepath.split('Modelagem de Requisitos')[1]
                return link
    return False

f = open('User_Stories/backlog_de_produto.md', 'r')
result = f.read()
f.close()
f = open('User_Stories/backlog_de_produto.md', 'r')
flag = 0
dir = os.path.dirname(os.path.abspath(__file__))
get_id = re.compile(r'([A-Z].*?)(?=\d)')
get_nums = re.compile(r'\d+')
get_rf = re.compile(r'RF(?=\d)')
get_rnf = re.compile(r'(RNF.*?)(?=\d)')

for line in f.readlines():
    if (flag <= 1):
        flag+=1
        continue
    else:
        id_rastros = line.split('|')[9].replace(' ', '').strip(',').split(',')
        for i in id_rastros:
            # print(i)
            idx = get_id.findall(i)[0]
            num = get_nums.findall(i)[0].lstrip('0')
            if (len(num) == 1):
                num = '0'+num

            pattern = re.compile(idx+"\d+"+num+"\_\w+\.md")
            link = findReplace(dir, '*.md', pattern)
            if (link):
                result = result.replace(i, '['+i+']'+'('+link+')')
            else:
                if get_rf.match(i):
                    result = result.replace(i, '['+i+']'+'('+rfs+')')
                if get_rnf.match(i):
                    result = result.replace(i, '['+i+']'+'('+rnfs+')')
print (result)