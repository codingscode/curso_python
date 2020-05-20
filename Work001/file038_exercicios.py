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


#12
num = int(input('digite um número inteiro positivo: '))

#n = 123
#para_string = str(n)
#print(para_string)
#print(para_string[0])
#print(para_string[1])
#print([float(para_string[i:i+1]) for i in range(0, len(para_string), 1)])


def somardigitos(numero):
    if numero > 0:
        lista = [int(str(numero)[i:i + 1]) for i in range(0, len(str(numero)), 1)]
        return f'soma dos dígitos: {sum(lista)}'
    return 'número inválido'


print(somardigitos(num))


# 14
dist = float(input('digite a distancia percorrida: '))
lit = float(input('digite a quantidade de litros gastos: '))


def carro(distancia, litros):
    consumo = distancia/litros
    if consumo < 8:
        return 'venda o carro!'
    elif 8 <= consumo < 14:
        return 'econômico'
    elif consumo > 12:
        return 'supereconomico'


print(carro(dist, lit))

#16
q = int(input('quantos traços: '))


def tracos(numero):
    re = ''
    re += '=' * numero
    return re


print(tracos(q))


#17
numero1 = int(input('digite o 1º numero: '))
numero2 = int(input('digite o 2º numero: '))


def somarnumeros(num1, num2):
    maior = max([num1, num2])
    menor = min([num1, num2])
    soma = 0
    for cada in range(menor+1, maior):
        soma += cada
    return soma


print('soma do intervalo:', somarnumeros(numero1, numero2))


# 19

import math

entrada = int(input('digite um número inteiro e positivo: '))

div = []


def seusdivisores(numero, variacao=0):
    divisores = []
    while numero - variacao >= 1:
        if numero % (numero - variacao) == 0:
            divisores.append(numero - variacao)
        variacao += 1
    return divisores


div = seusdivisores(entrada)
print(div)


def seusprimos(num):
    lista = seusdivisores(num)
    primos = []
    for cada in lista:
        if len(seusdivisores(cada, 0)) == 2:
            primos.append(cada)
    return primos


print(f'fatores primos de {entrada} é : {seusprimos(entrada)}')
print(f'maior fator primo de {entrada} é : {max(seusprimos(entrada))}')
print(f'logaritmo de 27 na base 3 é : {math.log(27, 3)}')


"""



#20











"""











"""
