'''Faça um program que faça a tabuada dea vários números, um de cada vez para cada valordigitado pelo usuário. O progra
ma será interrompido quando o número solicitado for negativo.''' #Precisei ver o vídeo do exercício
#Olá! Voltei depois de algumas horas, não esperava que poderia botar for dentro do while True, gostei.
cont = 0
while True:
    num = int(input('Digite um valor para fazer a tabuada: '))
    print('-'*30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)