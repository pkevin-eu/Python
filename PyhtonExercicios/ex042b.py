'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
- À vista dinheiro/ cheque: 10% de desconto; - À visto no cartão: 5%de desconto; - Em até 2x no cartão: preço normal; -
3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJA DO PAULO'))
preço_normal = float(input('Qual o valor do Produto: R$ '))
print('''Qual a forma de pagamento?
[ 1 ] à vista dinheiro / Cheque 
[ 2 ] à vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opção = int(input('Qual das opções acima você escolhe? '))
if opção > 4:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
if opção == 1:
    preço_descontado = preço_normal - preço_normal*0.1
    print('O valor era R${:.2f}, mas devido ao desconto de acordo com a forma de pagamento passou a ser R${:.2f}'.format(preço_normal, preço_descontado))
elif opção == 2:
    preço_descontado = preço_normal - preço_normal*0.05
    print('O valor era R${:.2f}, mas devido ao desconto de acordo com a forma de pagemento passa a ser R${:.2f}'.format(preço_normal, preço_descontado))
elif opção == 3:
        print('O valor do produto será de R${:.2f}'.format(preço_normal))
elif opção == 4:
    parcelas = int(input('Qual o número de parcelas? '))
    if parcelas >= 3:
        preço_com_juros = preço_normal + preço_normal*0.2
        print('O valor ira ter acréscimo de juros de 20% antes sendo R${:.2f} e ficará no valor de R${:.2f}'.format(preço_normal, preço_com_juros))