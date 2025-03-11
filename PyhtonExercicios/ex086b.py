'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números de 1 a 60 para cada jogo, cadrastando tudo em uma lista composta'''
from random import randint
from time import sleep
numeros = list()
jogo = list()
print('-'*30)
print('       JOGO DA MEGA SENA       ')
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            break
    numeros.sort()
    jogo.append(numeros[:])
    numeros.clear()
    tot += 1
print('-='*3, f'SORTEANDO {jogos} JOGOS', '-='*3)
for i, l in enumerate(jogo): #índice e lista!!
    print(f'jogo{i+1}: {l}')
    sleep(1)