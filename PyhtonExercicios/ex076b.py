'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectitivas posições na lista.'''
maior = menor = 0
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for chave, v in enumerate(valores):
    if v == maior:
        print(f'{chave}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for chave, v in enumerate(valores):
    if v == menor:
        print(f'{chave}... ', end='')