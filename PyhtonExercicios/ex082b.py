'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.'''
princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Digite seu peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('quer continuar? [S/N]: '))
    if res in 'Nn':
        break
print(f'Forma cadastradas {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi {maior}Kg, ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}... ', end='')
print(f'\nO menor peso cadastrado foi {menor}Kg, ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}... ')