# tuplas
# são imutaveis mas podem ser sobrescritas

tupla1 = (1, 2, 3, 4, 5, 8)
tupla2 = ('cidade', 'alegria', 'futuro', 'democracia')
tupla3 = (3, )
tupla4 = ()

print(f'{tupla1}  //  {tupla2}  // {tupla3} // {tupla4}')
print(f'{type(tupla1)} // {type(tupla2)} // {type(tupla3)} // {type(tupla4)}')

print(tupla1[2])
print(tupla2[1])
print(tupla1[2:5])   # indice 2 ao ?-1
print('--------------')

# usando len(), max(), min()
tupla5 = (10, 8, 5, 12, 16, 3, 2)
print(tupla5)

print(f'o tamanho é : {len(tupla5)}')
print(f'o maior é : {max(tupla5)}')
print(f'o menor é : {min(tupla5)}')

# transformando tupla em lista e vice versa
lista1 = list(tupla5)
print(lista1)

lista2 = [20, 8, 2, 15, 48]
tupla6 = tuple(lista2)
print(tupla6)

print('-------------')



