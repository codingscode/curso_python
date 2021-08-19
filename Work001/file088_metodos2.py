
class Pessoa:
    especie = 'humana'
    nota = 10

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        return f'olá eu sou {self.nome}'

    @classmethod
    def suanota(cls):
        return f'sua nota é {cls.nota}'



class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa('vicente', 12, 'recife')
pessoa2 = Pessoa('ferdinande', 21, 'canoas')

print(pessoa1.__dict__)
print(pessoa1.especie)
print(Pessoa.suanota())

print('1------------------------')
animal1 = Animal('aladin', 3)

print(animal1.nome)
print(animal1.idade)


print('2------------------------')
print('3------------------------')
print('4------------------------')
print('5------------------------')
print('6------------------------')
print('7------------------------')













