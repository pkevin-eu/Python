'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
números = []
while True:
    num = int(input('Digite um valor: '))
    if num not in números:
        números.append(num)
        print('Número cadastrado com sucesso!')
    else:
        print('Número duplicado! Não vou adicionar na lista...')
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
números.sort()
print(f'Os valores que foram digitados e cadastrados são {números}')
