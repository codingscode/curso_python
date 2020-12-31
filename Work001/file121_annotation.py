"""

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'*'*len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')


print(cabecalho('codando em python'))
print(cabecalho('usando django python', alinhamento=False))
print(cabecalho('code em python', alinhamento='geek'))  # agora checa

print('1-----------------')
"""
terminal da pasta do arquivo: mypy file121_annotation.py

file121_annotation.py:15: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
file121_annotation.py:60: error: Name '__annotations__' is not defined
file121_annotation.py:81: error: Cannot access "__init__" directly
file121_annotation.py:82: error: Cannot access "__init__" directly


"""

"""
Correto
texto: str

Incorreto
texto:str
texto : str

"""

import math


def circunferencia(raio: float) -> float:
    return 2*math.pi*raio


print(circunferencia.__annotations__)

print('2--------------')

nome: str = 'codando em python'
peso: float = 67.8

# não são duas declarações
ativo: bool
ativo = True   # preferivel ativo: bool = True

print(nome)
print(peso)
print(ativo)
print('**', __annotations__)

print('3-----------------')


class Pessoa:

    def __init__(self, nome2: str, idade2: int, peso2: float) -> None:
        self.__nome2: str = nome2
        self.__idade2: int = idade2
        self.__peso2: float = peso2

    def andar(self) -> str:  # def andar(self: Pessoa) -> str:  daria erro
        return f'{self.__nome2} está andando.'


p = Pessoa(nome2='Aladin', idade2=2, peso2=4)

print(p.__dict__)
#print(p.__annotations__)  # dá erro
print(p.andar.__annotations__)
print(p.__init__)
print(p.__init__.__annotations__)

print('4-----------------')
