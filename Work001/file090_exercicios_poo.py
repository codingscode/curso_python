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
        colocar_pessoa = {'id': Agenda.id, 'nome': nome, 'idade': idade, 'altura': altura}
        self.__lista.append(colocar_pessoa)
        Agenda.id += 1

    def remover_pessoa(self, nome):
        todos = self.__lista

        nova_lista = list(filter(lambda cada: cada['nome'] not in nome, todos))
        self.__lista = nova_lista
        return nova_lista


    def buscar_pessoa(self, nome):
        pass

    def imprimir_agenda(self):
        return self.__lista

    def imprir_pessoa(self, indice):
        pass


agenda1 = Agenda('silas', 21, 1.7)
agenda1.armazenar_pessoa('donatello', 33, 1.9)
agenda1.armazenar_pessoa('bob', 17, 1.73)
agenda1.armazenar_pessoa('lucia', 25, 1.8)
agenda1.armazenar_pessoa('aladin', 16, 1.6)
agenda1.armazenar_pessoa('jessy', 22, 1.71)
agenda1.armazenar_pessoa('dennis', 12, 1.4)
agenda1.armazenar_pessoa('dino', 26, 1.85)
agenda1.armazenar_pessoa('fabian', 23, 1.78)

#print(agenda1.imprimir_agenda())
[print(cada) for cada in agenda1.imprimir_agenda()]
print(len(agenda1.imprimir_agenda()))
print('------------------------------')

print(agenda1.remover_pessoa('jessy'))
#print(agenda1.imprimir_agenda())
[print(cada) for cada in agenda1.imprimir_agenda()]
print(len(agenda1.imprimir_agenda()))
print('------------------------------')







