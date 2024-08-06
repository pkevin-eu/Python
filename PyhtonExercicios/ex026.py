'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
 qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
from time import sleep   #Da a sensação do computador está analisando...
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5... Tente adivinhar') #o computador "pensa", mas na verdade rondomiza o número
print('-=-' * 20)
n = int(input('Tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
if n == sorteio:
    print('PARABÉNS VOCÊ ACERTOU O NÚMERO')
    print('Perdi!')
else:
    print('Não foi dessa vez, tente novamente!')
    print('O número que pensei foi o {}'.format(sorteio))
    print('GANHEI KKKKKKKKKKK')

'''
Apenas outra forma de se fazer e obter o mesmo resultado:
from random import randint
computador = randint(0, 5) #Faz o computador "pensar", na verdade está rondomizando
jogador = int(input('Pensei em um número entre 0 e 5, tente adivinhar...')) #Jogador tentando adivinhar
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer, acertou o número que pensei!')
else:
    print('GANHEI! o número que pensei foi {} e não o {}!'.format(computador, jogador))
    '''