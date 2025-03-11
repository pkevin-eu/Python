teste = list()
teste.append('Paulo')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 19
galera.append(teste[:])
teste[0] = 'Larissa'
teste[1] = 18
galera.append(teste[:])
print(galera)
print(galera[0])
print(galera[0][0])