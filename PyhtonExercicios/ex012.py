# Crie um programa que faça as conversões de temperatura.

Fah = float(input('Qual a temperatura em fahrenheit? '))
Kel = float(input('Qual a temperatura em Kelvin? '))

C_F = (5*Fah - 160)/9
C_K = Kel - 273

print('A temperatura em Fahrenheit é {}°F e convertendo a Celsius é: {}°C\n'.format(Fah, C_F))
print('A temperatura em Kelvin é {}K e convertendo em Celsius é: {}°C'.format(Kel, C_K))
