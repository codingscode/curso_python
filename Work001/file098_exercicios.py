"""
Exercicios da pasta


"""

"""
#01)
class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        return f'nome: {self.__nome}, endereco: {self.__endereco}, telefone: {self.__telefone}'


pessoa1 = Pessoa('magali', 'belo horizonte', 98782387)
print(pessoa1.__dict__)
print(pessoa1.imprimir())


"""


#03)


class Quadrado:

    def __init__(self, lado): # , area=0, perimetro=0
        self.__lado = lado
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        self.__area = self.__lado ** 2
        return self.__area

    def calcular_perimetro(self):
        self.__perimetro = self.__lado*4
        return self.__perimetro

    def imprimir(self):
        return f'lado: {self.__lado}, area: {self.__area}, perimetro: {self.__perimetro}'


quadrado1 = Quadrado(3)
print(quadrado1.__dict__)
print(quadrado1.imprimir())




