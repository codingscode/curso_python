"""
POO Métodos


Métodos (funcoes) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.
Em python, dividimos os metodos, assim como os atributos, em 2 grupos: Métodos de instancia e Métodos
de classe.

# Métodos de Instancia
O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o
objeto a partir da classe.

obs: Métodos são escritos em letras minusculas. Se o nome for composto, o nome terá as palavras
separadas por underline.


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return self.__valor * (1 - porcentagem / 100)


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def correr(self, metros):  # evitar dunder(double under)  __correr__
        print(f'Estou correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


print(dir())
print(dir(__builtins__))

p1 = Produto('play4', 'video game', 2300)
print(p1.desconto(20))

#print(Produto.desconto(40))  # dá erro
print(Produto.desconto(p1, 20))  # self, desconto

print('----------------------')



print('----------------------')
print('----------------------')
print('----------------------')
print('----------------------')
print('----------------------')
print('----------------------')
print('----------------------')

