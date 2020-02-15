ativo = True
print(f'ativo é {ativo}')

valor1, valor2 = 3, 5
print(valor1 == valor2)
print(f'São diferentes: {1 != 2}')
print(f'o tipo de ativo é {type(ativo)}')

# negação (not)
print(not ativo)

# alternância (or)
print('------')
bol1, bol2, bol3 = True, False, True
print(bol1 or bol2 or bol3)
bol1, bol2, bol3 = False, False, False
print(bol1 or bol2 or bol3)

# e (and)
x1, x2, x3 = True, True, True
print(f'os três são {x1 and x2 and x3}')
x1, x2, x3 = True, True, False
print(f'os três são {x1 and x2 and x3}')

