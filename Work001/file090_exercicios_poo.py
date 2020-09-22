"""
Exercicios POO

"""

"""
# 01)

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir(self):
        return f'nome: {self.__nome}, idade: {self.__idade}, altura: {self.__altura}'

    def setar_nome(self, valor_nome):
        self.__nome = valor_nome

    def setar_idade(self, valor_idade):
        self.__idade = valor_idade

    def setar_altura(self, valor_altura):
        self.__altura = valor_altura


pessoa1 = Pessoa('Paulo', 21, 1.85)

print(pessoa1.__dict__)
print(pessoa1._Pessoa__nome)
print(pessoa1._Pessoa__idade)
print(pessoa1._Pessoa__altura)

pessoa1.setar_nome('Samuel')
pessoa1.setar_idade(32)
pessoa1.setar_altura(1.78)
print(pessoa1.__dict__)


"""


# 02)


class Agenda:
    id = 0
    pessoa = dict()

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__pessoaatual = Agenda.pessoa
        self.__lista = []
        Agenda.pessoa = dict()

    def armazenar_pessoa(self, nome, idade, altura):
        pass

    def remover_pessoa(self, nome):
        pass

    def buscar_pessoa(self, nome):
        pass

    def imprimir_agenda(self):
        pass

    def imprir_pessoa(self, indice):
        pass
    

