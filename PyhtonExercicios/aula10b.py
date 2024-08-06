nota1 = float(input('A primeira nota: '))
nota2 = float(input('A segunda nota: '))
media = (nota1+nota2)/2
print('A média do aluno foi {:.2f}'.format(media))
if media >= 6:
    print('Sua média está aceitável. PARABÉNS!')
else:
    print('Sua média não está nada bem. ESTUDE MAIS!')
print('FIM DO PROGRAMA!')
