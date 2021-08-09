"""
Sorted -> ordena elementos

Não confunda com sort() que estudamos em listas. o sort() só funciona em listas.
Podemos usar o sorted() com qualquer iteravel

OBS: O sorted(), SEMPRE retorna uma lista com os elementos do iteravel ordenados
"""

numeros = [50, 20, 5, 14, 8]
print(numeros)

numeros.sort()  # modifica
print(numeros)

"""
tuplas não são alteraveis
"""

numeros2 = [23, 10, 7, 15, 19]
print(numeros2)

print(sorted(numeros2))  # não modifica

print(numeros2)

print('-----------------------------')

numeros3 = (23, 10, 7, 15, 19)

print(numeros3)
print(sorted(numeros3))  # fica como lista
print(numeros3)

print('-----------------------------')

numeros4 = {23, 10, 7, 15, 19}

print(numeros4)
print(sorted(numeros4))
print(numeros4)

print('-----------------------------')

# Adicionando parametros ao sorted()
numeros5 = [23, 10, 7, 15, 19]

print(numeros5)
print(sorted(numeros5))
print(sorted(numeros5, reverse=True))  # ordena do maior pro menor

print('-----------------------------')

# Podemos utilizar o sorted() para coisas mais complexas


usuarios = [
    {"nome": "samuel", "tweets": ["Eu adoro bolos", "eu adoro pizzas"]},
    {"nome": "dmitry", "tweets": ["Eu gosto de viajar", "eu amo programar"]},
    {"nome": "stefany", "tweets": ["Eu pratico yoga", "eu gosto de fazer caminhada"]},
    {"nome": "pamila", "tweets": ["Eu gosto de ler livros", "eu amo desenhar", "pratico judô"]},
    {"nome": "michael", "tweets": ["Eu gosto de desenhos", "eu amo ciências"]},
    {"nome": "kyle", "tweets": ["Eu estudo matemática", "sempre me informo sobre tecnologias"]},
    {"nome": "vicente", "tweets": []},
    {"nome": "tony", "tweets": []},
    {"nome": "Olga", "tweets": ["eu gosto de escrever"]}
]

[print(cada) for cada in usuarios]

# print(sorted(usuarios)) # dá erro
print(usuarios)
print(sorted(usuarios, key=len))  # key é chave de ordenação
print(sorted(usuarios, key=lambda usuario: usuario['nome'].lower()), '\n')

print('melhor visualização:')
[print(cada) for cada in sorted(usuarios, key=lambda usuario: usuario['nome'].lower())]

print('')
# ordenando pelo numero de tweets

print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])), '\n')

[print(cada) for cada in sorted(usuarios, key=lambda usuario: len(usuario['tweets']))]

print('-----------------------------')

musicas = [
   {'titulo': 'True', 'tocou': 12},
   {'titulo': 'back', 'tocou': 6},
   {'titulo': 'Space fire', 'tocou': 20},
   {'titulo': 'Break ice', 'tocou': 50},
   {'titulo': 'out of cave', 'tocou': 10},
   {'titulo': 'seeing the ocean', 'tocou': 18}
]

# ordem crescente
print(sorted(musicas, key=lambda cada: cada['tocou']), '\n')

ordem1 = sorted(musicas, key=lambda cada: cada['tocou'])
[print(cada) for cada in ordem1]

print('')
# ordem decrescente
ordem2 = sorted(musicas, key=lambda cada: cada['tocou'], reverse=True)
[print(cada) for cada in ordem2]
