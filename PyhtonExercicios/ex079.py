'''Crie um programa que vai ler vários números e colocar numa lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada na forma decrescente.
C) Se o valor 5 foi digitado e está ou não lista.'''
lista = []
while True:
    num = int(input('Digte um valor: '))
    lista.append(num)
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'A lista em ordem decrescente ficou da seguinte forma: {lista}')
print(f'Foram digitados {len(lista)} números.')
if 5 in lista:
    print('O valor solicitado (5) foi sim digitado.')
else:
    print('O valor solicitado (5) não foi encontrado.')