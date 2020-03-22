# Data ano, mês, dia, dia da semana

from datetime import date

data1 = date(2016, 12, 9)
print(f'{data1} // ano/mes/dia ')

print(f'hoje: {date.today()}')

print('--------------------')

hoje = date.today()

data2 = date(hoje.year, hoje.month, 5)
print(data2)

# diferença de dias
natal_2020 = date(2020, 12, 25)
quanto_falta = abs(natal_2020 - hoje)
print(f'faltam {quanto_falta.days} dias')

print('--------------------')

print(hoje.weekday())  # 0 é domingo, 1 é segunda, ...
print(f'numero do dia : {hoje.day}')

data2 = data2.replace(day=2)
print(data2)

print(data2.strftime("%d/%m/%Y"))
print('-----------------------')

# Tempo  -   horas, minutos, segundos, microsegundos

from datetime import time

tempo1 = time(12, 25, 31, 1333)
print(tempo1)

print(tempo1.strftime("%H horas, %M minutos e %S segundos"))

print('--------------------')

from datetime import datetime

datatempo1 = datetime(2020, 3, 10, 9, 43, 4, 800)
print(datatempo1)

datatempo2 = datetime.now()   # data local
print(datatempo2)
datatempo2 = datetime.utcnow()
print(datatempo2)











