# ESTRUTURA CONDIÇÃO ANINHADA: 'tipo igual aquelas bonecas russas, ta ligado?'
nome = str(input('Qual é o seu nome? '))
if nome == 'Paulo':
    print('Que nome lindo!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Gustavo' or nome == 'Ana':
    print('Seu nome é muito popular no Brasil!')
elif nome in 'Valnetina Aurora Angelina':
    print('Belo nome feminino')
else:
    print('Seu nome é tão normal...')     #O else sempre é opcional!!!!
print('Tenha um bom dia, {}!'.format(nome))