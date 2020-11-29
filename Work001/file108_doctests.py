"""
Doctests :

Doctests são testes que colocamos na docstring das funções/metodos python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

#saída:
3
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    file108_doctests
1 items passed all tests:
   1 tests in file108_doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.



"""


def soma(a, b):
    """soma os numeros a e b
    >>> soma(1, 2)
    3
    >>> soma(10,3)
    13
    """
    return a + b


print(soma(1, 2))  # roda como se fosse um teste
print(soma(3, 4))

"""
no terminal da pasta do arquivo: python -m doctest -v file108_doctests.py
"""

print('1-----------------')
# aplicando TDD


def duplicar(valores):
    """ duplicar os valores em uma lista
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])

    ['aa', 'bb', 'cc']
    >>> duplicar([True, None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    # pass antes
    #return []  # depois1
    return [2*elemento for elemento in valores]  # depois2

"""
fazer exemplo acima no terminal da pasta deste arquivo
"""

print('2-----------------')
# Erro inesperado


def fala_oi():
    """Fala oi
    >>> fala_oi()
    'oi'
    """
    # se invés de 'oi' fosse "oi" haveria erro
    return "oi"

"""
obs: Dentro do doctest, o python não reconhece string com aspas duplas. Precisa ser aspas simples.
"""

print('3-----------------')


def verdade():
    """ Retorna verdade
    >>> verdade()
    True
    """
    # após esse True na mesma linha não deve haver espaço em outras ides pois há erro. no pycharm há se houver espaços + comentarios.
    return True


"""
sublime text
"""

print('4-----------------')
print('5-----------------')

