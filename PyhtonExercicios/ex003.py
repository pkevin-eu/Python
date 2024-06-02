# Crie um programa que leia seu sucessor e antecessor:

n = int(input('Digite um número: '))
suc = n + 1
ant = n - 1
print('O número é: {}. O sucessor é: {} e seu antecessor é: {}'.format( n, suc, ant))
# Poderia fazer assim tbm: .format(n, (n+1), (n-1)) desta forma somente uma única variável seria utilizada