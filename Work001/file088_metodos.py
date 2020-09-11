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

# métodos de classe em python são conhecidos como métodos estáticos em outras linguagens

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

usuario1 = Usuario('Donatelo', 'Pizza', 'donatelo@gmail.com', '1234')
usuario2 = Usuario('Fiorina', 'Pita', 'fiorina@gmail.com', '5678')

print(usuario1.nome_completo())
print(Usuario.nome_completo(usuario1))

print(usuario2.nome_completo())

print(f'Senha usuario1: {usuario1._Usuario__senha}')  #  Acesso de forma errada de um atributo de classe

"""
instalar no terminal: pip install passlib
"""
from passlib.hash import pbkdf2_sha256 as criptografar


class UsuarioRef:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = criptografar.hash(senha, rounds=200000, salt_size=16) # usa-se hash(), pois encrypt() está deprecado

    def correr(self, metros):  # evitar dunder(double under)  __correr__
        print(f'Estou correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if criptografar.verify(senha, self.__senha):
            return True
        return False


usuario3 = UsuarioRef('jurandir', 'pires', 'jurandir@gmail.com','goiaba')

print(usuario3._UsuarioRef__senha)  # forma nao recomendada

print('----------------------')
# Métodos de Classe


class UsuarioRef2:
    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRef2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = criptografar.hash(senha, rounds=200000, salt_size=16) # usa-se hash(), pois encrypt() está deprecado
        UsuarioRef2.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if criptografar.verify(senha, self.__senha):
            return True
        return False


usuario4 = UsuarioRef2('Michelangelo', 'Silva', 'miko@gmail.com', '8231')

UsuarioRef2.contar_usuarios()   # forma correta
usuario4.contar_usuarios()  # possivel, mas incorreta
# método de instancia ≠ método de classe

print('----------------------')


class UsuarioRef3:
    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRef2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = criptografar.hash(senha, rounds=200000, salt_size=16) # usa-se hash(), pois encrypt() está deprecado
        UsuarioRef3.contador = self.__id

    def nome_completo(self):  # métodos públicos
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):  # métodos públicos
        if criptografar.verify(senha, self.__senha):
            return True
        return False

    # @classmethod  # o ideal os estáticos
    def ver(self):
        print('Teste')

usuario5 = UsuarioRef3('Leonardo', 'da vinci', 'leo@gmail.com', '1245678')
usuario5.contar_usuarios()

print('----------------------')

class UsuarioRef4:
    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRef2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = criptografar.hash(senha, rounds=200000, salt_size=16) # usa-se hash(), pois encrypt() está deprecado
        UsuarioRef4.contador = self.__id
        print(f'Usuario criado: {self.__gerar_usuario()}')

    def nome_completo(self):  # métodos públicos
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):  # métodos públicos
        if criptografar.verify(senha, self.__senha):
            return True
        return False

    # @classmethod  # o ideal os estáticos
    def ver(self):
        print('Teste')

    def __gerar_usuario(self):
        return self.__email.split('@')[0]



usuario6 = UsuarioRef4('Vangogh', 'van', 'goguinho@gmail.com', '87312')
#print(usuario6.__gerar_usuario())  # dá erro
print(usuario6._UsuarioRef4__gerar_usuario())  # acesso, de forma ruim


print('----------------------')
# Método Estático


class UsuarioRef5:
    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():
        return 'HLX22'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRef2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = criptografar.hash(senha, rounds=200000, salt_size=16) # usa-se hash(), pois encrypt() está deprecado
        UsuarioRef5.contador = self.__id
        print(f'Usuario criado: {self.__gerar_usuario()}')

    def nome_completo(self):  # métodos públicos
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):  # métodos públicos
        if criptografar.verify(senha, self.__senha):
            return True
        return False

    # @classmethod  # o ideal os estáticos
    def ver(self):
        print('Teste')

    def __gerar_usuario(self):
        return self.__email.split('@')[0]


print(UsuarioRef5.contador)
print(UsuarioRef5.definicao())

usuario7 = UsuarioRef5('Nelson', 'cavaquinho', 'violaoecavacos@gmail.com', '91341')

print(UsuarioRef5.contador)
print(UsuarioRef5.definicao())
print('----------------------')
