'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.
ex.:0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
print('-'*35)
print('Sequência de Fibonacci:')
print('-'*35)
termo = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('~'*35)
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= termo:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~'*35)