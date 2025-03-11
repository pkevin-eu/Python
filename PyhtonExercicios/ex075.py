'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais'''
palavras = ('aprender', 'programar', 'amor','estudo', 'namoro', 'talento', 'esforço', 'amizade')
for p in palavras:
    print(f'\nA palavra {p.upper()} possui tantas vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra} ', end='')