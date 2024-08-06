'''Crie um programa que leia dois valores e mostre um menu na tela
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a opereção solicitada em cada caso.'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = ''
while not opção == 5:
    print('''
        [1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA
        ''')
    opção = int(input('Qual das opções acima você escolhe? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos valores {} e {} foi {}'.format(n1, n2, soma))
    elif opção == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Dos valores inseridos o maior é o {}'.format(maior))
    elif opção == 4:
        r = 'S'
        while r == 'S':
            n = int(input('Digite algum outro valor: '))
            r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    elif opção > 5:
        print('Opção inválida. Tente novamente!')
    else:
        print('VOCÊ SAIU DO PROGRAMA!')
