from bs4 import BeautifulSoup as bs
import re
path='index.html'
soup = open(path).read()
soup = bs(soup)

def fix_latin(strn):
    strn = strn.replace("dirio", "diário").replace("histria", "história").replace("notcia", "notícia").replace("confirmao", "confirmação").replace('gua', 'água').replace('potvel', 'potável').replace('sade', 'saúde').replace('bsica', 'básica').replace('doaes', 'doações').replace('doao', 'doação').replace('fortificao', 'fortificação').replace('usurio', 'usuário').replace('doaoes','doações').replace('aps', 'após').replace('contribuio', 'contribuição').replace('carto', 'cartão').replace('crdito', 'crédito').replace('instituies', 'instituições').replace('_so_', '_são_').replace('_s_', '_às_').replace('poltca','política').replace('_j_','_já_').replace('publicao', 'publicação').replace('servios', 'serviços').replace('promoes', 'promoções').replace('padres','padrões').replace('utilizao','utilização').replace('frequncia','frequência').replace('contedo', 'conteúdo').replace('durao', 'duração').replace('sesses', 'sessões').replace('informao', 'informação').replace('informaes', 'informações').replace('histrico', 'histórico').replace('pgina', 'página').replace('localizao', 'localização').replace('geogrfica', 'geográfica').replace('atravs', 'através').replace('endereo', 'endereço').replace('fcil', 'fácil').replace('mnimos', 'mínimos').replace('esto', 'estão').replace('constante_internet', 'constante_à_internet').replace('clculos', 'cálculos').replace('necessrios', 'necessários').replace('verses', 'versões').replace('converso', 'conversão')

    return strn

def triple_dash(strn):
    # padrão:
    # 000-aaa
    strn = re.sub(re.compile(r'(\d)(\_)([^0-9]\w+)', re.UNICODE), r'\g<1>---\g<3>', strn)
    return strn

def fix_str(obj, link, triple=1):
    obj['href'] = fix_latin(obj['href'])
    if(triple):
        obj['href'] = triple_dash(obj['href'])
    obj['target']='_blank'
    obj['href']=link+obj['href']
    return obj

href_tags = soup.find_all(href=True)

# convert RFS
for a in soup.find_all('area', {'href':re.compile('\#rf')}):
    a['href']=r'https://github.com/requisitos-2019-1/Ribon/blob/master/Requisitos/Requisitos_Funcionais.md'+a['href'].replace('_page','')
    a['target']='_blank'

# convert artefatos
for a in soup.find_all('area', {'href':re.compile('artefatos')}):
    a['href']=r'https://github.com/requisitos-2019-1/Ribon/wiki/'+a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('#artefatos', '').replace('_', '-')
    a['target']='_blank'

# convert nfrs
for a in soup.find_all('area', {'href':re.compile('\#nfr')}):
    a=fix_str(a,r'https://github.com/requisitos-2019-1/Ribon/wiki/NFR-Softgoal',triple=0)
    a['href']=a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('_', '-')

# convert istars
for a in soup.find_all('area', {'href':re.compile('\#sd|\#sr')}):
    a=fix_str(a,r'https://github.com/requisitos-2019-1/Ribon/wiki/iStar')
    a['href']=a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('_', '-')

# convert cenarios e lexicos
for a in soup.find_all('area', {'href':re.compile('\#lx|\#cn')}):
    a=fix_str(a,r'https://github.com/requisitos-2019-1/Ribon/wiki/')
    a['href']=a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('_', '-').replace('#','')

# convert user stories
for a in soup.find_all('area', {'href':re.compile('\#us')}):
    a=fix_str(a,r'https://github.com/requisitos-2019-1/Ribon/wiki/Critérios-de-aceitação')
    a['href']=a['href'].replace('_page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('_', '-')

# convert casos de uso
for a in soup.find_all('area', {'href':re.compile('\#ucd')}):
    a['href']=fix_latin(a['href'])
    a['href']=a['href'].replace('xxxxx', '/')
    ucd=a['href'].split('/')[0].replace('#','').title().replace('Ucd', 'UCD')+'/'
    a['href']=a['href'].split('/')[1].title().replace('Uc', 'UC').replace('_De_', '_de_')
    a['href']=r'https://github.com/requisitos-2019-1/Ribon/blob/master/Modelagem%20de%20Requisitos/Casos_de_uso/'+ucd+a['href']
    a['href']=a['href'].replace('_Page','').replace('cenarios', 'cenários').replace('lexicos', 'léxicos').replace('Ong', 'ONG').replace('_A_', '_a_').replace('Alimentar','alimentar')+'.md'
    a['target']='_blank'



# print(soup.prettify())

f=open(path, 'w')
f.write(soup.prettify())
f.close()

# \d_\w