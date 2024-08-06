'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário; -2 para octal; -3 para hexadecimal'''

número = int(input('Digite um número qualquer: '))
print('Escolhas as bases de conversão:')
print('[ 1 ] Converter para a base BINÁRIO:')
print('[ 2 ] Converter para a base OCTAL:')
print('[ 3 ] Converter para a base HEXADECIMAL:')
base_trocada = int(input('Sua opção: '))
if base_trocada == 1:
    print('{} convertendo para a base binária ficaria {}'.format(número, bin(número)[2:])) #removendo o prefixo
elif base_trocada == 2:
    print('{} convertendo para a base octal ficaria {}'.format(número, oct(número)[2:])) #remove o prefixo
elif base_trocada == 3:
    print('{} convertendo para a base hexadecimal ficaria {}'.format(número, hex(número)[2:])) #remove o prefixo
else:
    print('Opção inválida. Tente novamente!!!')