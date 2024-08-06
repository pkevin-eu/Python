'''Crie um programa que leia duas notas de um aluno e calcule sua média, monstrando uma mensagem no final, de acordo com
a média atingida: -Média abaxio de 5.0: 'REPROVADO';-Média entre 5.0 e 6.9:'RECUPERAÇÃO';-Média 7.0 ou superior:'APROVADO'.'''

nome = str(input('Qual é o aluno em questão? ')).strip()
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media <= 5:      #(if 7 > media >= 5) Apenas uma simplificaçaõ!!!
    print('A média de {} foi {}'.format(nome, media))
    print('\033[31mREPROVADO\033[m. Está abaixo da média!')
elif media <= 6.9:
    print('A média de {} foi {}'.format(nome, media))
    print('A média não é o sufuciente para a Aprovação. \033[31mRECUPERAÇÃO\033[m')
else:
    print('A média de {} foi {}'.format(nome, media))
    print('\033[32mPARABÉNS!!!\033[m Sua média está dentro da aprovação.')