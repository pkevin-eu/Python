#Apenas um exemplo em que a estrutura de repetição for não seria utilizável
r = 'S'
while  r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
print('FIM')