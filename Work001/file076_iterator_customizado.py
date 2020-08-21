"""
Iterator Customizado


"""

for n in range(5):
    print(n)

print('---------')

for n in range(3, 8):
    print(n)

print('---------')


class Contador:
    def __init__(self, menor, maior):  # constructor
        self.menor = menor    # propriedade recebe parametro
        self.maior = maior    # propriedade recebe parametro


cont = Contador(3, 8)
print(cont)
print(cont.menor)
print(cont.maior)

#meu_ite = iter(cont)

#print(next(meu_ite)) # TyperError

print('-----------------')


class Contador2:
    def __init__(self, menor, maior):  # constructor
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


cont2 = Contador2(10, 18)
print(cont2)
print(type(cont2))
print(cont2.menor)
print(cont2.maior)

meu_ite2 = iter(cont2)
print(next(meu_ite2))
print(next(meu_ite2))
print(next(meu_ite2))  # continuando até o valor máximo dá erro

print('---------------')
