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

    def __len__(self):  # descomentar evita o erro abaixo
        return self.paginas
        #return len(self.titulo)

    #def __del__(self):
    #    print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):  # tenta comentar
        return f'{self} - {outro}'

    def __mul__(self, outro):  # tentar comentar
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não é possivel multiplicar'


livro1 = Livro('Python coding', 'escola do codigo', 250)
livro2 = Livro('IA com Python', 'code match', 100)

print(livro1)
print(str(livro1))

print(livro2)
print(str(livro2))

print('1----------------------------------------')

from file097_metodos_magicos import Livro

l1 = Livro('Qualquer', 'Outro', 80)
l2 = Livro('Harry Potter', 'ficção', 537)

print(l1)
print(str(l1))
print(repr(l1))  # testar no terminal é diferente
print(repr(l2))  # testar no terminal é diferente
print(len(l1))   # dá erro
print(len(l2))

#del l1

print('2----------------------------------------')
print(l1)
print(l2)
print(l1 + l2)  # dá erro
print(dir())
print(dir(__builtins__))

print('3----------------------------------------')
print(l1*3)  # dá erro
print(l1*3.4)  # dá erro
print(l1*'goiaba')  # dá erro

print('4----------------------------------------')
print(dir(object))

print('5----------------------------------------')
print('6----------------------------------------')
