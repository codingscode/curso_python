"""
Gil - python global interpreter lock

"""

import sys

a = []
b = a
print(sys.getrefcount(a))  # quantidade de referencias
print(dir(sys))
print('1-----------')