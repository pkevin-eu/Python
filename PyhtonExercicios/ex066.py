'''Faça um programa que jogue par ou ímpar com o computador. O programa será interrompido quando o jogador perder
mostrando o total de vitória consecutitvas no final do jogo.'''
from random import randint
print('-='*20)
print('VAMOS JOGAR UM PAR OU ÍMPAR')
print('-='*20)
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    par_impar = str(input('Qual você escolhe Par ou Ímpar [P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} deu {res}')
    print('-'*30)
    if par_impar == res[0]:
        print('Muito bem, computador! EU VENCI!')
        print('Vamos jogar novamente...')
        print('-='*20)
    else:
        print('VOCÊ PERDEU ')
        print('-='*20)
        print(f'GAME OVER!!! Você venceu {cont} vezes')
        print('-='*20)
        break
    cont += 1