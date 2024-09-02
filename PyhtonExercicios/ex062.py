'''crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
#A maneira que resolvi este programa foi muito bestinha, opinião minha, irei fazer de outra forma no ex062b.
num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um valor [Digite 999 para parar o programa]: '))
    soma += num
    cont += 1
    if num == 999:
        soma = soma - 999
        cont = cont - 1
print('A soma dos números inseridos pelo usuário foi {}. Desconsiderando a flag (número de parada [999])'. format(soma))
print('Foram digitados {} números nessa soma. Desconsiderando a flag(número de parada [999])'.format(cont))