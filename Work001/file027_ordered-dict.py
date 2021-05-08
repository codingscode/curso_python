"""
Modulo Collections: Ordered Dict

OrderedDict -> É um dicionario que nos garante a ordem de inserção dos elementos


"""

# em dicionario a ordem de inserção de elementos nõa é garantida

dicionario_1 = {'c': 1, 'd': 2, 'a': 3, 'e': 4, 'b': 5}
print(dicionario_1)

for chave, valor in dicionario_1.items():
    print(f'{chave} : {valor}')

print('--------------------------\n')

# fazendo o import

from collections import OrderedDict

dicionario_2 = OrderedDict({'c': 1, 'd': 2, 'a': 3, 'e': 4, 'b': 5})

for chave, valor in dicionario_2.items():
    print(f'{chave} : {valor}')

print('-------------\n')

# Entendendo a diferença entre Dict e Ordered Dict

# dicionarios comuns
dicionario_3 = {'a': 1, 'b': 2}
dicionario_4 = {'b': 2, 'a': 1}

print(dicionario_3 == dicionario_4)  # True, já que a ordem n importa para o dicionario

ordenado_dicionario1 = OrderedDict({'a': 1, 'b': 2})
ordenado_dicionario2 = OrderedDict({'b': 2, 'a': 1})

print(ordenado_dicionario1 == ordenado_dicionario2)  # False, para o ordered-dict a ordem conta diferença












