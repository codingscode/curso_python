"""
o bloco try/except:

o utilizamos para tratar erros que podem ocorrer no nosso código, prevenindo assim que
o programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problematica
except:
    // o que deve ser feito em caso de problema


"""

# tratando um erro generico
try:
    executar()  # isso nao foi definido antes, ValueError
except:
    print('Há algum problema')

print('--------------------------------')

try:
    len(5) # ocorreria  TypeError: object of type 'int' has no len()
except:
    print('Há algum problema2')

"""
OBS: Tratar erro de forma generica nao é a melhor forma de tratamento de erros. O ideal é 
SEMPRE tratar de forma específica.
"""
print('-----------------------------')

# tratando erro específico
try:
   curso()
except NameError:
   print('vc está utilizando uma função inexistente')

"""
try:
    len(5) #  mesmo assim o erro aparece . TypeError: object of type 'int' has no len()
except NameError:
    print('ou tipo de erro')

"""

try:
    len(5)
except TypeError:
    print('ou tipo de erro')

try:
    len(5)
except TypeError as erro:
    print('ou tipo de erro')
    print('------->>>', erro)

print('-----------------------------')
# podemos efetuar diversos tratamentos de erros de uma vez

try:
    #len(6)
    #executar()
    print('geek'[7])
    #print(1/0)
except NameError as erroa:
    print(f'*há NameError: {erroa}')
except TypeError as errob:
    print(f'**há TypeError: {errob}')
except:
    print('***outro erro')

print('-----------------------------')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dicio = {'nome': 'python'}

print(pega_valor(dicio, 'nome'))
print(pega_valor(dicio, 'duracao'))
print(pega_valor(8, 'nome'))
print(pega_valor(dicio, 20))
