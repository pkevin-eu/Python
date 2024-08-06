'''Crie um programa que faça o computador jogar jokenpô com você.'''
import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
print('-=-'*20)
print('Vamos disputar um Jokenpô? Duvido me vencer!!')
print('-=-'*20)
computador = random.choice(lista)
jogador = input('Entre Pedra, Papel e Tesoura qual vc escolhe: ')
print('Eu escolho {}'.format(computador))
print('PROCESSANDO...')
sleep(3)
if jogador == 'Pedra' and computador == 'Tesoura':
    print('PERDI! Parabéns... você venceu')
elif jogador == 'Papel' and computador == 'Pedra':
    print('PERDI! Parabéns... você venceu')
elif jogador == 'Tesoura' and computador == 'Papel':
    print('PERDI! Parabéns... você venceu')
elif jogador == 'Pedra' and computador == 'Papel':
    print('GANHEI KKKKKKKKKKKKKKKKKKKKKK')
    print('TENTA NOVAMENTE, QUERO VER!!!!')
elif jogador == 'Papel' and computador == 'Tesoura':
    print('GANHEI KKKKKKKKKKKKK')
    print('TENAT NOVAMENTE, QUERO VER!!!')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print('GANHEI KKKKKKKKKKKK')
    print('TENTA NOVAMENTE, QUERO VER!!!')
elif jogador == 'Pedra' and computador == 'Pedra':
    print('Temos um empate, vamos de novo?')
elif jogador == 'Papel' and computador == 'Papel':
    print('Temos um empate, vamos de novo?')
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print('Temos um empate, vamos de novo?')