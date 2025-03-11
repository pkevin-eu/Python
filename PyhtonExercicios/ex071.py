'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela de futebol do campeonato brasileiro de futebol, na
ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados.
b) os últimos 4 colocados da tabela.
c) uma lista com os times em ordem alfabética.
d) em que posição na tabela o time do flamengo.'''
times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG',
        'Internacional', 'Bragantino', 'Atlético-PR', 'Criciúma', 'Juventude', 'Grémio', 'Fluminense', 'Corinthians',
         'EC vitória', 'Cuiabá', 'Atlético-GO')
print('OS 5 PRIMEIROS COLOCADOS')
print('-'*80)
print(times[:5])
print('-'*80)
print('OS ÚLTIMOS 4 COLOCADOS DA TABELA')
print('-'*80)
print(times[-4:])
print('-'*80)
print('TIMES EM ORDEM ALFABÉTICA')
print('-'*80)
print(sorted(times))
print('-'*80)
print('EM QUE POSIÇÃO ESTÁ O FLAMENGO: ')
print('-'*80)
print(f'O Flamengo está na {times.index('Flamengo')+1}° posição')
print('-'*80)