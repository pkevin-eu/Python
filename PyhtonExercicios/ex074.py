'''Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem = ('Notebook', 2600, 'Mousepad', 40, 'mouse', 70, 'escrivaninha', 140)
print('-'*40)
print('LISTAGEM DE PREÇO: ')
print('-'*40)
for pos, n in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)