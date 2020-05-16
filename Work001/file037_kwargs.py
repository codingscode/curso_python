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

# OBS:  Os parametros *args e **kwargs não são obrigatórios
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
print('-------------------')

"""
nas nossas funções podemos ter nesta ordem:
-> parametros obrigatorios, -> *args, -> parametros nao obrigatorios(default), **kwargs

"""

def minha_funcao1(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(f'args: {args}')
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(f'kwargs: {kwargs} \n')


minha_funcao1(8, 'Julia')
minha_funcao1(18, 'Felicia', 4, 5, 3, solteiro=True)
minha_funcao1(34, 'Philips', eu='Não', voce='Vai')
minha_funcao1(19, 'Tom', 9, 4, 3, java=False, python=True)

print('--------------------------')

# Entenda por que é importante manter a ordem dos parâmetros na declaração

# função com ordem correta de parametros
def mostra_indo(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# a=1 b=2 args= (3,) instrutor='Geek' kwargs={'sobrenome': 'University', 'cargo': 'Instrutor'}
print(mostra_indo(1, 2, 3, sobrenome='University', cargo='Instrutor'))
print('--------------\n')

# função com ordem incorreta de parametros
def mostra_indo2(a, b, instrutor='CodePython', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_indo2(1, 2, 3, sobrenome='University', cargo='Instrutor'))
print('----------------\n')

# desempacotar com kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nome = {'nome': 'Felicia', 'sobrenome': 'Smith'}

print(mostra_nomes(**nome))

def somarnumeros(a, b, c):
    print(a+b+c)


lista1 = [3, 4, 5]
tupla1 = (3, 4, 5)
conjunto1 = {3, 4, 5}
dicionario1 = {'a': 3, 'b': 4, 'c': 5}
#dicionario2 = {'d': 3, 'e': 4, 'f': 5} dá erro
dicionario3 = {'a': 3, 'b': 4, 'c': 5, 'nome': 'Geek'}

somarnumeros(*lista1)
somarnumeros(*tupla1)
somarnumeros(*conjunto1)
somarnumeros(**dicionario1)
#somarnumeros(**dicionario2) dá erro
# OBS: Os nomes da chave em um dicionario devem ser o mesmo dos parametros da função
print('-----------------------------------')

#somarnumeros(**dicionario3, lang='Python')  # dá erro, mas pode ser evitado se colocar **kwargs na definição da função
