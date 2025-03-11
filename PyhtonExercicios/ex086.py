'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números de 1 a 60 para cada jogo, cadrastando tudo em uma lista composta'''
#É uma boa solução, porém não pode haver repetições nos jogos sorteados!
#A solução está certa, mas existe um problema que não impede de repetir um número no mesmo jogo!
from random import randint
from time import sleep
mega = []
jogos = int(input('Quantos jogos você quer? '))
tot = 1
while tot <= jogos:
    jogo = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1,60),randint(1,60)]
    tot += 1
    sleep(1)
    mega.append(jogo)
    print(f'Jogo {tot-1}: {jogo}')
print(f'Os palpites que ficaram na lista composta ficaram assim:\n{mega}')