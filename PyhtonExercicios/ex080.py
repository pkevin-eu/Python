'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respctivamente. Ao final, mostre o conteúdo das três listas
geradas.'''
lista = list()
listapar = lista[:]
listaimpar = lista[:]
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    res = str(input('Quer continuar?[S/N]: '))
    if num % 2 == 0:
        listapar.append(num)
    if num % 2 == 1:
        listaimpar.append(num)
    if res in 'Nn':
        break
lista.sort()
print(f'Os valores digitados na lista foram: {lista}')
print(f'Os valores pares digitados na lista par foram: {listapar}')
print(f'Os valores ímpares digitados na lista ímpar foram: {listaimpar}')