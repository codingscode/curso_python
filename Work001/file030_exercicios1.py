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



#24
from operator import itemgetter

todos = []
mbaixo = 0
malto = 0


def extrair(lista):
    return list(map(itemgetter(1), lista))  # 1 é indice da lista de cada elemento-lista


for i in range(10):
    numerox = float(input('numero: '))
    alturax = float(input('altura: '))
    par = [numerox, alturax]
    todos.append(par)

#for numero, altura in todos:
#    alturas.append(altura)

print(f'todos: {todos}')
print(f'alturas: {extrair(todos)}')

mbaixo = min(extrair(todos))
malto = max(extrair(todos))

print(f'mbaixo: {mbaixo}, seu numero: {todos[extrair(todos).index(mbaixo)][0]}')
print(f'malto: {malto}, seu numero: {todos[extrair(todos).index(malto)][0]}')


#25

quantidade = 99

atual = 1
valores = []

while len(valores) <= quantidade:
    if (atual % 7 == 0) or (int(repr(atual)[-1]) == 7):  # usado para pegar o nth dígito numero
        valores.append(atual)
    atual += 1

print(len(valores))
print(valores)


#27

quantidade = 10

valores = []
ordem = 0

primos = []

while len(valores) <= quantidade:
    valor = int(input(f'{ordem+1}º valor: '))
    valores.append(valor)
    ordem += 1

print(valores)


def primo(numero):
    delta = 0
    divisores = []
    while numero - delta >= 1:
        if numero % (numero - delta) == 0:
            divisores.append((numero - delta))
        delta += 1
    if len(divisores) == 2:
        return True
    else:
        return False

#print(primo(4))


for cada in valores:
    if primo(cada) is True:
        primos.append(cada)

print(f'primos: {primos}')

for cada in primos:
    print(f'{cada} sua posição: {valores.index(cada)}')


#30
    # 2 vetores de 10 elementos
quant_em_cada = 4

conjunto1 = set()
conjunto2 = set()

while len(conjunto1) < quant_em_cada:
    valor = int(input(f'{len(conjunto1) + 1}º valor: '))
    conjunto1.add(valor)

while len(conjunto2) < quant_em_cada:
    valor = int(input(f'{len(conjunto2) + 1}º valor: '))
    conjunto2.add(valor)

print(f'conjunto1: {conjunto1}')
print(f'conjunto2: {conjunto2}')

intersecao = conjunto1.intersection(conjunto2)
uniao = conjunto1 | conjunto2
soconjunto1 = conjunto1.difference(conjunto2)
soconjunto2 = conjunto2.difference(conjunto1)

print(f'intersecao: {intersecao}')
print(f'uniao: {uniao}')
print(f'somente conjunto1: {soconjunto1}')
print(f'somente conjunto2: {soconjunto2}')


#33



#36

quantidade = 4
valores = set()

for i in range(4):
    valor = int(input(f'{i+1}º valor: '))
    valores.add(valor)

print(valores)
ordenado = sorted(valores)
print(ordenado)






"""



#35



"""


x = {1, 2, 4, 10, -3}

print(x)

for cada in x:
    print(cada)


numero = 36528

print(int(repr(numero)[-1]))






"""
