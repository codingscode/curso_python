"""
Funções com retorno




"""

numeros = [20, 8, 34, 15, 43]

retorno_de_pop = numeros.pop()

print(f'retorno de pop: {retorno_de_pop}')

impressao_print = print('oi')

print(f'retorno de impressao_print: {impressao_print}')
print('-------------------------')


def quadrado_7():
    print(7**2)   # aqui não é retorno, e sim impressão


ret = quadrado_7()  # chamando

print(f'ret: {ret}')

# OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None
print('-------------')

# refatorando função para te retorno
def triplo_de_4():
    return 3*4


ret2 = triplo_de_4()

print(f'ret2: {ret2}')
print(f'{triplo_de_4()} || seu tipo: {type(triplo_de_4())}')   # tipo do retorno
# OBS: Não precisamos necessariamente criar uma variavel para receber o retorno de uma
# função. Podemos passar a execução da função para outras funções ou mesmo para um print.

print('------------------------')

"""
Obs sobre a palavra reservada 'return'
1 - ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores


"""

# exemplo do 1

def numero_10():
    print('Estou sendo executado antes do retorno...')
    return 10
    print('Estou sendo executado após o retorno...')  # não é executada


print(numero_10())

print('----------------')

# exemplo do 2
def outra_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(outra_funcao())

print('-----------------')

# exemplo do 3

def outra_funcao2():
    return 30, 18, 6, 4


num1, num2, num3, num4 = outra_funcao2()

print(num1, num2, num3, num4)
print(outra_funcao2())

print('---------------------')

# criando função para jogar moeda
from random import random

def jogar_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
print('-----------------')

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim
# codificação desnecessário

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False


print(eh_impar())
