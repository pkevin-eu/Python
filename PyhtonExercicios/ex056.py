'''Melhore o jogo do desafio 26 onde o computador vai "pensar" num número entre 0 e 10. Só que agora o jogador vai tentar
 adivinhar o valor sorteado até acertar, monstrando no final quantos palpites foram necessários para vencer.'''
from random import randint
palpites = 0
computador = randint(0, 10)
print('--- JOGO DA ADIVINHAÇÃO ---')
jogador = ''
while jogador != computador:
    print('tente adivinhar o número que estou pensando... entre 0 e 10, hein')
    jogador = int(input('minha jogada é: '))
    palpites += 1
    if jogador == computador:
        print('ME MAMA, COMPUTADOR KKKKK Eu ganhei!!')
    else:
        print('TOMA GAP, JOGADOR KKKKK Você perdeu!!')
print('O número do computador foi {}'.format(computador,))
print('Ao todo foram um total de {} tentativas'.format(palpites))
