# Crie um programa que leia um valor em metros e converta para centímetros e milímetros:

n = float(input('Digite um valor: '))
cent = n * 10**2
mili = n * 10**3
print('{} metro(s) em centímetros é: {} centímetros e em milímetros é: {} miliímetros'.format(n, cent, mili))