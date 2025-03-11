'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não irei adicionar a lista...')
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
valores.sort() # É melhor colocar as listas em ordem fora dos print
print(f'Os números cadastrados foram {valores}')