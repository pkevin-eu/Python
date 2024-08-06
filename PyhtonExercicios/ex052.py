'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
 maioridade e quantas já são maiores.'''
from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Qual a data de nascimento da {}° pessoa: '.format(c)))
    idade = ano_atual - nasc
    if idade < 18:
        print('A pessoa tem {} anos'.format(idade))
        print('Menor de idade')
        menor += 1
    else:
        print('A pessoa tem {} anos'.format(idade))
        print('Maior de idade')
        maior += 1
print('Teve {} pessoas que atingiram a maioridade e {} pessoas que ainda são menores de idade'.format(maior, menor))