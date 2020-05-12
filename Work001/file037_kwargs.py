"""
**kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o
**kwargs exige que utilizemos parametros nomeados, e transforma esses parametros extras em um
dicionario.


"""


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas()
cores_favoritas(vicente='laranja', simon='verde', geovana='azul', patricia='purpura')
print('---------------------\n')


def cores_favoritas2(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} é {cor}')


cores_favoritas2(vicente='laranja', simon='verde', geovana='azul', patricia='purpura')

# OBS:  Os parametros *args e **kwargs não obrigatórios
cores_favoritas2()
print('------------------------\n')

#exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))












