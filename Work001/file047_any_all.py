"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o
iteravel está vazio.

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio,
retorna False.

"""

print(all([0, 1, 2, 3, 4]))  # todos são verdadeiros ?
print(all([1, 2, 3, 4]))  # todos são verdadeiros ?
print(all([]))
print(all(()))
print(all({}))
print(all(''))

print('---------------------------')

nomes1 = ['Ana', 'Arlinda', 'Alinalva', 'Atila']
nomes2 = ['Ana', 'Arlinda', 'Alinalva', 'Atila', 'Tomas']

print(all([cada[0] == 'A' for cada in nomes1]))
print(all([cada[0] == 'A' for cada in nomes2]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))  # verifica se 'aeiou' contem 'eio'

# OBS: um iteravel vazio convertido em boolean é False, mas o all() entende como True
print(all([letra1 for letra1 in 'xt' if letra1 in 'abcde']))

print([letra for letra in 'eio' if letra in 'aeiou'])
print([letra1 for letra1 in 'xt' if letra1 in 'abcde'])

print('--------------------------')

print(all([num for num in [4, 2, 10, 8] if num % 2 == 0]))
print(all([num for num in [4, 2, 5, 8] if num % 2 == 0]))

print(all([num % 2 == 0 for num in [4, 2, 5, 8]]))
print(all([num % 2 == 0 for num in [4, 2, 10, 8]]))

print('-------------------------------')

print(any([0, 1, 2, 3, 4]))
print(any([-10, -4, -2]))
print(any([0]))
print(any(['', False, (), {}]))
print(any(['', False, (), {}, 3]))
print(any([False]))

print('------------------------')

nomes3 = ['Fabiola', 'Flavia', 'Felicia', 'Fanny', 'Vanessa']

print(any([cada[0] == 'F' for cada in nomes3])) # pelo menos um

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
