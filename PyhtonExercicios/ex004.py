#Crie um algoritmo que leia um número e me mostre seu dobro, triple e sua raiz quadrada:

n = int(input('Digite um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('O número é: {}, \n seu dobro é: {} \n'.format(n, dobro), end=' >> ')
print('O triplo é: {} e sua raiz quadrada é: {:.2f}'. format(triplo, raiz))