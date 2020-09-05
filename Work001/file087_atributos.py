"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.
Em python, dividimos os atributos em 3 grupos:
- atributos de instância
- atributos de classe
- atributos dinâmicos

# Atributos de instância: São atributos declarados dentro do método construtor
obs: método construtor: é um método especial utilizado para a construção do objeto.



"""

"""
# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada() {
   private int voltagem;
   private String cor;
   private Boolean ligada = false;

   public Lampada(int voltagem, String cor) {
      this.voltagem = voltagem;
      this.cor = cor
   }

   public int getVoltagem() {
      return this.voltagem;
   }
}

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é publico. Ou seja, pode
 ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
 acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo underscore
  no inicio de seu nome.
Isso é conhecido também por Name Mangling.


"""
# Classes com Atributo de Instancia Público


class Lampada:
    def __init__(self, voltagem, cor):  # método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Produto2:
    def __init__(algo, nome, preco):
        algo.nome = nome
        algo.preco = preco

# Atributos Publicos e Atributos Privados


class Acesso:
    def __init__(self, email, senha, nome):
        self.__email = email  # privado
        self.__senha = senha  # privado
        self.nome = nome  # publico

    def mostrar_senha(self):
        return self.__senha

    def mostrar_email(self):
        return self.__email


"""
Obs: Lembre-se que isso é apenas uma convenção, ou seja, a ling. Python não vai impedir que façamos
 acesso aos atributos sinalizados como privados fora da classe.

"""

usuario = Acesso('usuario@gmail.com', '123456', 'rudney')
#print(usuario.__email)  # dá erro, pois é privado  AttributeError
print(usuario.nome)    # não dá erro, pois é publico

print('--------------')

print(dir(usuario))
"""
['_Acesso__email', '_Acesso__senha', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', 'nome']

"""
print('--------------')

print(usuario._Acesso__email)  # Temos acesso. Mas não deveriamos fazer este acesso.  Name Mangling
print(usuario._Acesso__senha)

print('--------------')

print(usuario.mostrar_senha())

print('--------------')

print(usuario.mostrar_email())

print('--------------')
"""
O que significa atributos de instância?
Significa, que ao criarmos instancias/objetos de uma classe, todos as intancias terão estes atributos.
"""

usuario1 = Acesso('usuario1@gmail.com', 'abcd', 'silas')
usuario2 = Acesso('usuario2@gmail.com', 'efgh', 'giulia')

print(usuario1.mostrar_email())
print(usuario2.mostrar_email())

print('--------------')

# Atributos de classe
"""
São atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente
já inicializamos um valor, e este valor é compartilhado entre todas as instãncias da classe. Ou seja,
ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de 
instância, com os atributos de classe todas as instancias terão o mesmo valor para este atributo.
"""
p1 = Produto('playstation 4', 'video game', 2400)
p2 = Produto('macbook pro', 'computador movel', 16000)

print('--------------')
# Refatorando a classe produto


class ProdutoRef:
    # Atributo de classe
    imposto = 1.05  # 5% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * ProdutoRef.imposto


prod1 = ProdutoRef('pendrive', 'storage', 17.00)
prod2 = ProdutoRef('caneta', 'escrita', 2.00)

print(prod1.imposto)
print(prod2.imposto)

print(prod1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(prod2.valor)

"""
OBS: Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe.
"""
print(ProdutoRef.imposto)  # Acesso correto de um atributo de classe

print('--------------')


class ProdutoRef2:
    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRef2.contador + 1  # atributo de instancia
        self.nome = nome  # atributo de instancia
        self.descricao = descricao  # atributo de instancia
        self.valor = valor * ProdutoRef.imposto  # atributo de instancia
        ProdutoRef2.contador = self.id   # atributo de classe


meu_prod1 = ProdutoRef2('alicate', 'consertos', 12.00)
meu_prod2 = ProdutoRef2('caderno', 'material p/escritorio', 15.00)
meu_prod3 = ProdutoRef2('toalha', 'banho', 22.00)

print(meu_prod1.valor)
print(meu_prod2.valor)
print(meu_prod3.valor)

print(ProdutoRef2.imposto)

print(meu_prod1.id)
print(meu_prod2.id)
print(meu_prod3.id)

"""
obs: em linguagens como o java, os atributos conhecidos como atributos de classe aqui em python são
chamados de atributos estaticos.
"""

print('--------------')
# Atributos Dinâmicos
"""
um atributo de instancia que pode ser criado em tempo de execução.
obs: o atributo dinâmico será exclusivo da instancia que o criou.
"""


class ProdutoRef3:
    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRef2.contador + 1  # atributo de instancia
        self.nome = nome  # atributo de instancia
        self.descricao = descricao  # atributo de instancia
        self.valor = valor * ProdutoRef.imposto  # atributo de instancia
        ProdutoRef2.contador = self.id   # atributo de classe


meu_prod4 = ProdutoRef3('goiaba', 'alimento', 9.00)
meu_prod5 = ProdutoRef3('nescau', 'achocolatado', 3.2)

# Criando um atributo dinâmico em tempo de execução
meu_prod4.peso = '4'  # Note que na classe ProdutoRef3 não existe o atributo peso

print(f'ProdutoRef3: {meu_prod4.nome}, Descrição: {meu_prod4.descricao}, Valor: {meu_prod4.valor}, Peso: {meu_prod4.peso}')
# dá erro print(f'ProdutoRef3: {meu_prod5.nome}, Descrição: {meu_prod5.descricao}, Valor: {meu_prod5.valor}, Peso: {meu_prod5.peso}')

print('--------------')

# Deletando atributos
print(meu_prod4.__dict__)
print(meu_prod5.__dict__)

print(ProdutoRef3.__dict__)

del meu_prod4.nome
del meu_prod5.descricao

print(meu_prod4.__dict__)
print(meu_prod5.__dict__)

print('--------------')