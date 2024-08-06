'''Escreva um programa para aprovar um empréstimp bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado. '''

valor_casa = float(input('Qual o valor da casa a ser comprada? R$ '))
salario = float(input('Quanto que o comprador ganha mensalmente? R$ '))
anos_pagando = int(input('Quantos anos o comprador irá pagar as prestações? '))
parcela_a_pagar = valor_casa/(anos_pagando*12)
if parcela_a_pagar >= salario*0.3:
    print('A prestação da compra excedeu em 30% o salário do comprador. Pontanto, empréstimo negado')
    print('Agradecemos pelo seu interesse.')
else:
    print('\033[1;30;44mEmpréstimo aceito!!!\033[m')
    print('\033[7;36mParabéns pela sua compra, lembre-se sempre de pagar suas prestações até o dia de vencimento de cada mês!\033[m')
    print('Agradecemos seu interesse!')
print('O valor da prestação ficou em R${:.2f}'.format(parcela_a_pagar))