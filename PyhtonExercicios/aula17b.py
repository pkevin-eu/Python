valores = list()
#valores.append(2)
#valores.append(4)
#valores.append(8)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}...')
