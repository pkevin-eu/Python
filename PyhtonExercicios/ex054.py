'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
mediaidade = 0
somaidade = 0
maisvelho = 0
nomemaisvelho = ''
mulhernova = 0
for p in range(1, 5):
    print('------- {}° PESSOA --------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm': #in é se tiver um dos dois 'm' tá certo, valendo
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho =  nome
    if sexo in 'Ff' and idade < 20:
            mulhernova += 1
mediaidade = somaidade/4
print('A média das idades das pessoas é {}'.format(mediaidade))
print('Dentre os homens o mais velho é {} com seus {} anos'.format(nomemaisvelho, maisvelho))
print('Ao todo, tiveram {} mulheres com menos de 20 anos'.format(mulhernova))