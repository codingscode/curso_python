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
# Mudanças ocorrendo à meia noite. combine() -> datetime.combine(date, time)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())  # +1 dia
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

print('3------------------')
# Encontrar o dia da semana. weekday()  vai de 0 a 6 , segunda a domingo
dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']

print(manutencao.weekday())
print(dias_semana[manutencao.weekday()])

print('4------------------')
nascimento = input('digite a data de seu nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')

nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
print(nascimento)
print(nascimento.weekday())

if nascimento.weekday() == 0:
    print('você nasceu em uma segunda')
elif nascimento.weekday() == 1:
    print('você nasceu em uma terça')
elif nascimento.weekday() == 2:
    print('você nasceu em uma quarta')
elif nascimento.weekday() == 3:
    print('você nasceu em uma quinta')
elif nascimento.weekday() == 4:
    print('você nasceu em uma sexta')
elif nascimento.weekday() == 5:
    print('você nasceu em um sábado')
else:
    print('você nasceu em um domingo')

print('5------------------')
# formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora minuto


def formatar_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    else:
        return f'{data.day} de Dezembro de {data.year}'


hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

#hoje_formatado = hoje.strftime('%D/%M/%y')  # y para ano somente os 2 últimos dígitos, M é minutos aqui,
#hoje_formatado = hoje.strftime('%d/%B/%Y')  # B é nome do mês, b é as iniciais do mês,
hoje_formatado = hoje.strftime('%d/%B/%Y')
print(hoje_formatado)

print(formatar_data(hoje))

print('6------------------')
"""
pip install textblob
"""
from textblob import TextBlob
# precisa de internet


def formatar_data2(minha_data):
    return f"{minha_data.day} de {TextBlob(minha_data.strftime('%B')).translate(to='pt-br')} de {minha_data.year}"


print(formatar_data2(hoje))

print('7------------------')

nascimento2 = datetime.datetime.strptime('23/03/1997', '%d/%m/%Y')
print(nascimento2)

print('8------------------')
# somente a hora

almoco = datetime.time(12, 30, 32)  # hora minuto segundo
print(almoco)

print('9------------------')
import timeit

# marcando tempo de execução do nosso codigo com timeit

#loop for
tempo1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo1)  # tempo gasto

# list comprehension
tempo2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo2)  # tempo gasto

# map
tempo3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo3)  # tempo gasto

print('10-----------------')
import functools


def teste(n):
    soma = 0
    for num in range(n*200):
        soma += num**4 + 4
    return soma


print(teste(5))  # tempo
print(timeit.timeit(functools.partial(teste, 2), number=1000))  # tempo

print('11-----------------')
print('12-----------------')

