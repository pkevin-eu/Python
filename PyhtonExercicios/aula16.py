#As tuplas são imutáveis!!!
#Programa parado posso meter na tupla, em execução não
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche[:2])
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#Nem sempre vou precisar mostrar a posição, mas quando precisar somente a maneira de cima resolve.
#OU usando 'pos' e 'enumerate' também da.
for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')