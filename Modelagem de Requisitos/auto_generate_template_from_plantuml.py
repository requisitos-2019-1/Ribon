import re
import glob
import collections as ct
from contextlib import suppress
import datetime
import subprocess
import os

cdu = 'Casos_de_uso/'
now = datetime.datetime.now()
user = str(subprocess.check_output(['git', 'config', 'user.name'])).replace('\\n', '').replace('\'', '').replace('b', '')
today = str(now.day)+'/'+str(now.month)+'/'+str(now.year)

template_diag_cdu = open('ucd_template.md').read()
template_cdu = open('uc_template.md').read()

for plantuml in glob.iglob(cdu+'/**/*.txt', recursive=True):
	f = open(plantuml).read()
	path = '/'.join(plantuml.split('/')[:-1])+'/'

	cases = re.findall(r'\(UC.*', f)
	cases = [(i.split('(')[1].split(')')[0].replace('\\n', ' '), i.split('(')[1].split(')')[1].split('as ')[1]) for i in cases]

	actors = re.findall(r'actor .*', f)
	actors = [i.split(':')[1] for i in actors]

	
	dic_name = {}
	dic_relations = ct.defaultdict(list)
	for name, alias in cases:
		dic_name[alias] = name
		rgx = re.compile(r'.*\b'+alias+r'\b.*')
		relations = rgx.findall(f)
		relations = [r.strip() for r in relations]
		relations = relations[1:]

		for r in relations:
			related = re.sub(r'\b'+alias+r'\b','', r)
			related = related.split(':')[0].replace('up', '').replace('left', '').replace('right', '').replace('down', '').replace('-', '').replace('.', '').replace('<', '').replace('>', '').replace('|', '').replace(' ', '')
			
			dic_relations[alias].append(related)
	dic_relations = dict(dic_relations)

	for alias, relateds in dic_relations.items():
		flux = ''.join(['1. O usuário realiza o caso \"'+dic_name[x]+'\"\n' for x in relateds if x != 'u' and x != 'ong'])
		case_name = dic_name[alias]
		new_case = template_cdu.replace('Título/Objetivo', case_name)
		new_case = new_case.replace('Ex: Navegar até X', '')
		new_case = new_case.replace('Versão X', '\nVersão 1.0')
		new_case = new_case.replace('diagrama.png', plantuml.split('/')[-1].replace('txt', 'png'))
		new_case = new_case.replace('Ex: Gerente, Cliente', ', '.join(map(str, actors)))
		new_case = new_case.replace('1. Passo 1\n1. Passo 2, etc', ']]]insere passos aqui]]]')
		new_case = new_case.replace(']]]insere passos aqui]]]', flux)
		new_case = new_case.replace('|  |  |  |  |', '| {0} | {1} | {2} | {3} |'.format(today, '1.0', 'Adicionando caso', user))
		filename = path+case_name.replace('-', '').replace('  ', ' ').replace(' ', '_')+'.md'
		try:
			new_file = open(filename, 'r')
			continue
		except FileNotFoundError:
			new_file = open(filename, 'w')
		new_file.write(new_case)
		new_file.close()


