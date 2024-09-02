'''Melhore o desafio anterior (59), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.'''
print('GERADOR DE PA.')
print('-='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(primeiro_termo), end='')
        primeiro_termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada! Ao todo foram {} termos mostrados'.format(total))