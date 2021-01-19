"""
Funções matemáticas e estatistica


math.prod -> retorna o produto de um container numérico

math.isqrt -> integer square root -> parte inteira da raiz quadrada

math.dist -> retorna a distância euclidiana entre dois pontos, 3D ou 2D

math.hypot -> retorna a hipotenusa, ou norma Euclidiana

statistics.fmean -> calcula a média de números reais

statistics.geometric_mean -> calcula a média geométrica de número reais.

statistics.multimode -> retorna o valor mais frequente em uma sequencia.


"""
import math

nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

print('1-----------------------')

print(math.isqrt(9))
print(math.isqrt(7))
print(math.sqrt(7))
print(math.isqrt(4))
print(math.isqrt(21))
print(math.sqrt(21))
print(math.isqrt(25))
#print(math.isqrt(1.44))  # dá erro
print(math.sqrt(1.44))

print('2-----------------------')

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

print('3-----------------------')

print(math.hypot(*p3d1))
print(math.hypot(*p2d1))

print('4-----------------------')
# Estatística

import statistics

valores_reais = [3.4, 10.5, 8.2, 7.89, 3.75]
valores_inteiros = [7, 3, 16, 20, 6]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

print('5-----------------------')

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

print('6-----------------------')

seq1 = 'Jeriquaquara'
seq2 = [2, 8, 7, 9, 7, 1, 7]
seq3 = [5, 8, 4, 9, 8, 3, 0, 2, 3, 1, 1]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))

print('7-----------------------')
print('8-----------------------')
