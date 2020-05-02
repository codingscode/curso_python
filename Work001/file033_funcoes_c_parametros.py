"""
Funções com parametros:
- recebem dados para serem processados dentro da mesma.
entrada -> processamento -> saída




"""

# refatorando uma função

def quadrado(num):
    return num**2


print(quadrado(3))
print(quadrado(5))
print(quadrado(7))

print('-------------------')


def frase(nome, local):
    return f'{nome} mora em {local}.'


print(frase('simon', 'campo grande'))

"""
funções podem ter 'n' parametros de entrada

"""


def repete(a, b, msg):
    return (a + b) * msg


print(repete(2, 3, 'repete '))
print(repete(1, 2, 'python '))









