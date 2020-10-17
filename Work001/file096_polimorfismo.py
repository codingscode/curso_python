"""
POO:
Polimorfismo  :

Poli (Muitos)
Morfis (Formas)


"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    #def falar(self): descomentar depois
    #    print(f'{self._Animal__nome} fala #rsqw..fsdfsdf')


felix = Gato('Felix')
felix.comer()
felix.falar()

aladin = Cachorro('Aladin')
aladin.comer()
aladin.falar()

mickey = Rato('Mickey')
mickey.comer()
#mickey.falar()  #  NotImplementedError: A classe filha precisa implementar este método

print('-----------------------------------------')
print('-----------------------------------------')
