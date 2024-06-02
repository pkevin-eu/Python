#Crie um programa que leia largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados:

larg = float(input('Qual é a largura da parede em metros? '))
alt = float(input('Qual é a altura da parede em metros? '))
area = larg*alt
qtd_tinta = area/2
print('A parede possui as dimensões {} metros x {} metros. Portanto, possui {:.3f}m² '.format(larg, alt, area))
print('A quantidade de tinta necessária para pintar a parede de {:.3f}m² será de {:.3f} litros.'.format(area,qtd_tinta))
