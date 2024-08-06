'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
num = int(input('Digite o valor que fará a tabuada: '))
for m in range(1, 11):
    print('{} x {:2} = {}'.format(num, m, num*m))