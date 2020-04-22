"""
pasta 7 pdf 1





# 01

A = [1, 0, 5, -2, -5, 7]
print(A)

soma_especifica = A[0] + A[1] + A[5]
print(soma_especifica)

A[4] = 100
print('---------------')

for cada in A:
    print(cada)

print('---------------\n')

# 04

quantidade = 8
valores = []
x = 0
y = 0

for indice in range(8):
    cada = int(input(f'{indice + 1}º valor: '))
    valores.append(cada)

print(valores)

x = int(input('posicao indice x: '))
y = int(input('posicao indice y: '))

try:
    if 0 <= x or y <= 8:
        print(f'valores[x]: {valores[x]}, valores[y]: {valores[y]}')
        print(f'soma: {valores[x] + valores[y]}')
    else:
        print('pelo menos um indice está fora do intervalo')
except:
    print('pelo menos um indice está fora do intervalo')


#05

valores = []
pares = []

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)

for cada in valores:
    if cada % 2 == 0:
        pares.append(cada)

print(f'pares: {pares} || quantos: {len(pares)}')


# 07

print('digite 10 números inteiros: ')
valores = []

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)
print(f'maior: {max(valores)}, seu indice: {valores.index(max(valores))}')

#08

valores = []

for indice in range(6):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(f'ordem inversa {valores[::-1]}')


#11
valores = []
contar_negativo = 0
soma_positivos = 0

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

for cada in valores:
    if cada < 0:
        contar_negativo += 1
    else:
        soma_positivos += cada

print(f'quantidade de negativos: {contar_negativo}')
print(f'soma dos positivos: {soma_positivos}')

#14
from functools import reduce

valores = []

for indice in range(4):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)

#
verificar = all(cada == valores[0] for cada in valores)

print(verificar)

#14.2

from functools import reduce

valores = []

for indice in range(4):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)

# reduce(function, sequence[, initial]) -> value
def funcao(acumulador, atual):
    return acumulador is atual


#verificar = all((valores[indice] == valores[indice]) for indice in range(len(valores)))

verificar = reduce(funcao, valores)

print(verificar)
#https://thispointer.com/python-check-if-all-elements-in-a-list-are-same-or-matches-a-condition/


#15

elementos = set()

for i in range(20):
    valor = int(input(f'{i+1}º valor: '))
    elementos.add(valor)

print(f'{elementos} || {type(elementos)}')

#17

valores = []

for i in range(5):
    valor = int(input(f'{i+1}º valor: '))
    if valor < 0:
        valores.append(0)
    else:
        valores.append(valor)

print(valores)


#18

x = int(input('valor para x: '))

numeros = []
contador = 0

for i in range(5):
    valor = int(input(f'{i+1}º valor: '))
    numeros.append(valor)

print(numeros)

for cada in numeros:
    if cada % x == 0:
        contador += 1
    else:
        contador += 0

print(f'números de múltiplos de {x}: {contador}')


"""




#24

























"""




"""






