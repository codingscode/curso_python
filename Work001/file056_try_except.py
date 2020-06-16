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

















