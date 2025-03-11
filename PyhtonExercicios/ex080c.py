'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respctivamente. Ao final, mostre o conteúdo das três listas
geradas.'''
lista = []
pares = list()
ímpares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-+'*30)
print(f'A lista ficou {lista}')
print(f'A lista dos numeros pares ficou: {pares}')
print(f'A lista dos números ímpares ficou: {ímpares}')