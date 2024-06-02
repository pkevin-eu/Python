#Crie um programa que leia o valor da carteira de uma pessoa e dólares ela pode comprar. Cnsidere: 1 US$ == 5.10 R$
n = eval(input('Quanto reais você tem na sua carteira? '))
dc = n/5.1
print('Você tem {} reais e pode comprar até {:.2f} dólares.'.format(n, dc))