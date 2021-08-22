"""
Continuação POO -> Herança (Inheritance)


A ideia de herança é a de reaproveitar código. Também extender nossas classes.
Obs: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar
atributos e métodos da classe herdada.


Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns
a outras entidades ?

OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
- Super Classe
- Classe Mãe
- Classe Pai
- Classe Genérica

Quando uma classe herda de outra classe, ela é chamada de:
- Sub Classe
- Classe Filha
- Classe Específica

Sobrescrita de métodos (Override):
Sobrescrita de métodos, ocorre quando reescrevemos/implementamos um método presente na super classe
em classes filhas.
"""


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Simon', 'Nooks', 57942755538, 1200)
funcionario1 = Funcionario('Bob', 'mile', 25841953857, 374572645)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print('1---------------------')


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class ClienteRef1(Pessoa):  # ClienteRef1 herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # ou Pessoa.__init__(self, nome, sobrenome, cpf) // não comum
        self.__renda = renda


class FuncionarioRef1(Pessoa):  #  FuncionarioRef1 herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente2 = ClienteRef1('Clarence', 'Silver', 57942755538, 1200)
funcionario2 = FuncionarioRef1('Mike', 'Stone', 25841953857, 374572645)

print(cliente2.nome_completo())
print(funcionario2.nome_completo())

print(cliente2.__dict__)
print(funcionario2.__dict__)

print('2---------------------')


class PessoaRef2:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class ClienteRef2(PessoaRef2):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class FuncionarioRef2(PessoaRef2):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print('**da super**', super().nome_completo())
        print('***', self._PessoaRef2__cpf)  # dá erro com super()._PessoaRef2__cpf
        return f'Funcionário: {self.__matricula}, Nome: {self._PessoaRef2__nome}'


# Sobrescrita de métodos (Overriding)
cliente3 = ClienteRef2('Tom', 'Stone', 57942755538, 1200)
funcionario3 = FuncionarioRef2('Ken', 'Yamamoto', 25841953857, 374572645)

print(cliente3.nome_completo())
print(funcionario3.nome_completo())

print('3---------------------')
