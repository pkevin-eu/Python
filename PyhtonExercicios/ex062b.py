'''crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
n = cont = soma = 0     #forma mais simplificada da gambiarra
n = int(input('Digite um número [999 para parar]: '))  #Se o flag for 999 ele sai direto não vai somar dentro do laço, como última linha
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(cont, soma))
