# pasta 06

"""
#01

base = 3

for i in range(5):
    print(f'{i+1} º : {base + i*3}')


#02

for i in range(10):
    print(i+1, i+1, i+1)

print('--------')

ind = 1
while ind < 10:
    print(ind)
    ind += 1

print(ind)
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

print(soma)


#06

from statistics import mean

numeros = []

for i in range(4):
    numero = float(input('digite um número: '))
    numeros.append(numero)

medianumeros = mean(numeros)

print(medianumeros)


#07
from statistics import mean

valor = 0
valores = []
verificar = float(valor) - int(valor)

for i in range(5):
    valor = input('digite valor: ')
    if verificar == 0 and (int(valor) > 0):
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
verificar = n - int(n)
impar = 1

if verificar == 0:
    for i in range(int(n)):
        print(impar)
        impar += 2
else:
    print('valor inválido')


#12

n = float(input('digite um número inteiro n positivo : '))

numeros = []

if (n == int(n)) and (n > 0):
    for i in range(int(n+1)):
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
        print(f'{i+1}º algarismo: {pstring[i]}')


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
    for i in range(1, int(numero+1)):
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



"""





#25























