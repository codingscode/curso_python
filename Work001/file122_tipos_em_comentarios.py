"""
Tipos em comentarios

"""

import math


"""
def circunferencia(raio):
    # type  (float) -> float
    return 2 * math.pi * raio


print(circunferencia(5))  # nao dá erro
print(circunferencia('geek'))

"""


def circunferencia(raio):  # def circunferencia(raio: float) -> float:
    # type  (float) -> float
    return 2 * math.pi * raio


print(circunferencia(5))  # nao dá erro
#print(circunferencia('geek'))  # no terminal deveria dar erro


"""
testar tambem no terminal: mypy file122_tipos_em_comentarios.py
"""


def cabecalho(texto, alinhamento=True):
    # type (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'




