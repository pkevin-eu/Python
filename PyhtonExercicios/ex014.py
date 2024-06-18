#Crie um programa que leia um número qualquer pelo teclado e mostra na tela a sua porção inteira.
from math import trunc

num = float(input('Digite um número com casas decimais: '))
print('O número {} tem a parte inteira de: {}'.format(num, trunc(num)))

'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é: {}'.format(num, int(num)))'''