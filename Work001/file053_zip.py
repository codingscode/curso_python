"""
Zip

zip -> cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis passados como
entrada em pares.

"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(list(zip1))  # serve tupla e dicio tambem
print(type(zip1))

# sempre podemos gerar uma lista, tupla ou dicionario
print(list(zip1))
print(tuple(zip1))
print(dict(zip1))

zip2 = zip(lista1, lista2, 'abc')

print(list(zip2))
print('---------------------')

"""
obs: o zip() utiliza como parametro o menor tamanho em iteravel. Isso significa que se estiver 
trabalhando como iteraveis de tamanhos diferentes, irá parar quando os elementos do menor 
iteravel acabarem.
"""
lista3 = [10, 5, 11, 8, 7]

zip3 = zip(lista1, lista2, lista3)

print(list(zip3))

print('---------------------')

# podemos usar diferentes iteraveis com zip
uma_tupla = (1, 2, 3, 4, 5)
uma_lista = ['k', 'w', 't', 'x', 'y']
um_dicionario = {'a': 'um', 'b': 'dois', 'c': 'tres', 'd': 'quatro', 'e': 'cinco'}

zip4 = zip(uma_tupla, uma_lista, um_dicionario.values())
print(list(zip4))

# lista de tuplas
dados1 = [(3, 6), (51, 10), (1, 9), (8, 4), (2, 20)]

print(list(zip(*dados1)))

print('---------------------')

# exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['vicente', 'simon', 'toni']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# podemos usar o map
final2 = zip(alunos, map(lambda cada: max(cada), zip(prova1, prova2)))

print(dict(final2))
