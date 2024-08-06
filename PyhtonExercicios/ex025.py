#Faça um programa que leia o nome completo de uma pessoa e mostre, separadamente, o primeiro e último nome da mesma:
nome = str(input('Insira seu nome: ')).strip().split()
print(nome)
print('O primeiro nome do indivíduo é: {}'.format(nome[0]))
print('O último nome do indivíduo é: {}'.format(nome[len(nome)-1])) #A última posição de uma string

