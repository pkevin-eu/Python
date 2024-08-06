'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
mediaidade = 0
somaidade = 0
nomevelho = ''
maioridadehomem = 0
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    else:
        if idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média das idades entre os indivíduos é: {}'.format(mediaidade))
print('O homem mais velho possui {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Dentro da pesquisa tiveram {} mulheres com menos de 20 anos'.format(totmulher20))