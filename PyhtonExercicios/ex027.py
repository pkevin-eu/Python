'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
 foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual foi a velocidade do carro em Km/h? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado! A multa custurá R$7,00 por cada Km/h acima do limite')
    print('Portanto, a velocidade do carro estava {}KM/h e por consequência o valor agregado da multa foi de R${}'.format( velocidade, multa))
print('Dirija com moderação')
