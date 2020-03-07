# Listas

"""
"""
print(type([]))

lista1 = [51, 3, 27, 22, 42, 5, 27, 6, 7, 3, 17, 27, 42]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11)) # 0 a ?-1
lista5 = list('Codar é bom para o cérebro')

print(f'lista1 é {lista1}')
print(f'lista2 é {lista2}')
print(f'lista3 é {lista3}')
print(f'lista4 é {lista4}')
print(f'lista5 é {lista5}')
print('------------')

#checar se valor x está contido na lista
num = 8
if num in lista4:
    print(f'encontrado o numero {num}')
else:
    print(f'não encontrado {num}')

caractere = 'y'
if caractere in lista2:
    print(f'encontrado o caractere {caractere}')
else:
    print(f'não encontrado {caractere}')

print('------------')
# sort - ordenação
lista1.sort()
print(lista1)

lista2.sort()
print(lista2)

# count - contar numero de ocorrencias em lista
print(lista1.count(27))
print(lista5.count('r'))

# append - adicionar elementos a lista
print(lista1)
lista1.append(91)  # assim só um elemento por vez
print(lista1)
lista1.append([15, 21, 79])
print(lista1)
#lista1.append(47, 102, 400)  # dá erro

if [15, 21, 79] in lista1:
    print('essa lista foi encontrada')
else:
    print(('essa lista não foi encontrada'))

if [6, 22, 27] in lista1:
    print('esses foram encontrados')
else:
    print(('esses não foram encontrados'))

lista1.extend([61, 62, 63]) # mais de um por vez, n aceita valor unico
print(lista1)
lista1.extend(['bula'])
lista1.extend('bola')
print(lista1)

lista6 = [32, 33, 34, 'meio', 37]
lista6.append(5)
print(lista6)

# Podemos inserir um novo elemento na lista informando a posição do indice
lista6.insert(2, 'novo valor')  # ordem 2, n substitui
print(lista6)

lista7 = ['babuino', 17, 'copa', 2020]
lista8 = lista6 + lista7
print(lista8)
lista6.extend(lista7)
print(lista6)

# podemos inverter uma lista
lista7.reverse()
print(lista7)

lista9 = ['pao', 'queijo', 'café', 'leite', 10]
print(lista9[::-1])

# copiar uma lista
lista10 = lista9.copy()
print(lista10)

# contando elementos dentro da lista
print(f'o tamanho de lista 9 é {len(lista9)}')

# remover último elemento de uma lista
lista11 = [90, 91, 92, 93, 94, 95, 96, 97]
print(lista11.pop())  # retorna o ultimo e tira
lista11.pop()
print(lista11)

# podemos remover um elemento pelo indice
lista11.pop(1)  # tira o da ordem 1
print(lista11)

# podemos remover todos os elementos de uma lista
lista12 = [12, 13, 14, 15, 16]
lista12.clear()
print(lista12)

# podemos repetir elementos em uma lista
novo = [1, 2, 3]
novo *= 3
print(novo)

# podemos converter string para lista
# exemplo1
curso = 'programação em python'
print(curso)
curso = curso.split()
print(curso)

curso2 = 'programando-em-react'
curso2 = curso2.split('-')
print(curso2)

# convertendo uma lista em uma string
curso3 = ['programando', 'em', 'python']
curso4 = ['programando', 'em', 'javascript']
print(curso3)

parastring = ' '.join(curso3)
print(parastring)

parastring2 = '***'.join(curso4)
print(parastring2)

# listas aceitam misturas
lista13 = [1, 2, [21, 0, 4], True, 3.6, 'avenida', 'r', 1231031]
print(f'{lista13} e seu tipo é {type(lista13)}')
print('-----------')

# Iterando sobre listas
# exemplo 1 - usando for
lista14 = [7, 2, 21, 16, 64]
minhastring = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'e', ' ', 'em', ' ', 'p', 'y', 't', 'h', 'o', 'n']

soma = 0
for elemento in lista14:
    print(elemento)
    soma += elemento

print(f'a soma é {soma}')

juntar = ''
for elemento in minhastring:
    print(elemento)
    juntar += elemento

print(f'juntar é : {juntar}')
print('----------')

# exemplo 2 - usando o while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
       carrinho.append(produto)

for produto in carrinho:
    print(produto)



# fazendo acesso aos elementos de forma indexada
cores = ['laranja', 'verde', 'amarelo', 'vermelho', 'azul', 'branco']

print(f'1 - {cores[0]}, 5 - {cores[4]}')

# fazer acesso aos elementos de forma indexada inversa

print(f'{cores[-1]}, {cores[-2]}, {cores[-3]}, {cores[-6]}') # {cores[-7]} dá erro

print(cores[::-1])

for cor in cores:
    print(cor)

print('------------')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1   # ou indice += 1

print('------------')

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

cores2 = list(enumerate(cores))
print(cores2)

print('-----------')

# Listas aceitam valores repetidos
lista = []
lista.append(54)
lista.append(54)
lista.append(54)
lista.append(15)
lista.append(15)
lista.append('card')
lista.append('card')

print(lista)
print('-----------')

# Outros metodos não tão importantes mas também úteis
# Encontrar o indice de um elemento na lista
listnumeros = [21, 7, 10, 24, 10, 16, 41, 7]

# em qual indice está o valor 16
print(listnumeros.index(16))
print(listnumeros.index(41))
print(listnumeros.index(10))  # retorna o indice o 1º ref elemento encontrado
# caso não haja o referido elemento na lista, dá erro
print('--------------')

# Podemos fazer busca dentro de um range, ou seja, qual indice comerçar a buscar
print(listnumeros.index(7, 1)) #buscar a partir do indice 1
print(listnumeros.index(41, 3))
print(listnumeros.index(16, 1))
print('---------------')

# podemos fazer busca dentro de um range, inicio/fim
print(listnumeros.index(10, 1, 5))  # achar 10 entre indices 1->5

print('----------')

# revisão slice
# lista[inico:fim:passo]
# range[inico:fim:passo]

# Trabalhando com slice de lista com o parametro 'inicio'
lista16 = [5, 6, 7, 8, 9, 10, 12, 21, 28, 32, 34, 37, 49, 50, 52, 56]
print(lista16[2:])   # parti de indice 2 até o último
print(lista16[::])   # tudo
print(lista16[-1:])
print(lista16[:-1])
print(lista16[::-1])

# trabalhando com slice de lista com o parametro 'fim'
print(lista16[:2]) # inicia em 0, pega até o indice 2 - 1

print(lista16[2:5]) # inicia em indice 2, pega até o indice 5 - 1

# trabalhando em slice de lista com o parametro 'passo'
print(lista16[2::3]) # inicia indice 2, até o final, com passo de 3
print(lista16[::2])  # de indice 0 ao final, de 2 em 2
print(lista16[::-1])
print(lista16[::-3])
print('-------')

# invertendo valores em uma lista
nomes = ['alameda', 'dos', 'santos']
nomes[0], nomes[2] = nomes[2], nomes[0]
nomes2 = ['todas', 'as', 'ruas', 'levam', 'a', 'roma']

print(nomes)
print(nomes2[::-1])
nomes2.reverse()
print(nomes2)
print('----------------')

# Soma, valor maximo*, valor minimo*, tamanho
# * se os valores forem todos inteiros ou reais
lista17 = [14, 15, 16, 17, 18, 19, 20, 21]
print(f'a soma é {sum(lista17)}')
print(f'o minimo é {min(lista17)}')
print(f'o maximo é {max(lista17)}')
print(f'o tamanho é {len(lista17)}')

# transformar uma lista em tupla
print(f'o tipo de lista17 é {type(lista17)}')

tupla = tuple(lista17)
print(f'tupla é {tupla}, e seu tipo é {type(tupla)}')

# desempacotamento de listas
lista18 = [2, 3, 4]
num1, num2, num3 = lista18  # se a lista tivesse mais elementos daria erro, e vice-versa

print(num1, num2, num3)
print('--------------------')

# Copiando uma lista para outra (shallow copy e deep copy)
#forma 1 deep copy
lista19 = [3, 4, 5, 6]

nova = lista19.copy()   #deep copy
print(f'nova é {nova}')

nova.append(39)

print(f'lista19 é {lista19}')
print(f'nova é {nova}')

#forma 2 shallow copy
lista20 = [6, 7, 8, 9]

nova2 = lista20
nova2.append(23)

print(f'lista20 é {lista20}')
print(f'nova2 é {nova2}')


