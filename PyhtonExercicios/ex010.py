#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com um desconto de 5%.

prec_produto = float(input('Qual é o preço do produto? '))
desc = prec_produto*95/100
produto_desc = prec_produto - desc
print('O preço do produto era {} reais, após um desconto de 5% o preço passou a ser {} reais. '.format(prec_produto, desc, ))
print('\nO valor do desconto foi {} reais.'.format(produto_desc))