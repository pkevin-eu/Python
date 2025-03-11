'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respctivamente. Ao final, mostre o conteúdo das três listas
geradas.'''
lista = []
listapar = lista[:]
listaimpar = lista[:]
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N]: ')).strip()
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 == 1:
        listaimpar.append(n)
    if res in 'Nn':
        break
lista.sort()
print(f'Os valores digitados na lista foram {lista}')
print(f'Os valores que foram salvos na lista par foram {listapar}')
print(f'Os valores que foram salvos na lista ímpar foram {listaimpar}')