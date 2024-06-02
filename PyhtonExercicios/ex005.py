#Crie um programa que leia duas notas de um aluno e faça sua média:

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

print('A média do aluno é: {} porque suas notas foram {} e {}'.format(media, nota1, nota2))