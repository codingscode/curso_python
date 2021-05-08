"""
Módulos Built-in
   -> modulos integrados que já vem com o python

https://docs.python.org/3/py-modindex.html

"""

"""
dir():
      ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys']

dir(__builtins__):
      ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

import random
dir():
      ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random', 'sys']

"""

# utilizando alias(apelidos) para modulos/funções

from random import random as importado

print(importado())
print('-------------')

# podemos importar todas as funções de um modulo utilizando o *
from random import *

print(randint(7, 10))
print('-------------')

from random import uniform as intervalo, shuffle as embaralhar

lista = ['pedra', 'papel', 'tesoura']

print(intervalo(1.2, 4))
embaralhar(lista)
print(lista)

print('-------------')
# costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (random, randint, shuffle, choice)

print(random())
print(randint(2, 6))
print(choice(['a', 'b', 'c', 'd']))

print('-------------')
"""
dir():
    ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys']

import math
dir():
    ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'sys']

math.pi:
    3.141592653589793
math.e:
    2.718281828459045
"""
