"""
Modulo Collections - Deque

é uma lista de alta performance

"""

# importando
from collections import deque

# criando deques
deq1 = deque('ipanema')

print(deq1)
print(list(deq1))
print('----------------\n')

# adicionando elementos no deque
deq1.append('s')   # adiciona no final
print(deq1)


deq1.appendleft('t')   # adiciona no começo
print(deq1)

print('----------------\n')

# removendo elementos
print(deq1.pop())      # remove e retorna o último elemento
print(deq1)

print(deq1.popleft())  # remove e retorna o primeiro elemento
print(deq1)
