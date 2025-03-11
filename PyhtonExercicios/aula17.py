num = [2, 5, 9, 0]
num[2] = 3
num.append(7) # Única maneira de adicionar novos elementos as listas
num.sort(reverse=True) #Ordena só que ao contrário
num.insert(2, 2) #Inseri valores aonde eu quiser com o arrumamaneto de chaves de identificação
#num.pop() #Dessa forma sem parâmetro elimina o último elemento da lista
#num.pop(3) #Dessa forma com parâmetro elimina o elemento que tiver o índice identificado
num.remove(2) #Elimina apenas a primeira ocorrência do parâmetro
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')