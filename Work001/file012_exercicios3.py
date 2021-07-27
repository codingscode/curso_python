# pasta 06

"""


#01

base = 3

for i in range(5):
    print(f'{i+1}º : {base + i*3}')


#02

for i in range(10):
    print(i+1, i+1, i+1)

print('--------')

ind = 1
while ind < 10:
    print(ind)
    ind += 1

print(f'ind fora: {ind}')
print('-----------------')


# 03

numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

#05

valor = 0
valores = []
soma = 0

for i in range(3):
    valor = input('digite um valor: ')
    valores.append(int(valor))

soma = sum(valores)

print(f'soma: {soma}')


#06

from statistics import mean

numeros = []

for i in range(4):
    numero = float(input('digite um número: '))
    numeros.append(numero)

medianumeros = mean(numeros)

print(f'media: {medianumeros}')


#07
from statistics import mean

valor = 0
valores = []
verificar = float(valor) == int(valor)

for i in range(5):
    valor = input('digite valor: ')
    if verificar and (int(valor) > 0):
        valores.append(int(valor))

media = mean(valores)

print(media)

#08

numeros = []

for i in range(5):
    numero = float(input('digite um número: '))
    numeros.append(numero)

print(f'o menor número é : {min(numeros)}')
print(f'o maior número é : {max(numeros)}')


#09

n = float(input('digite um valor inteiro para n : '))
verificar = n == int(n)
impar = 1

if verificar:
    for i in range(int(n)):
        print(impar)
        impar += 2
else:
    print('valor inválido')


#12

n = float(input('digite um número inteiro n positivo : '))

numeros = []

if (n == int(n)) and (n > 0):
    for i in range(int(n + 1)):
        numeros.append(i)

print(numeros[::-1])


#17

n = float(input('digite um número inteiro n positivo : '))

numeros = []

if (n == int(n)) and (n > 0):
    for i in range(int(n)):
        numeros.append(i)

print(numeros)
print(f'soma : {sum(numeros)}')


#18

n = float(input('quantidade de numeros : '))
numeros = []

if n == int(n):
    for i in range(int(n)):
        numero = float(input('digite um número: '))
        numeros.append(numero)
else:
    print('quantidade não inteira')

print(numeros)
print(f'o maior número é : {max(numeros)}')

print(f'o {max(numeros)} aparece {numeros.count(max(numeros))} vezes')


#19
n = int(input('digite um número entre 100 e 999: '))

if 100 < n < 999:
    pstring = str(n)
    for i in range(len(pstring)):
        print(f'{i + 1}º algarismo: {pstring[i]}')


#20

numero = 0
inteiros = []
pares = []

while numero != 100:
    numero = int(input('digite um número: '))
    inteiros.append(numero)

print(inteiros)
print(f'número de dados lidos: {len(inteiros)}')

for i in range(len(inteiros)):
    if inteiros[i] % 2 == 0:
        pares.append(inteiros[i])

print(pares)
print(f'número de dados pares: {len(pares)}')


#23

numero = float(input('digite um número inteiro e positivo: '))
indice = 0
divisores = []

if (numero == int(numero)) and numero > 0:
    valores = []
    for i in range(1, int(numero + 1)):
        valores.append(i)
        armazenar = valores
    for j in range(len(armazenar)):
        if numero % armazenar[j] == 0:
            divisores.append(armazenar[j])
else:
    print('valor inválido')


print(divisores)


#24

numero = float(input('digite um número inteiro e positivo: '))
indice = 0
divisores = []

if (numero == int(numero)) and numero > 0:
    valores = []
    for i in range(1, int(numero+1)):
        valores.append(i)
        armazenar = valores
    for j in range(len(armazenar)):
        if numero % armazenar[j] == 0:
            divisores.append(armazenar[j])
else:
    print('valor inválido')


print(divisores)
print(f'soma de seus divisores com exceção dele mesmo é  {sum(divisores[:-1])}')

# 25

num = 0
numeros = []

for i in range(1, 11):
    if (i % 15 == 0) or (i % 5 == 0) or (i % 3 == 0):
        numeros.append(i)

print(numeros)
soma = sum(numeros)
print(soma)

# 26

numero = int(input('digite um número: '))

plus = 0
resposta = 1
# 1º multiplo de 11, 13 ou 17


while (resposta % 11 == 0 or resposta % 13 == 0 or resposta % 17 == 0) is False:
    resposta = numero + plus
    plus += 1


print(f'resposta : {resposta}')


#35

print('digite um intervalo: ')
inicio = int(input('digite um inicio: '))
final = int(input('digite um fim: '))

plus = 0
impares = []
soma = 0
atual = 0

if (final > inicio):
    while atual < final - 1:
        if (inicio+plus) % 2 == 1:
            atual = inicio + plus
            impares.append(atual)
        plus += 1

else:
    print('final deve ser maior que inicio')

print(impares)
soma = sum(impares)
print(soma)


#46
      # achar número
from random import randrange

resposta = 0

aleatorio = randrange(1, 1001) # de 1 a 1000 inclusivo

while aleatorio != resposta:
    resposta = int(input('digite um valor: '))
    if resposta < aleatorio:
        print('é maior')
    elif resposta > aleatorio:
        print('é menor')
    else:
        print('achou')

print(f'resposta : {aleatorio}')


#50

a_chico = 1.5
plus_chico = 0.02

a_ze = 1.1
plus_ze = 0.03

anos = 0

while a_ze <= a_chico:
    a_chico += plus_chico
    a_ze += plus_ze
    anos += 1


print(f'idade chico: {a_chico}')
print(f'idade ze: {a_ze}')
print(f'anos: {anos}')

# 52
saque = int(input('digite o valor do saque: '))
# por exemplo 188

lado_a_lado = []

n_100 = saque // 100
r_100 = saque % 100  # sobra 88
n_50 = r_100 // 50
r_50 = r_100 % 50   # sobra 38
n_20 = r_50 // 20
r_20 = r_50 % 20    # sobra 18
n_10 = r_20 // 10
r_10 = r_20 % 10   # sobra 8
n_5 = r_10 // 5
r_5 = r_10 % 5     # sobra 3
n_2 = r_5 // 2
r_2 = r_5 % 2   # sobra 1
n_1 = r_2 // 1
r_1 = r_2 % 1  # sobra 0

tipos = ['notas de 100', 'notas de 50', 'notas de 20', 'notas de 10', 'notas de 5', 'notas de 2', 'notas de 1']
notas = [n_100, n_50, n_20, n_10, n_5, n_2, n_1]
soma = sum(notas)

for i in range(len(notas)):
    lado_a_lado.append(f'{tipos[i]}: {str(notas[i])}')  # tipos[i] + ': ' + str(notas[i])

print(tipos)
print(notas)
print(lado_a_lado)
print(f'total de notas {soma}')


#53

n = int(input('Digite o número de linhas: '))
x = 1  #Fila actual que es el mismo número que el número de columnas que tiene que tener esa fila
y = 1   # Número que tem que imprimir
z = 1   # Número de colunas em cada linha
frase = ''

for x in range(1, n + 1):
    for z in range(1, x + 1):  #z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)
        frase += (str(y) + ' ')
        y += 1
    print(frase)
    frase = ''

# https://altocodigo.blogspot.com/2018/06/triangulo-de-floyd-en-python.html

#54

numero = int(input('digite um numero inteiro maior que 1: '))
delta = 0
divisores = []
inico = 0

while (numero - delta) >= 1:  # (numero - delta) >= 1
    if numero % (numero - delta) == 0:
        divisores.append((numero - delta))
    delta += 1

print(f'divisores: {divisores}')

if len(divisores) == 2:
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um número primo')


# 55

quantidade = int(input('digite a quantidade: '))

atual = 0  # numero atual
delta = 0  # variacao
atual_divisores = []  # divisores do numero atual
n_primos = []  # numeros primos


def testar(x, delta2):
    while (x - delta2) >= 1:
        if x % (x - delta2) == 0:
            atual_divisores.append(x - delta2)
        delta2 += 1

    if len(atual_divisores) == 2:
        # print(f'{x} é um número primo')
        return True
    elif len(atual_divisores) > 2:
        # print(f'{x} não é um número primo')
        return False

# print(testar(29, 0))


while len(n_primos) <= quantidade-1:
    if testar(atual, delta) is True:
        n_primos.append(atual)
    atual_divisores.clear()
    atual += 1

print(f'os {quantidade}º primos: {n_primos}')
print(f'sua soma é {sum(n_primos)}')


#while len(n_primos) <= quantidade:
#    for numero in range(2, 100):
#        atual = numero
#        if testar(atual, delta) is True:
#            n_primos.append(atual)
#        atual_divisores.clear()

#print(n_primos)

#for numero in range(2, 21):
#    atual = numero
#    if testar(atual, delta) is True:
#        n_primos.append(atual)
#    atual_divisores.clear()

#print(n_primos)


#for numero in range(2, 21):
#    atual = numero
#    print(f'{atual} : {testar(atual, delta)}')
#    atual_divisores.clear()


#56


atual = 0  # numero atual
delta = 0  # variacao
atual_divisores = []  # divisores do numero atual
n_primos = []  # numeros primos


def testar(x, delta2):
    while (x - delta2) >= 1:
        if x % (x - delta2) == 0:
            atual_divisores.append(x - delta2)
        delta2 += 1

    if len(atual_divisores) == 2:
        # print(f'{x} é um número primo')
        return True
    elif len(atual_divisores) > 2:
        # print(f'{x} não é um número primo')
        return False

# print(testar(29, 0))


for numero in range(2, 2000001):
    atual = numero
    if testar(atual, delta) is True:
        n_primos.append(atual)
    atual_divisores.clear()
    atual += 1

print(f'os {2000000}º primos: {n_primos}')
print(f'sua soma é {sum(n_primos)}')


#57

print('digites o intervalo a a b:')
v_a = int(input('digite o valor de a: '))
v_b = int(input('digite o valor de b: '))

atual = 0  # numero atual
delta = 0  # variacao
atual_divisores = []  # divisores do numero atual
n_primos = []  # numeros primos


def testar(x, delta2):
    while (x - delta2) >= 1:
        if x % (x - delta2) == 0:
            atual_divisores.append(x - delta2)
        delta2 += 1

    if len(atual_divisores) == 2:
        # print(f'{x} é um número primo')
        return True
    elif len(atual_divisores) > 2:
        # print(f'{x} não é um número primo')
        return False

# print(testar(29, 0))


for numero in range(v_a, v_b + 1):
    atual = numero
    if testar(atual, delta) is True:
        n_primos.append(atual)
    atual_divisores.clear()
    atual += 1

print(f'os primos do intervalo: {n_primos}')
print(f'quantidade: {len(n_primos)}')


#58

print('digites o intervalo a a b:')
v_a = int(input('digite o valor de a: '))
v_b = int(input('digite o valor de b: '))

atual = 0  # numero atual
delta = 0  # variacao
atual_divisores = []  # divisores do numero atual
n_primos = []  # numeros primos


def testar(x, delta2):
    while (x - delta2) >= 1:
        if x % (x - delta2) == 0:
            atual_divisores.append(x - delta2)
        delta2 += 1

    if len(atual_divisores) == 2:
        # print(f'{x} é um número primo')
        return True
    elif len(atual_divisores) > 2:
        # print(f'{x} não é um número primo')
        return False

# print(testar(29, 0))


for numero in range(v_a, v_b + 1):
    atual = numero
    if testar(atual, delta) is True:
        n_primos.append(atual)
    atual_divisores.clear()
    atual += 1

print(f'os primos do intervalo: {n_primos}')
print(f'a soma é : {sum(n_primos)}')




"""


