"""
Erros mais comuns

SyntaxError -> ocorre quando o python encontra um erro de sintaxe. Ou seja, foi escrito algo que
o python nao reconhece como parte da linguagem.

NameError -> ocorre quando uma variavel ou função não foi definida.

TyperError -> ocorre quando um funcao/operacao/acao é aplicada a um tipo errodo

IndexError -> ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado
indexado utilizando um indice inválido.

ValueError -> ocorre quando uma funcao/operacao built-in (integrada) recebe um argumento com
tipo correto mas valor inapropriado.

KeyError -> ocorre quando tentamos acessar um dicionario com uma chave que não existe.

AttributeError -> ocorre quando uma variavel nao tem um atributo/funcao.

IndentationError -> ocorre quando nao respeiamos a indentacao do python (4 espacos)

OBS: Exceptions e Errors são sinonimos na programacao.

"""

#printf('curso python')   # erro proposital  # NameError: name 'printf' is not defined
"""
obs: observar saídas de erros
"""

# SyntaxError
   # exemplo 1
"""
def funcao:   # SyntaxError: invalid syntax
    print('codando em python')
"""

   # exemplo 2
"""
None = 1  # None é palavra reservada  # SyntaxError: cannot assign to None
"""

   # exemplo 3
"""
return    # SyntaxError: 'return' outside function

"""

# NameError
    # exemplo 1
"""
print(nome)  # NameError: name 'nome' is not defined
print(calcular())

a = 8  #  se a > 10 dá erro

if a < 10:
    mensagem = 'é menor que 10'

print(mensagem)

"""

# TypeError

"""
print(len('bom dia.')) # normal
print(len([2, 10, 5])) # normal

print(len(7))  # TypeError: object of type 'int' has no len()
print(len(True)) #  TypeError: object of type 'bool' has no len()
print('python' + [])  # TypeError: can only concatenate str (not "list") to str
print('python' + 3)  # TypeError: can only concatenate str (not "int") to str
print('python' + str(3)) 


"""

# IndexError

"""
lista1 = ['python'] 
print(lista1[0]) # normal
print(lista1[1]) # IndexError: list index out of range
print(lista1[0][0]) # normal
print(lista1[0][10]) # IndexError: string index out of range


"""

# ValueError

"""
print(int('42')) # normal
print(int('r')) #  ValueError: invalid literal for int() with base 10: 'r'

"""

# KeyError
"""
dicionario = {}
print(dicionario['nome'])  # KeyError: 'nome'

"""

# AttributeError

"""
tupla = (41, 10, 20, 5)
print(tuple.sort())  #  AttributeError: type object 'tuple' has no attribute 'sort'


"""

# IndentationError

"""
def novo():
print('oi')  # IndentationError: expected an indented block

novo()

for indice in range(4):
print(indice)  #  IndentationError: expected an indented block

"""
