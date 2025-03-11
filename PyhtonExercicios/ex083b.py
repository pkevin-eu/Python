'''Crie um programa que o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
num = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'A lista dos valores ficou {num}')
print(f'A lista somente com os valores pares ficou {num[0]}')
print(f'A lista com os valores ímpares ficou {num[1]}')