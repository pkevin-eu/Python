#Escreva um programa que pergunte a qauntidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado.
#Calcule o preço a pagar sabendo que o carro custa 60R$ por dia e 0,15R$ por KM rodados.

dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos kilômetros você rodou? '))
preço_total = (dias * 60) + (km * 0.15)
print('O total a ser pago deve ser {:.2f}R$'.format(preço_total))
