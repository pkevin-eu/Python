'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Número duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor cadastrado com sucesso!')
    res = str(input('Deseja continuar? [S/N]: '))
    if res in 'Nn':
        break
valores.sort()
print(f'A lista que foi cadastrada ficou assim: {valores}')