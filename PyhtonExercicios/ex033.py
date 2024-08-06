''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
a = float(input('Digite o tamnaho de um lado: '))
b = float(input('Digite o tamanho do outro lado: '))
c = float(input('Digite o tamanho do último lado: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível existir um triângulo dados os tamanhos das retas!')
else:
    print('É impossível que exista um triângulo dadas as circunstâncias!')