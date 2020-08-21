"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.
Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


"""

nome = 'python'   # é um iteravel mas não é um iterator
numeros = [2, 8, 4, 7, 3]  # é um iteravel mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)


print(nome)
#print(next(nome))  # TypeError: 'str' object is not an iterator

print('it1', it1, type(it1))
print('it2', it2, type(it2))

print('len(it1)', len([it1]))
print('len(it2)', len([it2]))

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
#print(next(it1))  # passou do fim

print(next(it2))
print(next(it2))

print('-----------------------')

nome2 = 'borboleta'

for cada in nome2:
    print(f'{cada}')


print('-----------------------')
print('-----------------------')
