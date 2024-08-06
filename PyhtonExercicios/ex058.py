'''faça um programa que leia um número qualquer e mostre o seu fatorial.
ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
c = 1
num = int(input('Digite o valor que você queira fazer o fatorial: '))
while c > 1:
    print(c)
    c += 1
print('FIM')from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))