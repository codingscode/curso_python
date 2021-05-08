"""
Tipos em comentarios

"""

import math

"""
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(5))  # nao dá erro
#print(circunferencia('geek'))

"""


def circunferencia(raio):  # def circunferencia(raio: float) -> float:
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(5))  # nao dá erro
print(circunferencia('geek'))  # no terminal deveria dar erro


"""
testar tambem no terminal: mypy file122_tipos_em_comentarios.py
"""
print('1---------------------')


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


print(cabecalho(texto=43, alinhamento='geek'))
print(cabecalho(texto=43, alinhamento=0))
print('2---------------------')


def cabecalho2(
    texto,  # type: str
    alinhamento=True  # type: bool
):  # type:  (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


print(cabecalho2(texto=42, alinhamento='geek'))

nome = 'Geek University'  # type: str

print('3---------------------')
