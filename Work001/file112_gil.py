"""
Gil - python global interpreter lock

"""

import sys

a = []
b = a
print(sys.getrefcount(a))  # quantidade de referencias

print('1-----------')