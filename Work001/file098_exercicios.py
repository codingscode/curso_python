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

#03)
class Quadrado:

    def __init__(self, lado): 
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


# 05)
class Retangulo:

    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        self.__area = self.__lado1 * self.__lado2
        return self.__area

    def calcular_perimetro(self):
        self.__perimetro = (self.__lado1 + self.__lado2)*2
        return self.__perimetro

    def imprimir(self):
        return f'lado1: {self.__lado1}, lado2: {self.__lado2}, area: {self.__area}, perimetro: {self.__perimetro}'


retangulo1 = Retangulo(3, 4)
print(retangulo1.__dict__)
print(retangulo1.imprimir())

#06)
class Retangulo:

    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__area = self.__lado1 * self.__lado2
        self.__perimetro = (self.__lado1 + self.__lado2)*2
    

retangulo1 = Retangulo(5, 7)
print(retangulo1.__dict__)

# 11)


class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def imprimir(self):
        return f'marca: {self.__marca}, modelo: {self.__modelo}, cor: {self.__cor}, marcha: {self.__marcha}'

    def marcha_acima(self):
        if self.__marcha == 2:
            print('já se encontra na marcha limite')
        self.__marcha += 1

    def marcha_abaixo(self):
        if self.__marcha == 2:
            print('se encontra na marcha mínima')
        self.__marcha -= 1


moto1 = Moto('yamaha', 'KW8LW21', 'azul', 0)
print(moto1.__dict__)
print(moto1.imprimir())
moto1.marcha_acima()
moto1.marcha_acima()
print(moto1.imprimir())
moto1.marcha_acima()
print(moto1.imprimir())

# 17)


class Eletrodomestico:

    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        return f'ligado: {self.__ligado}'


eletro1 = Eletrodomestico(True)
print(eletro1.__dict__)
print(eletro1.imprimir())


#31)


class Microondas:

    def __init__(self, ligado, porta_fechada):
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def imprimir(self):
        return f'ligado: {self.__ligado}, porta fechada: {self.__porta_fechada}'

    def ligar(self):
        if self.__porta_fechada:
            self.__ligado = True
        elif not self.__porta_fechada:
            print('Feche a porta para ligar')

    def desligar(self):
        self.__ligado = False

    def fechar_porta(self):
        self.__porta_fechada = True

    def abrir_porta(self):
        self.__porta_fechada = False


produto1 = Microondas(True, True)
print(produto1.__dict__)
print(produto1.imprimir())
produto1.ligar()
print(produto1.imprimir())
produto1.abrir_porta()
print(produto1.imprimir())
produto1.ligar()
print(produto1.imprimir())
produto1.desligar()
print(produto1.imprimir())




"""


