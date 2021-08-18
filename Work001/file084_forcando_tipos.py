"""
Forçando tipos de dados com Decoradores

"""


def forcar_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forcar_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('python', 3)
print('1-------------')
repete_msg('python', '3')

print('2-------------')


@forcar_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('6', 3)
dividir('7', '4')
print('3-------------------')
