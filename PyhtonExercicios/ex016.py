#Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente do mesmo.
from math import radians, sin, cos, tan

ang = int(input('Digite o valor: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('O valor do ângulo é: {} e seu seno: {}; cosseno: {}; tangente: {}'.format(ang, sen, cos, tan))