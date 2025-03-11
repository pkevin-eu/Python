'''Crie um programa que leia um nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
boletim = list()
aluno = list()
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input(('nota 2: ')))
    media = (nota1 + nota2)/2
    res = str(input('Quer continuar? [S/N]: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    if res in 'Nn':
        break
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-'*30)
for i, lista in enumerate(boletim):
    print(f'{i:<4}{boletim[i][0]:<10}{boletim[i][3]:>8.1f}')
print('-'*26)
while True:
    n = int(input('Mostrar a nota de qual aluno? [999 para interromper]: '))
    if n == 999:
        break
    if n <= len(boletim) - 1:  #não da erro quando digitar algo maior que o tamnaho da lista!!
        print(f'Notas de {boletim[n][0]} são: [{boletim[n][1]}, {boletim[n][2]}] ')
    print('-'*30)
print('-'*30)
print('<<<  VOLTE SEMPRE  >>>')
