"""

"""

# tipagem implícita/dinamica
numero = 10
print(numero)
print(type(numero))

numero = 3.2
print(numero)
print(type(numero))

print('1------------------')
if False:  # testar trocar False por True, dá erro. TypeError: unsupported operand type(s) for +: 'int' and 'str'
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)

print('2------------------')
