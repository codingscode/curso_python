"""
POO - Metodo super

O metodo super() se refere a super classe.

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'animal {self.__nome} emite: {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)  #  ou Animal.__init__(self, nome, especie)
        self.__raca = raca
        super().faz_som('miau miau')


chiquinho = Gato('chiquinho', 'felino', 'siames')
chiquinho.faz_som('miau')
print('---------------------')
