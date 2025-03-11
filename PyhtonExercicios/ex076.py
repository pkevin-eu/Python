'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectitivas posições na lista.'''
maior = menor = 0
valores = list()
for cont in range(0, 5):
    valores.append(int((input(f'Digite um valor para a posição {cont}: '))))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-='*30)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {maior} na posições ', end='')
for chave, valor in enumerate(valores):
    if valor == maior:
        print(f'{chave}... ', end='')
print(f'\nO menor digitado foi {menor} na posições ', end='')
for chave, valor in enumerate(valores):
    if valor == menor:
        print(f'{chave}... ', end='')