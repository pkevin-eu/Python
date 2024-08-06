#Faça um programa que leia o nome de uma pessoa e veja se possui 'Silva'
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome {}, possui "Silva?" {}'.format(nome, 'silva' in nome.lower()))
