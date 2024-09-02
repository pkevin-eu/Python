'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores'''
num = 0
r = 'S'
soma = 0
media = 0
maior = 0
menor = 0
cont = 0
while r == 'S':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    r = str(input('Quer continuar ou não? [S/N] ')).upper()[0]
    if cont == 1:
        maior = num
    if num > maior:
        maior = num
    if cont == 1:
        menor = num
    if num < menor:
        menor = num
media = soma/cont
print('A media é {} e foram mostrados {} valores.'.format(media, cont))
print('O maior valor inserido foi {} e o menor foi {}'.format(maior, menor))