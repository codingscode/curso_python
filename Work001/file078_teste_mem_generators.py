"""
Teste de memória com generators


sequencia de fibonacci: 1, 1, 2, 3, 5, 8, 13 ...

"""


def fib_lista(maximo):  # função usando listas
    numeros = []
    a, b = 0, 1
    while len(numeros) < maximo:
        numeros.append(b)
        a, b = b, a + b
    return numeros


for cada in fib_lista(15):
    print(f'{cada} ', end='')

print('\n------------')


def fib_gen(maximo):   # função usando geradores,  gasta menos memória
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


for cada in fib_gen(10):
    print(f'{cada} ', end='')
