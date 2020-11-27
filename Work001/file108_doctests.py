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
print('2-----------------')
