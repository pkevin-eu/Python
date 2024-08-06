'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
 Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

viagem = float(input('Quanto Km a sua viagem terá? '))
if viagem > 200:
    preço = viagem*0.45
    print('A distância desta viagem será de {}Km, logo custará R${}'.format(viagem, preço))
else:
    preçomaior = viagem*0.50
    print('A distância desta viagem será de {}Km, logo custará R${}'.format(viagem, preçomaior))
