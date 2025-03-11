'''Aprimore o desafio anterior mostrando:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição ({l}, {c}): '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][2]:
            soma3c += matriz[l][2]
        if c == 0:
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print(f'A soma de todos os valores pares da matriz resultou em: {somapar}')
print(f'A soma de todos os valores da terceira coluna resultou em: {soma3c}')
print(f'O maior valor da segunda linha é: {maior}')