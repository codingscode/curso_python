"""
Argumentos somente posicionais

"""

valor = '14.7'
print(float(valor))

"""
no terminal: help(float)
"""

print('1-------------------')


def cumprimentar_v1(nome):
    return f'Olá {nome}'


print(cumprimentar_v1('python'))
print(cumprimentar_v1(nome='python'))

print('2-------------------')


def cumprimentar_v2(nome, /):  # tudo antes de '/' é somente posicional
    return f'Olá {nome}'


print(cumprimentar_v2('python'))
#print(cumprimentar_v2(nome='python'))  # dá erro

print('3-------------------')


def cumprimentar_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimentar_v3('python'))
print(cumprimentar_v3('javascript', mensagem='Como vai'))
print(cumprimentar_v3('Felícia', mensagem='Bem vinda'))
#print(cumprimentar_v3(nome='python'))  # dá erro

print('4-------------------')


def cumprimentar_v4(nome, mensagem='Aê', /):
    return f'{mensagem} {nome}'


print(cumprimentar_v4('python'))
print(cumprimentar_v4('Olga', 'Bem vinda'))
#print(cumprimentar_v4('javascript', mensagem='Como vai'))  # dá erro
#print(cumprimentar_v4(nome='python'))  # dá erro


print('5-------------------')


def cumprimentar_v5(*, nome):  # tudo depois de '*' é somente não posicional
    return f'Olá {nome}'


print(cumprimentar_v5(nome='pythonista'))
#print(cumprimentar_v5('pyhonico'))  # dá erro

print('6-------------------')


def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v6('Geek', mensagem1='Aê', mensagem2='bom dia'))
print(cumprimentar_v6('Geek', mensagem2='bom legal pra ti'))
#print(cumprimentar_v6('Geek', 'Oi', 'Vamos?'))  # dá erro
print(cumprimentar_v6('Geek', 'Oi', mensagem2="Como vai"))

print('7-------------------')
print('8-------------------')
