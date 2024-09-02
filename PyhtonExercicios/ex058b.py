'''faça um programa que leia um número qualquer e mostre o seu fatorial.
ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input('Digite o número para calcular o fatorial: '))
c = n
f = 1   #Multiplicação limpa, o número multiplicado por 1 se mantém ele mesmo
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))