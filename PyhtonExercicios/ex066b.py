from random import randint
vitoria = 0
while True:
    jogador =  int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            vitoria += 1
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
        else:
            print('VocÊ perdeu')
            break
print(f'GAME OVER!!! Você venceu {vitoria} vezes')