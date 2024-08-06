'''Crie um programa que faça o computador jogar jokenpô com você.'''    #GOSTEI MAIS DESSA RESOLUÇÃO!!!
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-='*20)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
        print('TOMA GAP KKKKKKKKKKK')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:   #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
        print('TOMA GAP KKKKKKK')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
        print('TOMA GAP KKKKKK')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVÁLIDA!')