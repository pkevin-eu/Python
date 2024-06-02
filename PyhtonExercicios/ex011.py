#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com um aumento de 15%.

sal = float(input('Informe seu salário: '))
novosal = sal*115/100
aumento = novosal - sal
print('Seu antigo salário era de {} reais e seu novo salário é {} reais.'.format(sal, novosal), end=' >>> ')
print('O acréscimo no seu salário foi de {} reais.'.format(aumento))