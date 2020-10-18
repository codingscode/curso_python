"""
POO:
Métodos Mágicos

são todos os métodos que utilizam o dunder.
dunder init -> __init__()
dunder -> double underscore
dunder repr -> representação do objeto

__str__ prevalece sobre __repr__



"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self): #  tenta comentar
        #return self.titulo
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo


livro1 = Livro('Python coding', 'escola de codigo', 250)
livro2 = Livro('IA com Python', 'code match', 100)

print(livro1)
print(str(livro1))


print(livro2)
print(str(livro2))


print('1----------------------------------------')

from file097_metodos_magicos import Livro

l1 = Livro('Qualquer', 'Outro', 80)

print(l1)
print(str(l1))
print(repr(l1))  # testar no terminal é diferente
print(repr(l1))  # testar no terminal é diferente
#print(len(l1))   # dá erro



print('2----------------------------------------')
print('3----------------------------------------')
print('4----------------------------------------')




