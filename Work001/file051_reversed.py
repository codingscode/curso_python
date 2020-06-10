"""
Reversed

OBS: Não confunda com a função reverse() (só funciona com list) que foi visto em listas.
Já a função reversed() funciona com qualquer iteravel.
Sua função é inverter o iteravel.
A função reversed() retorna um iteravel chamado List Reverse Iterator

"""
lista1 = [20, 8, 14, 3]
print(lista1)

lista1.reverse()  # modifica a lista original
print(lista1)

print('----------------------------------------')

lista2 = [34, 12, 6, 28]
print(lista2)

res = reversed(lista2)
print(res)
print(type(res))
print(list(res))  # guardado em variavel é usado só uma vez
print(tuple(res))
print(set(res))
print(tuple(reversed(lista2)))
print(set(reversed(lista2)))  #  set não tem ordem
"""
em conjuntos nao definimos a ordem dos elementos
"""

print('----------------------------------------')

# podemos iterar sobre o reversed()
for letra in reversed('pindamonhangaba'):
    print(letra, end='')

print('')
# podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('taubaté'))))

# mais fácil com slice de string
print('Piracicaba'[::-1])

# podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(10)):
    print(n, end='')

print('')

# usando o próprio range
for n in range(9, -1, -1): # inicio/fim/passo
    print(n, end='')
