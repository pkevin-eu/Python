'''Crie um programa que crie uma matriz 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz com
a formatação correta.'''
#dessa forma eu não preciso preencher a matriz com append e só substituindo os valores já estabelecidos "0".
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição ({l}, {c}): '))
#Apenas alimentei os valores da minha matriz.
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()