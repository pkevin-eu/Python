'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais'''
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(f'{letras.lower()}', end=' ')