'''Crie um programa que leia o preço de vários produtos. O programa deverá perguntar se quer continuar ou não. No final,
mostre:
a) Qual é o total de gasto na compra;
b) Quantos produtos custam mais de 1000 R$;
c) Qual é o nome do produto mais barato; '''
soma = cont = cont1k = menor = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: R$ '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preço
    cont += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    if preço > 1000:
        cont1k += 1
    if resp in 'Nn':
        break
print(f'O total gasto dos produtos foi de {soma}')
print(f'{cont1k} produtos custam mais de 1000R$')
print(f'O nome do produto mais barato foi {barato} e custou {menor} R$')