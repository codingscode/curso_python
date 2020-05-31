"""
Map

Map ≠ mapas

- mapeamento função valor
- Com map, fazemos mapeamento de valores função.



"""

import math


def area(raio):
    return math.pi * raio**2


print(area(2))
print(area(1))
print('---------------------')

raios = [0.5, 3, 4.2, 8]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

print('------------------')
# Forma 2: usando Map
areas2 = map(area, raios)  #  função/um iteravel
print(list(areas2))
print(areas2)
print(list(areas2)) # é usado apenas uma vez
print(type(areas2))
print(type(area))
print(type(raios))

print('------------------')

# Forma 3: Map com lambda
print(list(map(lambda r: math.pi * r ** 2, raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.
print('------------------')

"""
Para fixar Map
Temos dados iteraveis

dados: a1, a2, ..., an

Temos uma função:

Função: f(x)

Utilizamos a função map(f, dados) onde map irá 'mapar' cada elemento dos dados e aplicar a função.

O Map object: f(a1), f(a2), f(...), ..., f(an)

"""

cidades = [('campo grande', 31), ('porto alegre', 23), ('rio de janeiro', 34), ('teresina', 38), ('nova york', 12)]

print(cidades)

# f = 9/5 * (celsius) + 32

c_para_f = lambda dado: (dado[0], (9/5)*dado[1] + 32)

print(list(map(c_para_f, cidades)))
