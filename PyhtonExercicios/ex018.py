#O mesmo professor do desaio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos qautro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('Dos alunos {} a ordem de apresentação selecionada foi {}'.format(lista, lista ))