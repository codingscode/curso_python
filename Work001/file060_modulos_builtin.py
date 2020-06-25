"""
Módulos Built-in
   -> modulos integrados que já vem com o python

https://docs.python.org/3/py-modindex.html


"""


"""
dir()
dir(__builtins__)
import randm
dir()

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
dir()
import math
dir()
math.pi
math.e

"""
