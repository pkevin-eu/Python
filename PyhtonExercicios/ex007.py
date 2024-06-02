#Crie um programa que leia um número inteiro e mostre sua tabuada:
n = int(input('Digite um número inteiro: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print(' Aqui está a tabuada de {} \n 4x1: {}; 4x2: {}; 4x3: {}; 4x4: {}; 4x5: {}'.format(n, n1, n2, n3, n4, n5),
      end=' ... ')
print('4x6: {}; 4x7: {}; 4x8: {}; 4x9: {}; 4x10: {}'.format(n6, n7, n8, n9, n10))

# Ou poderia fazer cada linha da tabuada como print, afinal é uma apresentação ent n eh tão necessário guardar esses valores
