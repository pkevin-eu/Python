'''Crie um programa que vair ler vários números e colocar numa lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada na forma decrescente.
C) Se o valor 5 foi digitado e está ou não lista.'''
valores = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    res = str(input('Quer continuar? [S/N]: ')).strip()
    if res in 'Nn':
        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores na lista')
print(f'A lista que foi salva ficou assim: {valores}')
if 5 in valores:
    print('O número 5 que foi solicitado está na lista')
else:
    print('O número 5 que foi solicitado não está na lista')