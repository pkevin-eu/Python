'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
- À vista dinheiro/ cheque: 10% de desconto; - À visto no cartão: 5%de desconto; - Em até 2x no cartão: preço normal; -
3x ou mais no cartão: 20% de juros'''
#Receber o preço e a forma de pagamento:
preço_normal = float(input('Qual é o valor do produto: R$'))
forma_de_pagamento = input('Qual a forma de pagamento? ').strip()
#Estrutura condicional se for dinheiro ou cartão e quantas parcelas
if forma_de_pagamento.upper() == 'DINHEIRO':
    preço_normal = preço_normal - preço_normal*0.1
    print('O valor do produto então será de R${}'.format(preço_normal))
elif forma_de_pagamento.upper() == 'CARTÃO':
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 1:
        preço_normal = preço_normal - preço_normal*0.05
        print('O valor do produto será de R${}'.format(preço_normal))
    elif parcelas == 2:
        print('O valor do produto será o preço normal mesmo, sem descontos! Ou seja, R${}'.format(preço_normal))
    else:
        preço_normal = preço_normal + preço_normal*0.2
        print('O valor do produto então será de R${}'.format(preço_normal))
print('Obrigado pela preferência!!!')
