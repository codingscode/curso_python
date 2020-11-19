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

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)


print('6------------------')
print('7------------------')
print('8------------------')
print('9------------------')
