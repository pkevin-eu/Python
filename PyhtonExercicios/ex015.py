# Faça um prgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. calcule e mostre o comprimento da hipotenusa.
import math

cat_oposto = int(input('Digite um valor: '))
cat_adjacente = int(input('Digite outro valor: '))
hipotenusa = math.hypot(cat_oposto, cat_adjacente)

'''hipotenusa = (cat_oposto**2 + cat_adjacente**2)**(1/2)'''

print('O valor do catetos oposto e adjacente são, respectivamente, {} e {}'.format(cat_oposto, cat_adjacente))
print('O valor da hipotenusa é {}'.format(hipotenusa))
