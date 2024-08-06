''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de
 palíndromos:'''
frase = str(input('Digite uma frase: ')).strip().upper() #sem espaços desnecessários e tudo em maiúsculo
palavras = frase.split()     #separei as palavras nos seus espaços
junto = ''.join(palavras)   #as palavras separadas e transformadas na lista estão sendo juntadas novamneto sem espaços
inverso = ''
'''inverso = junto[::-1]''' #modo de fazer sem precisar do for e da linha de cima
for letra in range(len(junto) -1, -1, -1):   #Aqui eu estou colocando a frase pra ser escrita de trás para frente
    inverso += junto[letra]
print(junto, inverso)
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('não temos um palíndromo')