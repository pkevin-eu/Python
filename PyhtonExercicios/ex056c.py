'''Melhore o jogo do desafio 26 onde o computador vai "pensar" num número entre 0 e 10. Só que agora o jogador vai tentar
 adivinhar o valor sorteado até acertar, monstrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador e estou pensando num número entre 0 e 10...')
print('Quer tentar adivinhar o número que pensei? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!!!'.format(palpite))
