"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção


"""
from statistics import mean

valores = 6.5, 9.3, 8.2, 7.5, 10, 9.6, 5.5
media_valores = mean(valores)

print(valores)
print(media_valores)
print('--------------------------')

# OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iteravel.

res = filter(lambda cada: cada > media_valores, valores)
print(res)
print(list(res))
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.
print('-------------------')

paises = ['', 'argentina', '', 'méxico', 'australia', 'alemanha', '', 'noruega']
print(paises)

res2 = filter(lambda cada: cada, paises)
print(res)
print(list(res2))

res3 = filter(None, paises)
print(res3)
print(list(res3))

res4 = filter(lambda cada: len(cada) > 0, paises)
print(res4)
print(list(res4))

print('' is None)

print('------------------------------')
"""
map() -> retorna valores
filter() -> retorna valores booleanos


"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "eu adoro pizzas"]},
    {"username": "dmitry", "tweets": ["Eu gosto de viajar", "eu amo programar"]},
    {"username": "stefany", "tweets": ["Eu pratico yoga", "eu gosto de fazer caminhada"]},
    {"username": "pamila", "tweets": ["Eu gosto de ler livros", "eu amo desenhar", "pratico judô"]},
    {"username": "michael", "tweets": ["Eu gosto de desenhos", "eu amo ciências"]},
    {"username": "kyle", "tweets": ["Eu estudo matemática", "sempre me informo sobre tecnologias"]},
    {"username": "vicente", "tweets": []},
    {"username": "tony", "tweets": []},
    {"username": "Olga", "tweets": ["eu gosto de escrever"]}
]

[print(cada) for cada in usuarios]
# filtrar os usuarios inativos

print('_________________________')

# forma 1
inativos = list(filter(lambda cada: len(cada['tweets']) == 0, usuarios))
print(inativos)

# forma 2
inativos2 = list(filter(lambda cada: not cada['tweets'], usuarios))
print(inativos2)

print(bool([]))
print(bool([]) is False)
print(bool(['a']))
print(bool([2]))
print(bool(0))
print(bool(4))

print('------------------------------------\n')

# combinar filter() e map()
nomes = ['alina', 'daciana', 'mikaela', 'stela', 'geovana', 'diocleziana']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 7 caracteres
lista = list(map(lambda cada: f'sua instrutora é : {cada}', filter(lambda nome: len(nome) < 7, nomes)))
print(lista)

print(list(filter(lambda nome: len(nome) < 7, nomes)))
