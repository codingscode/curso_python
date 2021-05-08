"""

max() -> retorna o maior valor em um iteravel ou o maior de dois ou mais elementos.

min() -> retorna o menor valor em um iteravel ou o menor de dois ou mais elementos.

"""

lista = [3, 34, 10, 15]  # serve tambem para tupla, set, dicionario
dicio = {'b': 3, 'a': 34, 't': 10, 'k': 15}

print(max(lista))
print(max(dicio))
print(max(dicio.values()))

print('--------------------------------------')

print(max(5, 14))
print(max('a', 'ab', 'abc', 'abcd'))
print(max('a', 'b', 'c', 'd'))
print(max('x', 'bty', 'bz', 'm'))
print(max('hoje faz sol'))

print('--------------------------------------')

lista2 = [3, 34, 10, 15]  # serve tambem para tupla, set, dicionario
dicio2 = {'b': 3, 'a': 34, 't': 10, 'k': 15}

print(min(lista))
print(min(dicio))
print(min(dicio.values()))

print(min(5, 14))
print(min('a', 'ab', 'abc', 'abcd'))
print(min('a', 'b', 'c', 'd'))
print(min('x', 'bty', 'bz', 'm'))
print(min('hoje faz sol'))
print(min('hodcum'))

print('--------------------------------------')

nomes = ['jack', 'tom', 'olivier', 'or', 'samuel', 'germanisson', 'ben']

print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda cada: len(cada)))
print(min(nomes, key=lambda cada: len(cada)))
# help(funçãoqualquer) no terminal

"""
max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

para saber mais é só segurar 'ctrl' e passar o cursor em cima da função

"""

print('--------------------------------------')

musicas = [
   {'titulo': 'True', 'tocou': 12},
   {'titulo': 'back', 'tocou': 6},
   {'titulo': 'Space fire', 'tocou': 20},
   {'titulo': 'Break ice', 'tocou': 50},
   {'titulo': 'out of cave', 'tocou': 10},
   {'titulo': 'seeing the ocean', 'tocou': 18}
]

#print(max(musicas))  # dá erro
#print(min(musicas))  # dá erro

print(max(musicas, key=lambda cada: cada['tocou']))  # ordenação mais tocada
print(min(musicas, key=lambda cada: cada['tocou']))

print(max(musicas, key=lambda cada: cada['tocou'])['titulo'])  # só o título
print(min(musicas, key=lambda cada: cada['tocou'])['titulo'])

print(max(musicas, key=lambda cada: cada['titulo'].lower()))  # ordenação titulo
print(min(musicas, key=lambda cada: cada['titulo'].lower()))

print(max(musicas, key=lambda cada: cada['titulo'].lower())['titulo'])  # só titulo
print(min(musicas, key=lambda cada: cada['titulo'].lower())['titulo'])

print('--------------------------------------')

# sem usar max, min e lambda

maximo = 0
for cada in musicas:
    if cada['tocou'] > maximo:
        maximo = cada['tocou']

for cada in musicas:
    if cada['tocou'] == maximo:
        print(cada['titulo'], '- musica mais tocada')

menos = 999999
for cada in musicas:
    if cada['tocou'] < menos:
        menos = cada['tocou']

for cada in musicas:
    if cada['tocou'] == menos:
        print(cada['titulo'], '- musica menos tocada')

print('--------------------------------------')

outro = [cada['tocou'] for cada in musicas]

maior2 = max(outro)
menor2 = min(outro)

print(outro)
print(maior2, 'indice: ', outro.index(maior2))
print(menor2, 'indice: ', outro.index(menor2))

print(musicas[outro.index(maior2)])
print(musicas[outro.index(menor2)])


print('--------------------------------------')

listaqualquer = [10, 5, 20, 18]

print(listaqualquer.index(5))
