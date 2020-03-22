# pasta5

"""
#01
numero1 = float(input('valor numero1: '))
numero2 = float(input('valor numero2: '))

numeros = [numero1, numero2]
maior = max(numeros)

print(f'o maior é {maior}')

#02
numero = float(input('digite um número : '))

if numero>0:
    print(numero**0.5)
else:
    print('número invalido')

#05
x = 1.0
y = 1

print(type(x))
print(type(y))

numero = float(input('digite um numero : '))

if numero % 2 == 0:
    print('numero par')
else:
    print('numero impar')


#06

#ver se é inteiro
numero1 = float(input('digite valor numero1: '))
numero2 = float(input('digite valor numero2: '))

verificar1 = float(numero1) - int(numero1)   # ver se é inteiro
verificar2 = float(numero2) - int(numero2)

if verificar1 == 0 and verificar2 == 0:
    print(f'o maior deles é {max([numero1, numero2])}')
    print(f'a diferença entre eles é : {abs(numero1 - numero2)}')
else:
    print('pelo menos um deles não é inteiro')


#08
from statistics import mean

i = 0
notas = []

for i in range(2):
    valor = float(input('nota : '))
    notas.append(valor)
    if (0 <= notas[i] <= 10) and len(notas) == 2:
        print(f'a média deles é {mean(notas)}')
    elif len(notas) == 2:
        print('pelo menos um valor inválido')


#11
numero = input('digite o valor do número : ') # toda entrada input é por padrão string

verificar1 = float(numero) - int(numero)
num = 0

if (float(numero) > 0) and verificar1 == 0:
    for i in range(len(numero)):
        num += float(numero[i])

    print(num)
elif float(numero) < 0:
    print('Número inválido')

#19
numero = input('digite um numero inteiro: ')

verificar = float(numero) - int(numero)

if verificar == 0:
    if ((int(numero)%15 == 0) is False) and (int(numero)%3==0 or int(numero)%5 == 0):
        print('ok')
    else:
        print('n ok')


#23

ano = input('Digite um ano: ')

verificar = float(ano) - int(ano)

if verificar == 0:
    if (int(ano)%400 == 0 or int(ano)%4 == 0) and not int(ano)%100 == 0:
        print(f'{ano} é ano bissexto')
    else:
        print(f'{ano} não é ano bissexto')



"""


# 26










""" 


numero = 4.2
verificar = float(numero) - int(numero)

if verificar == 0.0:
    print('é inteiro')
else:
    print('não é inteiro')
    
    
x = 1.0
y = 1
z = '1'
k = str(x)
t = str(y)

print(type(x))
print(type(y))
print(type(z))

print(k == t)


"""
