"""
Generators (Generator Expression)

= tuple comprehensions


"""

nomes = ['Cecília', 'Caroline', 'Cassia', 'Carl', 'Roberto']

print(any(nome[0] == 'C' for nome in nomes))  # pelo menos 1
print(any([nome[0] == 'C' for nome in nomes])) # aqui não é generator
print(any((nome[0] == 'C' for nome in nomes))) # aqui é generator

print((nome[0] == 'C' for nome in nomes))   # é generator
print([nome[0] == 'C' for nome in nomes])
print({nome[0] == 'C' for nome in nomes})

print('-------------------------------')

generator = (nome[0] == 'C' for nome in nomes)
print(tuple(generator))   # usado só uma vez
print(tuple(generator))

print('-------------------------------')

# list comprehension
res1 = [nome[0] == 'C' for nome in nomes]

print(type(res1))
print(res1)

# generator  -> é mais performático
res2 = (nome[0] == 'C' for nome in nomes)

print(type(res2))
print(res2)

print('-------------------------------')

from sys import getsizeof

# getsizeof() -> retorna a quantidade de bytes em memória do elemento passado como parametro

print(getsizeof('Python Coding'))  # quanto de bytes ocupa em memória
print(getsizeof(2))
print(getsizeof(14))
print(getsizeof(True))

print('-------------------------------')

# Gerando uma lista de numeros com List comprehension
list_comp = getsizeof([x*10 for x in range(50)])

# Gerando uma lista de numeros com Set comprehension
set_comp = getsizeof({x*10 for x in range(50)})

# Gerando uma lista de numeros com Dictionary comprehension
dict_comp = getsizeof({x: x*10 for x in range(50)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(x*10 for x in range(50))

print('mesma tarefa, gasto em memória:')
print(f'list comprehension: {list_comp} bytes')
print(f'set comprehension: {set_comp} bytes')
print(f'dictionary comprehension: {dict_comp} bytes')
print(f'generator expression: {gen} bytes')

print('-------------------------------')

# Iterando com Generator Expression

gen2 = (cada * 10 for cada in range(10))

print(gen2)
print(type(gen2))

for num in gen2:
    print(num)
