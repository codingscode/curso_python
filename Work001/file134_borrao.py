
print('algo...')


lista = [
    {'nome': 'paulo', 'idade': 21, 'codigo': 1},
    {'nome': 'maria', 'idade': 17, 'codigo': 2},
    {'nome': 'ze', 'idade': 25, 'codigo': 3},
    {'nome': 'vicente', 'idade': 10, 'codigo': 4},
]

print(lista)

x = lista[3].get('codigo')

print(x)


rec = {'x': 2}

print(rec)
print('------------------')

uma_string = 'nome'

for cada in lista:
    if cada[f'{uma_string}'] == 'ze':  # if cada.get(f'{uma_string}') == 'ze':
        print('achado')
    else:
        print('não achado')



