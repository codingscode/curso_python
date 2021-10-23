"""
Gil - python global interpreter lock

"""

import sys

a = []
b = a

print(f'1: {sys.getrefcount(a)}')  # quantidade de referencias

print(f'2: {dir(sys)}')
print(f'3: {len(dir(sys))}')
print('1-----------')
print(f'4: {type(sys.getrefcount(a))}')
