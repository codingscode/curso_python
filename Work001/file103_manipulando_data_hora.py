"""
Manipulando data e hora

Há um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime .

"""

import datetime

print(datetime)
print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

#  modulo / classe / método -> retorna a hora e a data atual
print(datetime.datetime.now())
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)


print('1-----------------------')
print('2-----------------------')
print('3-----------------------')
print('4-----------------------')
print('5-----------------------')
