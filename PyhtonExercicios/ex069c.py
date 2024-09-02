'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor a
ser sacado (númeor inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
OBS.:Considere que o caixa tenha notas de R$50, R$20, R$10 e R$1'''
totced = 0
ced = 50
valor = int(input('Qual o valor que você quer sacar? '))
total = valor
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Você sacou {totced} cédulas de {ced} R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('FIm do programa, volte sempre ao banco do Paulo!!')
