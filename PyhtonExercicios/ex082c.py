'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.'''
dados = list()  #Lista principal
pessoa = list()  #Lista temporaria, lista que vai ficar dentro da lista principal, aliás, listas
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    res = str(input('Quer continuar? [S/N]: '))
    if res in 'Nn':
        break
print(dados)
print(f'Foram cadastradas {len(dados)} pessoas na lista.')
print(f'O maior peso registrado na lista foi de {maior}, ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}... ', end='')
print(f'\nO menor peso registrado na lista foi de {menor}, ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}... ', end='')