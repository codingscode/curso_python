"""
Por que testar nosso código

Testes automatizados

- Reduzir bugs(problemas) no código existente.
- Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos.
- Testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos.
- Testes garantem que refatoração que costumamos fazer não tragam novos bugs.


"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        return f'{self.__nome} está miando...'


animal1 = Gato('felix')

print(animal1.nome)
print(animal1.miar())

