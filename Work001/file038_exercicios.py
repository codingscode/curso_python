"""


#01

def o_dobro(numero):
    print(numero*2)


o_dobro(3)

#02

import locale
from datetime import date
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

hoje = date.today()

print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%B %d, %Y"))
print(hoje.strftime("%d de %B de %Y"))

print(hoje.strftime("%m/%d/%y"))
print(hoje.strftime("%b-%d-%Y"))

#03

numero = float(input('digite um número: '))

def verificar(num):
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


print(verificar(numero))

#04
numero = float(input('digite um número: '))

def qdperfeito(num):
    if num**0.5 - int(num**0.5) == 0:
        return f'{num} é um quadrado perfeito'
    return f'{num} não é um quadrado perfeito'


print(qdperfeito(numero))

#10

quantidade = int(input('quantidade de números: '))
numeros = []

while len(numeros) < 3:
    valor = int(input(f'{len(numeros) + 1}º valor: '))
    numeros.append(valor)

print(numeros)
print(f'maior: {max(numeros)}')

#11
import math
from math import isnan
from statistics import mean

notas = []
while len(notas) < 3:
    nota = float(input(f'{1 + len(notas)}ª nota: '))
    notas.append(nota)

letra = input('digite uma letra: ')
notas.append(letra)

notas = tuple(notas)

print(notas)


def calcular(*args):
    if args[-1] == 'a':
        return mean(args[:-1])
    if args[-1] == 'p':
        return (args[0]*5 + args[1]*3 + args[2]*2)/10
    else:
        return 'comando inválido'


print(calcular(*notas))

print('x' == (' x  ').strip())
print('1' == float('1'))
print('aqui ','1' == 1)
print(1 != 1)
print('1' != '1')
print('ver 1', math.isnan(float(3)))
print('ver 2')
print(type('cc'))
print(1 == float('1'))
print('isnt', isinstance('x', int))
print('isnt', isinstance(1.2, float))
print('isnt', isinstance(2, int))


"""






#12











"""































"""