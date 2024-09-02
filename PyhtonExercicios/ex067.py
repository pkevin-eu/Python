'''Crie um programa que leia idade e sexo de várias pessoas. A cada pessoa registrada, O programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos;
b) quantos homens foram cadastrados;
c) quantas mulheres com menos de 20 anos foram cadastradas;'''
#Possui alguns detalhes que faltam que vou fazer na ex067b! Mas está feito e está correto.
mulhernova = 0
quanthomem = 0
adultos = 0
while True:
    sexo = ' '  #O detalhe que faltava era este, agora sim a solução corresponde ao enunciado
    resp = ' '
    print('-'*35)
    print('CADASTRE UMA PESSOA')
    print('-'*35)
    idade = int(input('Idade: '))
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: [M/F] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if sexo in 'Ff' and idade < 20:
        mulhernova += 1
    if sexo in 'Mm':
        quanthomem += 1
    if idade >= 18:
        adultos += 1
    if resp in 'Nn':
        break
print(f'Ao todo temos {adultos} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {quanthomem} homens.')
print(f'Também foram cadastradas {mulhernova} mulheres com menos de 20 anos.')