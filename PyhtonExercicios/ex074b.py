'''Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('Escrivaninha', 390, 'Celular', 3900, 'Cadeira', 530)
print('-'*40)
print(f'{"Lista do meu Carrinho":^40} ')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-'*40)