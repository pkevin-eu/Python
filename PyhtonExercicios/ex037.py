'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo co sua idade:
-Se ele ainda vai se alistar ao serviço militar. -Se já passou do tempo do alistamento. Seu programa também deverá mostrar
o tempo que falta ou que passou do prazo.'''
from datetime import date
ano_atual = date.today().year      #ano atual
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print('Você tem {} anos'.format(idade))
if idade < 18:
    falta = 18 - idade
    ano = ano_atual + falta     #poderia ser tbm "nasc + 18"
    print('Você ainda terá que se alistar em breve!')
    print('Faltam apenas {} anos para você se alistar!'.format(falta))
    print('Se alistamneto será no ano de {}'.format(ano))
elif idade == 18:
    print('Este é o ano que você deve procurar se alistar nas forças armadas!')
else:
    passa = idade - 18
    ano = ano_atual - passa
    print('Seu alistamento foi no ano de {}'.format(ano))
    print('Você ja passou do tempo de se alistar nas forças armadas')
    print('Passaram apenas {} anos desde que você se apresentou ao alistamento militar!'.format(passa))
