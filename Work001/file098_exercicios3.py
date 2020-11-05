"""


"""


class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, *valores):
        if len(valores) == 0:
            return 'sem valor passado'
        else:
            if isinstance(valores[0], int):
                if valores[0] == 1:
                    return f'codigo: {self.__codigo}, nome: {self.__nome}, idade: {self.__idade}'
                return f'codigo: {self.__codigo}, nome: {self.__nome}'
            else:
                print('valor inválido')


class Testapessoa(Pessoa):

    def __init__(self, codigo, nome, idade):
        super().__init__(codigo, nome, idade)


teste1 = Testapessoa(201243, 'paulo', 22)

print(teste1.exibe())
print(teste1.exibe(1))
print(teste1.exibe(2))
print(teste1.exibe(1, 2))
print(teste1.exibe(2, 3))

print('-------------------')
print('-------------------')
