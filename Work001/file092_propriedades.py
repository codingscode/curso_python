"""
POO - Propriedades

Em linguagens como Java, ao declararmos atributos privados nas classes, costumamos criar metodos
publicos para manipulação desses atributos. Esses metodos são conhecidos por getters e setters, onde
os getters retornam o valor do atributo e os setters alteram o valor do mesmo.


"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo}, do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Nina', 12000, 20000)
conta2 = Conta('Laury', 7000, 11000)

print(conta1.extrato())
print(conta2.extrato())

# forma incorreta
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'a soma das contas é {soma}')

print('1---------------------------')


class ContaRef1:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = ContaRef1.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ContaRef1.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo}, do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):  # método publico de acesso
        return self.__numero

    def get_titular(self):  # método publico de acesso
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):  # método publico de acesso
        return self.__saldo

    def get_limite(self):  # método publico de acesso
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta3 = ContaRef1('Bob', 2300, 7000)
conta4 = ContaRef1('Lya', 4000, 6000)

soma2 = conta3.get_saldo() + conta4.get_saldo()
print(f'a soma das contas é {soma2}')

print(conta3.__dict__)
conta3.set_limite(10000)
print(conta3.__dict__)

print('2---------------------------')


class ContaRef2:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = ContaRef2.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ContaRef2.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo}, do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta5 = ContaRef2('Rob', 14000, 20000)
conta6 = ContaRef2('Caren', 23000, 32000)

print(conta5.extrato())
print(conta6.extrato())

soma3 = conta5.saldo + conta6.saldo
print(f'a soma é {soma3}')

print(conta5.__dict__)
print(conta5.limite)
conta5.limite = 18000
print(conta5.__dict__)
print(conta5.limite)

print('para conta5:', conta5.valor_total)
print('para conta6:', conta6.valor_total)

print('3---------------------------')
print('4---------------------------')
print('5---------------------------')


