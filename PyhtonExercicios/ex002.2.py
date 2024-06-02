#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informações possíveis sobre ele.

msg = input('Digite algo:')
print(type(msg))
print('Ele é numérico?', msg.isnumeric())
print('Ele é alfabético?', msg.isalpha())
print('Ele é alfanumérico?', msg.isalnum())
print('Ele está em letras maiúsculas?', msg.isupper())
print('Ele está em letras minúsculas?', msg.islower())
print('Está capitalizada?', msg.istitle())
print('Só tem espaços?',msg.isspace())
