"""
Json e Pickle

Json -> javascript object notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook,
YouTube ...) e terceiros (nós desenvolvedores).



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


print('2-----------------------')
print('3-----------------------')
print('4-----------------------')




