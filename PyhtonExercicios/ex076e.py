'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectitivas posições na lista.'''
valores = list() #ou valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor da lista é {maior} que foi encontrado na posição: ', end=' ')
for chave, valor in enumerate(valores):
    if valor == maior:
        print(f'{chave}... ', end='')
print(f'\nO menor valor da lista é {menor} que foi encontrado na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ')
print(valores)