'''Crie um programa que vai ler vários números e colocar numa lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada na forma decrescente.
C) Se o valor 5 foi digitado e está ou não lista.'''
lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N]: '))
    if res in 'Nn':
        break
lista.sort(reverse=True)
print(f'No fim, a lista ficou assim: {lista}')
print(f'Forma digitados {len(lista)} números.')
if 5 in lista:
    print('O númeor 5 foi sim digitado e está dentro da lista...')
else:
    print('O número 5 não foi digitado, portanto não foi adicionado na lista...')