import sys
import pandas as pd
import matplotlib.pyplot as plt
import json

def apply_grade(row):
    if row[1] >= 5.0:
        return "Aprovado"
    else:
        return "Reprovado"

f = open(sys.argv[1]).read()

high = len(f.split('Alto'))-1
med = len(f.split('Médio'))-1
low = len(f.split('Baixo'))-1

f = f.replace('&#10003;', '10')
f = f.replace('X', '0')

imp = {}
questions = f.split('<!-- questao -->')
questions = f.split('<!-- questao -->')[1].split('<!-- fquestao -->')[0]
questions=questions.strip('\n').split('\n')
for i in range(len(questions)):
    if i < 2:
        continue
    impacto = questions[i].split('|')[2].strip(' ')
    no = int(questions[i].split('-')[0].strip('| '))
    if(impacto=='Alto'):
        imp[no]=3
    if(impacto=='Médio'):
        imp[no]=2
    if(impacto=='Baixo'):
        imp[no]=1

print(json.dumps(imp, indent=4))
print(len(imp))
max_ = high*3+med*2+low*1
print(max_)
checklists = f.split('<!-- inicio -->')[1].split('<!-- fim -->')[0].split('<!-- tabela -->')
for c in checklists:
    df = pd.DataFrame(  )
    print (c)
    table_name = c.split('- |\n')[0]
    all_rows = c.split('- |\n')[1]

    table_name = table_name.split(')')[0].strip('\n').strip('|').strip(' ').replace('(', '- ')
    all_rows = all_rows.strip('\n').split('\n')

    named_rows = {}
    for r in all_rows:
        values = [x.strip(' ') for x in r.strip('|').split('|')]
        res = 0
        for i in range(len(values)):
            if(i==0):
                continue
            v = values[i]
            print(i, v)
            res+=int(v)*int(imp[i])
        print(values)
        res = (res/max_)
        row_name = values[0]
        row = [row_name, res]
#         # named_rows[row_name] = values[1:]
        df = df.append([row], ignore_index=True)

    df.reset_index(drop=True, inplace=True)
    df = df.set_index(df.columns[0])
    # df = pd.DataFrame(named_rows)

    for column in df:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        df.plot(kind='barh')
    df["mencao"]=df.apply(lambda row : apply_grade(row), axis=1)
    print(df.to_string())


plt.show()
    # print(df)

# >>> f = open('Verificacao/Verificacao_Cenarios.md').read()
# >>> questions = f.split('<!-- questao -->')
# >>> questions = f.split('<!-- questao -->')[1].split('<!-- fquestao -->')[0]
# >>> questions=questions.strip('\n').questions.split('\n')
# >>> impacto = questions[2].split('|')[2].strip(' ')
# >>> no = questions[2].split('-')[0].strip('| ')
