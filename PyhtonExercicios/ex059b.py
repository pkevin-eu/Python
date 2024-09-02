'''Refaça o desafio 49, lendo o primeiro termo e a razão de uma PA, monstrando os 10 primeiros termos da progressão
usando a estrutura while.'''
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro_termo), end='')
    primeiro_termo += razão
    cont += 1
print('FIM!')
print('Progressão finalizada! Ao todo foram {} termos mostrados no programa.')