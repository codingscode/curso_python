"""
Entendendo *args

É um parametro como outro qualquer
*args coloca os valores extras informados como entrada em uma uma tupla. Então desde
já lembre-se que tuplas são imutáveis.

argumentos em args não são obrigatórios

"""


def soma_todos_numeros(n1=0, n2=0, n3=0):
    return n1 + n2 + n3


print(soma_todos_numeros(4, 5, 6))
print(soma_todos_numeros(4, 5))
#print(soma_todos_numeros(1, 3, 2, 4))  # typeError
print('------------------')
# *args


def somando(*args):
    print(args)


somando()
somando(1)
somando(1, 2)
somando(1, 2, 3)
somando(1, 2, 3, 4)
print('------------------')


def somando2(*args):
    total = 0
    for numero in args:
        total += numero
    return total


print(somando2())
print(somando2(1))
print(somando2(1, 2))
print(somando2(1, 2, 3))
print(somando2(1, 2, 3, 4))
print('--------------------')


def somando3(*args):
    return sum(args)


print(somando3())
print(somando3(1))
print(somando3(1, 2))
print(somando3(1, 2, 3))
print(somando3(1, 2, 3, 4))
print(somando3(1.5, 1.2, 3.6, 4.2))
print('--------------------')


def com_soma(nome, email, *args):
    return f'{nome}, {email}, {sum(args)}'


print(com_soma('simon', 'simon@'))
print(com_soma('paul', 'paul@', 1.4, 3.2, 7.1))
print(com_soma('shin', 'shin@', 3, 2, 1))
print(com_soma('vicente', 'vicente@', 0, 2, 5))
print('-----------------------------\n')


def verificar_info(*args):
    if 'Python' in args and 'Curso' in args:
        return 'Bem vindo ao curso Python'
    return 'você não faz curso Python'


print(verificar_info())
print(verificar_info(1, True, 'Python', 'Curso'))
print(verificar_info(False, 1.5, 'java', True, 3))

print('-------------------\n')


def somartodos(*args):
    print(f'quem é args: {args}')
    return sum(args)


minha_lista1 = [4, 1, 0, 7]
minha_lista2 = [3, 0, 10, 2]
print(somartodos())
print(somartodos(1, 2, 3))
#print(somartodos(minha_lista1))  # dá erro  entende como  ([4, 1, 0, 7],)

# desempacotador
print(somartodos(*minha_lista2))
# OBS: O asteristo (*) serve para que informemos ao Python que estamos passando como argumento
# uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados.
