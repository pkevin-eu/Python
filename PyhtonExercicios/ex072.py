'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
numeros = (randint(0,10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(numeros)
print(f'O maior valor da lista de números é {max(numeros)}')
print(f'O menor valor da lista de números é {min(numeros)}')
#Esse min e max são um métodos que pode-se utilizar em variáveis compostas