#Peculiaridade do pyhton sobre listas:
a = [2, 3, 4, 7]
b = a #Pyhton cria uma ligação entre as listas
b = a[:] #Dessa forma cria-se uma cópia de fato
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')