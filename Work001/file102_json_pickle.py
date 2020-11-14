"""
Json e Pickle

Json -> javascript object notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook,
YouTube ...) e terceiros (nós desenvolvedores).

Integrando o JSON com o Pickle

pip install jsonpickle

"""

import json

retorno = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(retorno))
print(retorno)

print('1-----------------------')


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


gato1 = Gato('Felix', 'Siames')
print(gato1.__dict__)

retorno2 = json.dumps(gato1.__dict__)
print(retorno2)


print('2-----------------------')

import jsonpickle

gato2 = Gato('Frajola', 'American Shorthair')

retorno3 = jsonpickle.encode(gato2)
print(retorno3)

print('3-----------------------')
# Escrevendo o arquivo json/pickle

gato3 = Gato('Tom', 'Vira-Lata')

with open('file102_gato_teste1.json', 'w') as arquivo1:
    retorno4 = jsonpickle.encode(gato3)
    arquivo1.write(retorno4)


print('4-----------------------')

with open('file102_gato_teste1.json', 'r') as arquivo2:
    conteudo = arquivo2.read()
    retorno4 = jsonpickle.decode(conteudo)
    print(retorno4)
    print(type(retorno4))
    print(retorno4.nome)
    print(retorno4.raca)

print('5-----------------------')
print('6-----------------------')
