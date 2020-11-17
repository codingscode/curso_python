"""
Métodos data e hora



"""

import datetime

# Com now() podemos especificar um timezone (Fuso Horario), com today() n ocorre isso
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

print('1------------------')
hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

print('2------------------')
# Mudanças ocorrendo à meia noite. combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())


print('3------------------')
print('4------------------')
