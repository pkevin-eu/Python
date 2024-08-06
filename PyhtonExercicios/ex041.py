'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela a seguir: - Abaixo de 18.5:Abaixo do peso; - Entre 18.5 e 25:Peso ideal; - 25 a 30: Sobrepeso; - 30 até 40:
Obesidade morbida'''

peso = float(input('Qual é o seu peso (Kg): '))
altura = float(input('Qual a sua altura (m): '))
imc = peso / altura**2
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
else:
    print('Obesidade morbida')
