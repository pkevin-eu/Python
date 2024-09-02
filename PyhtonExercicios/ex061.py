'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.
ex.:0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''      #Tive dificuldade em fazer este programa
print('-'*30)
print('Sequência de Fibonacci: ')   #n° = (n°-1) + (n°-2)
print('-'*30)
termo = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
n1 = 0
n2 = 1
print('~'*30)
print('{} -> {}'.format(n1, n2), end='')
cont = 3
while cont <= termo:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3                     #Não peguei a linha de raciocínio de primeira, porém a lógica é fácil
    cont += 1
print(' -> FIM')
print('~'*30)