#Crie um programa em que leia e mostre o nome completo de uma pessoa: - maiúsculo; - minúsculo; - Quantas letras o nome
#completo sem contar espaços; - mostre quantas letras possui o primeiro nome.
nome = str(input('insera seu nome completo: ')).strip()
dividido = nome.split()
print('O nome todo em maiúsculo {} é: '.format(nome.upper()))
print('O nome todo em minúsculo {} é: '.format(nome.lower()))
print('A quantidade de letras do nome é: {} '.format(len(nome)-nome.count(' ')))
print('A quantidade de letras do primeiro nome é: {} '.format(len(dividido[0])))
#print('A quantidade de letras do primeiro nome é: {} '.format(nome.find(' ')))
