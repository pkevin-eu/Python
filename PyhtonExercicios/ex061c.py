'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.
ex.:0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
#Fiz algumas modificações: mostra os 10 primerios termos da sequência de FIbonacci e pergunta quantos termos a mais quer ver
print('-'*40)
print('SEQUÊNCIA DE FIBONACCI: ')
print('-'*40)
#n = int(input('Quantos termos você quer mostrar da sequência de Fibonacci? '))
n1 = 0
n2 = 1
cont = 3
total = 0
mais = 10
print('~*'*30)
print('{} -> {} -> '.format(n1, n2), end='')
while mais != 0:
    total += mais
    while cont <= total:
        n3 = n1 + n2
        print('{} -> '.format(n3), end='')
        n1 = n2
        n2 = n3
        cont += 1
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos da sequência de Fibonacci? '))
print('~*'*30)
print('Sequência finalizada. Ao todo foram mostrados {} termos da sequência de Fibonacci.'.format(total))
