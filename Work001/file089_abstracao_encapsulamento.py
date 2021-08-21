"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo lógico e hierarquico utilizando
classes.
Encapsular -> capsula

Relembrando atributos/metodos privados em python:
Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um metodo
privado chamado __falar()
Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas python não bloqueia
este acesso fora da classe. Com python acontece um fenomeno chamado Name Mangling, que faz uma
alteração na forma de se acessar os elementos privados, conforme:
_Classe__elemento
Exemplo - Acessando elementos privados fora da classe:
instancia._Classe__nome
instancia._Classe__metodo()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e
métodos privados de usuario.

"""
"""
      classe
--------------------------------
|       atributos e metodos    |
|                              |
|______________________________|
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador  # publico, nao boa pratica
        self.titular = titular  # publico, nao boa pratica
        self.saldo = saldo  # publico, nao boa pratica
        self.limite = limite  # publico, nao boa pratica
        Conta.contador += 1

    def extrato(self):  # metodo de instancia
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):  # metodo de instancia
        self.saldo += valor

    def sacar(self, valor):  # metodo de instancia
        self.saldo -= valor


conta1 = Conta('Geek', 150.00, 1500)
print(conta1)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print(conta1.numero)
print(conta1.__dict__)

conta1.numero = 42
conta1.titular = 'Bob'
conta1.saldo = 9999
conta1.limite = 88888

print(conta1.__dict__)

conta1.extrato()

print('1---------------------------')


class Conta2:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta2.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta2.contador += 1

    def extrato(self):  # metodo de instancia
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):  # metodo de instancia
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor tem que ser positivo')

    def sacar(self, valor):  # metodo de instancia
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor tem que ser positivo')


conta2 = Conta2('TechGo', 32000, 200000)
print(conta2.__dict__)

conta2._Conta2__titular = 'Celso'
conta2._Conta2__saldo = 40000

print(conta2.__dict__)
conta2.depositar(2300)
print(conta2.__dict__)
conta2.depositar(-1000)
print(conta2.__dict__)

conta2.sacar(800)
print(conta2.__dict__)
conta2.sacar(50000)
print(conta2.__dict__)
conta2.sacar(-2100)
print(conta2.__dict__)

print('2---------------------------')

conta3 = Conta2('Softway', 1200, 6000)
conta3.extrato()

conta4 = Conta2('Compfire', 2300, 8000)
conta4.extrato()

# transferindo de uma conta para outra (forma não adequada)
valor = 100

conta3.sacar(valor)
conta4.depositar(valor)

conta3.extrato()
conta4.extrato()
print('3---------------------------')


class Conta3:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta3.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta3.contador += 1

    def extrato(self):  # metodo de instancia
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):  # metodo de instancia
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor tem que ser positivo')

    def sacar(self, valor):  # metodo de instancia
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor tem que ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 remover o valor da conta de origem
        self.__saldo -= valor + 10  #  taxa de transferencia
        # 2 adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Transferindo de forma adequada
conta5 = Conta3('ChinaImportados', 5500, 18000)
conta5.extrato()

conta6 = Conta3('ItalyGourmet', 12300, 37000)
conta6.extrato()

conta5.transferir(100, conta6)

conta5.extrato()
conta6.extrato()

print('4---------------------------')
