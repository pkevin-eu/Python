'''Reforça o desafio 33 dos triângulos, recurso de mostrar que tipo de triângulo será formado: -Equilátero: todos os
lados são iguais; - Isósceles:  dois lados são iguais. -Escaleno: Todos so lados são diferentes.'''

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and a + c > b and b +c > a:
    print('É possível sim que exista um triângulo dado os segmentos')
    if a != b != c != a:
        print('O triângulo formado é ESCALENO')
    elif a == b == c:
        print('O triângulo formado é EQUILÁTERO')               #EXEMPLO DE ESTRUTURA CONDICIONAL ANINHADA
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('Não é possível formar um triângulo com esses segmentos!!')
