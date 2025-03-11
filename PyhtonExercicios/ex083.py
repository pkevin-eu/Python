'''Crie um programa que o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lista = list()
listap = list()
listai = list()
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
lista.append(listai)
lista.append(listap)
lista.sort()
print(f'A lista normal ficou {lista}')
print(f'A lista par ficou {listap}')
print(f'A lista ímpar ficou {listai}')
