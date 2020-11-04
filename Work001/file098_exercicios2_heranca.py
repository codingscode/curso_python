

class Equipamento:

    def __init__(self, tipo, preco):
        self.__tipo = tipo
        self.__preco = preco

    def get_tipo(self):
        return self.__tipo

    def get_preco(self):
        return self.__preco

    def set_tipo(self, valor):
        self.__tipo = valor

    def set_preco(self, valor):
        self.__preco = valor


class Computador(Equipamento):

    def __init__(self, nome, tipo, preco):
        super().__init__(tipo, preco)
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, valor):
        self.__nome = valor


class TestaEquipamento(Equipamento, Computador):

    def __init__(self, tipo, preco):
        super().__init__(tipo, preco)


