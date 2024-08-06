'''Melhore o jogo do desafio 26 onde o computador vai "pensar" num número entre 0 e 10. Só que agora o jogador vai tentar
 adivinhar o valor sorteado até acertar, monstrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)
palpite = 0
jogador = ''
print('''Sou seu computador e pensei num número entre 0 e 10...
consegue adivinhar qual número eu pensei? ''')
while jogador != computador:
    jogador = int(input('Seu palpite é: '))
    palpite += 1
    if jogador == computador:
        print('Finalmente acertei!')
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print('O número que p computador pensou foi {}'.format(computador))
print('Foram necessários {} palpites para adivinhar o número certo'.format(palpite))
