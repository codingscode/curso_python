"""
Manipulando data e hora


Há um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime .

"""

import datetime

print(datetime)
print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime)
print(dir(datetime.datetime))

print('0----------------')

#  modulo / classe / método -> retorna a hora e a data atual
print(datetime.datetime.now())
print(repr(datetime.datetime.now()))  # representação se passesse valores

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

print('1-----------------------')

evento = datetime.datetime(2019, 1, 1, 0)
print(evento)
print(type(evento))
print(type('03/02/2020'))

print('2-----------------------')
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
print(nascimento)
print(type(nascimento))
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
#nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
print(nascimento)
print(type(nascimento))

print('3-----------------------')
# Acessa individual dos elementos de data e hora
evento2 = datetime.datetime.now()
print(evento2)
print(f'ano : {evento2.year}')
print(f'mês : {evento2.month}')
print(f'dia : {evento2.day}')
print(f'hora : {evento2.hour}')
print(f'minuto : {evento2.minute}')
print(f'segundo : {evento2.second}')
print(f'microsegundo : {evento2.microsecond}')

print(dir(evento2))

print('4-----------------------')
