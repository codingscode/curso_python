"""
Funções de maior grandeza -> Higher Order Functions (HOF)


O que isso signidica?
Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras
funções como resultado ou mesmo que podemos passar função como argumentos para outras funções, e até
mesmo criar variaveis do tipo de funções nos nossos programas.


"""

# Exemplo - definindo as funções


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 2, somar))
print(calcular(4, 2, subtrair))
print(calcular(4, 2, multiplicar))
print(calcular(4, 2, dividir))
print('-----------------')

# Nested Functions - Funções Aninhadas (funções dentro de funções)

from random import choice


def saudacao(pessoa):
    def humor():
        return choice(('E aí', 'Suma daqui', 'Gosto muito de você'))
    return f'{humor()} {pessoa}'


print(saudacao('silas'))
print(saudacao('felícia'))
print(saudacao('toni'))
print('-----------------')

# Retornando funções de outras funções

def fazer_rir():
    def rir():
        return choice(('haha', 'kkk', 'hehe'))
    return rir


rindo = fazer_rir()
print(rindo)
print(rindo())

#obs: inner functions (funções internas / nested functions) podem acessar o escopo de funções
# mais externas
