"""
Preservando metadata com wraps

Metadados -> são dados intrísecos aos arquivos.

wraps -> são funções que envolvem elementos com diversas finalidades.


"""

#Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """função logar dentro de outra"""
        print(f'Você está chamando {funcao. __name__}')
        print(f'Aqui a documentação {funcao. __doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma_dois(a, b):
    """ somando dois numeros"""
    return a + b


print(soma_dois(10, 30))

print('--------------------')

print(soma_dois)
print(soma_dois.__name__)
print(soma_dois)
print(soma_dois.__doc__)

print('--------------------')

# Resolução do problema
from functools import wraps


def ver_log2(funcao):
    @wraps(funcao)
    def logar2(*args, **kwargs):
        """função logar dentro de outra2"""
        print(f'Você está chamando {funcao. __name__}')
        print(f'Aqui a documentação {funcao. __doc__}')
        return funcao(*args, **kwargs)
    return logar2


@ver_log2
def soma_dois2(a, b):
    """somando dois numeros2"""
    return a + b


print(soma_dois2(12, 14))

print(soma_dois2.__name__)
print(soma_dois2.__doc__)
print('--------------------')

print('****', help(soma_dois2))

print('--------------------')
