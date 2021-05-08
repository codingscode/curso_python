"""
Utilizando lambdas

são expressões funções sem nome ou seja funções anonimas



"""


def calculo(valor):
    return valor * 2 + 4


print(calculo(2))
print(calculo(3))
print('---------------')

lambda x: 2 * x + 4  # lambda parametro: retorno

calc = lambda x: 2 * x + 4
print(calc(2))
print(calc(3))
print('---------------')

"""
podemos ter expressões lambdas com multiplas entradas 


"""

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' kyle', 'SMITH'))
print(nome_completo(' amBROsio       ', 'sardinha'))

print('------------------------')

"""
em funções python podemos ter nenhuma ou várias entradas. Em lambdas também

"""

amar = lambda: 'Como não amar Python? '

uma_entrada = lambda x: 3 * x + 1

duas_entradas = lambda x, y: (x * y) ** 0.5

tres_entradas = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn: <expressão>

print(amar())
print(uma_entrada(2))
print(duas_entradas(5, 1))
print(tres_entradas(3, 1, 4))

# obs: Se passarmos mais argumentos do que parametros esperados teremos TypeError
print('----------------------------')

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert',
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)
print(sorted(autores))
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # ordenando pelo sobrenome
print(autores)

print('------------------')


def f_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste1 = f_quadratica(2, 3, -5)

print(teste1(0))  # passando valor para x
print(teste1(1))
print(teste1(-2.5))

print(f_quadratica(3, 2, 1)(2))  # direto
print(f_quadratica(3, 2, 1))