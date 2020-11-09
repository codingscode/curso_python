"""
Pickle :
A função do Pickle é realizar o seguinte processo:
Objeto Python -> Binarização
Binarização -> Objeto Python
Este processo é chamado de serialização/deserialização

#Obs: o modulo Pickle não seguro contra dados maliciosos e desta forma não é recomendado trabalhar
com arquivos pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.




"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        return f'{self.__nome} esta comendo'


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        return f'{self._Animal__nome} esta miando'


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        return f'{self._Animal__nome} esta latindo'


gato1 = Gato('felix')
cachorro1 = Cachorro('aladin')

with open('file101_pickle_criandoarquivo1.pickle', 'wb') as arquivo1:  # o .pickle nao é necessario
    pickle.dump((gato1, cachorro1), arquivo1)





