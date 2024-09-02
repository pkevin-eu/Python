'''Refaça o desafio 49, lendo o primeiro termo e a razão de uma PA, monstrando os 10 primeiros termos da progressão
usando a estrutura while.'''
print('='*15)
print('GERADOR DE PA:')
print('='*15)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
while primeiro_termo < decimo + razao:
    print('{}'.format(primeiro_termo), end=' -> ')
    primeiro_termo += razao
print('FIM!')