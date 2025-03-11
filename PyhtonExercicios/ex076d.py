'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectitivas posições na lista.'''
maior = menor = 0
valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Os valores digitados da lista foram {valores}')
print(f'O maior valor digitado foi de {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor registrado na lista foi de {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')