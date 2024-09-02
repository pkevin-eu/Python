'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores'''
resp = 'S'
num = quant = soma = media = maior = menor = 0       #Forma simplificada da gambiarra
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    resp = str(input('Quer continuar ou não? ')).upper().strip()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma/quant
print('Foram lidos {} valores, a soma foi {}, a media foi {}'.format(quant, soma, media))
print('Dos valores lidos o maior é {} e o menor é {}'.format(maior, menor))