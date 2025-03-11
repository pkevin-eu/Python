'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''
num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 foi encontrado na posição {num.index(3)+1}°')
else:
    print('O número 3 não foi encontrado dentro desta tupla')
print('Os valores pares encontrados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')