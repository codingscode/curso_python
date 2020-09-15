"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo lógico e hierarquico utilizando
classes.
Encapsular -> capsula

Relembrando atributos/metodos privados em python:
Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um metodo
privado chamado __falar()
Esses elementos privados só devem/deveriam sera acessados dentro da classe. Mas python não bloqueia
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
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
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






