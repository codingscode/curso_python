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


"""





#08


