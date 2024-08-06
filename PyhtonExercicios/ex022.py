#Faça um programa que leia um nome cidade e diga se ela começa ou não com 'Santo'.
cidade = str(input('Qual o nome da cidade? ')).strip()
print('Santo' in cidade.title())
#print(cidade[:5].upper() == 'SANTO')
print(cidade)