from bs4 import BeautifulSoup as bs
import re
path='index.html'
soup = open(path).read()
soup = bs(soup)
href_tags = soup.find_all(href=True)

# convert RFS
for a in soup.find_all('area', {'href':re.compile('\#rf')}):
    a['href']=r'https://github.com/requisitos-2019-1/Ribon/blob/master/Requisitos/Requisitos_Funcionais.md'+a['href'].replace('_page','')
    a['target']='_blank'

# convert artefatos
for a in soup.find_all('area', {'href':re.compile('artefatos')}):
    a['href']=r'https://github.com/requisitos-2019-1/Ribon/wiki/'+a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('#artefatos', '').replace('_', '-')
    a['target']='_blank'


# print(soup.prettify())

f=open(path, 'w')
f.write(soup.prettify())
f.close()

# \d_\w