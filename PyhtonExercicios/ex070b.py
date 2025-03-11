'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso'''
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze'
, 'Quartoze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        resp = str(input('Você quer continuar?? [S/N]: ')).strip()[0]
        if resp in 'Nn':
            break
    print('Tente novamente. ', end='')
print('FIM DO PROGRAMA!')
