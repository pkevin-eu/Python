'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor registrado com sucesso!')
    else:
        print('Valor duplicado! Não vou registrar o número...')
    resp = str(input(('Quer continuar? [S/N]: '))).strip()
    if resp in 'Nn':
        break
valores.sort()
print(f'Os valores registrados na lista foram {valores}')