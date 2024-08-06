'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com sua idade:-Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 20 anos: SÊNIOR;
Acima: MASTER'''
from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta possui {} anos.'.format(idade))
if idade <= 9:
    print('Classificação MiRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade == 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificaçaõ: MASTER')