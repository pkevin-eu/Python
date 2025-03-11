'''Crie um programa que crie uma matriz 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz com
a formatação correta.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                      #Dessa forma eu não vou precisar usar o 'append'
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição ({l}, {c}): '))
#Essa parte foi apenas para a alimentação dos valores da minha matriz
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
#Quando termina de substituir os valores de uma linha, quebra a coluna e continua substituindo os valores dass linhas