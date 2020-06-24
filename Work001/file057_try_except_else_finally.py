"""
try / except / else / finally

Dica de quando e onde tratar codigo:
Toda entrada deve ser tratada !

obs: a função do usuario é destruir seu sistema.
else -> é executado somente se não ocorrer o erro.

"""
num = 0

try:
    num = float(input('digite um número: '))
except ValueError:
    print(f'valor incorreto  | tipo: {type(num)}')
else:
    print(f'vc digitou {num}')

print('----------------------------')

try:
    num = float(input('digite um número: '))
except ValueError:
    print(f'valor incorreto  | tipo: {type(num)}')
else:
    print(f'vc digitou {num}')
finally:
    print('finally executado de qualquer forma')

"""
finally é executado independente de exceção. o finally é, geralmente, usado para fechar
 ou desalocar recursos.
"""
print('----------------------------')
# forma 1


def dividir(a, b):
    return a/b


try:
    numero1 = float(input('informe o 1º número: '))
    numero2 = float(input('informe o 2º número: '))
    print(dividir(numero1, numero2))
except ValueError:
    print('o valor precisa ser numérico.')

# forma 2 melhor 1


def dividir2(a, b):
    try:
        return float(a)/float(b)
    except ValueError:
        return 'valor incorreto'
    except ZeroDivisionError:
        return 'não é possível realizar uma divisao por zero'


numero1 = input('informe o 1º número: ')
numero2 = input('informe o 2º número: ')
print(dividir2(numero1, numero2))

print('----------------------------')
print('exemplo genérico:')


def dividir3(a, b):
    try:
        return float(a)/float(b)
    except:
        return 'ocorreu um problema'


numero1 = input('informe o 1º número: ')
numero2 = input('informe o 2º número: ')
print(dividir3(numero1, numero2))

print('----------------------------')


print('exemplo semi genérico:')


def dividir3(a, b):
    try:
        return float(a)/float(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'ocorreu um problema: {erro}'


numero1 = input('informe o 1º número: ')
numero2 = input('informe o 2º número: ')
print(dividir3(numero1, numero2))
