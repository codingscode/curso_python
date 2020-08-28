"""
Decorators com diferentes assinaturas


Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern.
A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada

"""

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


print(saudacao('Fulanis'))

try:
    print(ordenar('Bisteca', 'pure')) # assim dá erro , a f aumentar() tem só 1 parametro
except:
    print('Houve erro')


print('---------------------')
# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern.
# Refatorando com o Decorator Pattern


def gritar2(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar2
def ordenar2(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


print(ordenar2('Bisteca', 'pure'))

print('---------------------')


@gritar2
def lol():
    return 'lol'


print(lol())

print('---------------------')
# OBS: Vale lembrar que podemos utilizar parametros nomeados

print(ordenar2(acompanhamento='salada', principal='peixe assado'))

print('---------------------')
# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! 1º argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print('1', soma_dez(10, 12))
print('2', soma_dez(1, 21))

print('3', comida_favorita('pizza', 'churrasco', 'salada'))
print('4', comida_favorita('churrasco', 'salada', 'batata'))

print('---------------------')
