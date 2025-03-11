'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.'''
galera = list() #Principal
dados = list()  #Temporaria
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N]: '))
    if res in 'Nn':
        break
print(galera)
print(f'No total foram cadastradas {len(galera)}')
print(f'O maior peso cadastrado foi {maior}Kg ', end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}... ', end='')
print(f'\nO menor peso cadastrado foi {menor}Kg ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}... ', end='')
