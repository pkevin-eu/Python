''' Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
for num in range(1, 51): #"Para num dentro do intervalo"   #intervalo
    if num % 2 == 0: #se o número for par
        print(num) #mostrando se o número for par
print('ACABOU!')

for n in range(2, 51, 2):       #A maneira de fazer que tenha a mesma solução porém ocupando metade do processador
    print(n, end=' ')
print('Acabou!')