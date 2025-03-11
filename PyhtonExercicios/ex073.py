'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''
numeros = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('DIgite outro valor: ')),
           int(input('Digite mais um valor: ')))
print(numeros)
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 foi encontrado na posição {numeros.index(3)+1}°')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print(f'Os valores pares encontrados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')