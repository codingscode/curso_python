"""
POO - Herança Multipla

Herança multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança multipla pode ser feita de duas maneiras:
   - Por Multiderivação Direta;
   - Por Multiderivação Indireta;

OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos
 os atributos e métodos das super classes.


"""

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivação Indireta


class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class MultiDerivada2(Base6):
    pass


print('----------------------------')


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


baleia = Aquatico('Mobydick')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Peba')
print(tatu.andar())
print(tatu.cumprimentar())

linu = Pinguim('Pingo')
print(linu.andar())
print(linu.nadar())
print(linu.cumprimentar())  #  ??????  Method Resolution Order (MRO) // Eu sou Pingo do mar // Aquatico vem primeiro

print('---------------------')

print(f'Pingo é instancia de Pinguim ? : {isinstance(linu, Pinguim)}')
print(f'Pingo é instancia de Aquatico ? : {isinstance(linu, Aquatico)}')
print(f'Pingo é instancia de Terrestre ? : {isinstance(linu, Terrestre)}')
print(f'Pingo é instancia de object ? : {isinstance(linu, object)}')
print(f'Pingo é instancia de str ? : {isinstance(linu, str)}')
print(f'Pingo é instancia de Animal ? : {isinstance(linu, Animal)}')
print(f'Peba é instancia de Aquatico ? : {isinstance(tatu, Aquatico)}')

"""
(1)
class Pessoa:
    pass
    
(2)
class Pessoa(object):
    pass
    
(1) e (2) são a mesma coisa    
"""

print('---------------------')
print('---------------------')
