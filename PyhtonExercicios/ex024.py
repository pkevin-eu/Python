#Faça um programa que leia uma frase e mostre: - Quantas vezes aparece a letra "A"; - Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez:
frase = str(input('Digite uma frase: ')).strip().upper()
print('O número de vezes que aparece a letra "A" é: {}'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra "A" aparece a última vez na posição: {}'.format(frase.rfind('A')))