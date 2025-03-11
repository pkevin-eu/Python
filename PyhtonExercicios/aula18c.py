galera = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()       #Importante pra caramba, limpa para que dessa forma seja adicionado novos dados
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')
print(galera)