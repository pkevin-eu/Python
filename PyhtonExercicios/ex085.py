'''Aprimore o desafio anterior mostrando:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.'''
somapar = maior = soma3c = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição ({l}, {c}): '))
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
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos números pares deu {somapar}. ')
print(f'A soma dos valores da terceira coluna deu {soma3c}')
print(f'O maior valor da segunda linha informado foi {maior}')
print('-='*30)