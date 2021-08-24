"""
POO :
MRO - Method resolution order

Resolução de ordem de métodos -> é a ordem de execução dos métodos (quem será executado primeiro)
Em Python, nós podemos conferir a ordem de execução dos métodos (MRO) de 3 formas:
- Via propriedade da classe __mro__
- Via metodo mro()
- Via help

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

    #def cumprimentar(self):  #  experimentar descomentar
    #    return f'Pinguim'


linu = Pinguim('Pingo')
print(linu.andar())
print(linu.nadar())
print(linu.cumprimentar())
"""
saída:
Pingo está andando
Pingo está nadando.
Eu sou Pingo do mar

"""

print('1-----------------------------------------')

from file095_MRO import Pinguim

print('2-----------------------------------------')

print(Pinguim.__mro__)

print('3-----------------------------------------')

print(Pinguim.mro())

print('4-----------------------------------------')

help(Pinguim)

print('5-----------------------------------------')
print('6-----------------------------------------')
