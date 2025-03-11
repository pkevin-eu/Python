'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectitivas posições na lista.'''
maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'DIgite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou os valores {valores}')
print(f'Dos valores digitados o {maior} foi o maior valor nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nDos valores digitados o {menor} foi o menor valor nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')