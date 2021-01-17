
"""
Operador Walrus

permite fazer a atribuição e retorno de valor em uma única expressão
variável := expressao
"""

nome = 'python'
print(nome)

print(nome2 := 'pythonista')

print('1-------------------')
"""
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

"""
# o mesmo que:
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)


print('2-------------------')
print('3-------------------')
