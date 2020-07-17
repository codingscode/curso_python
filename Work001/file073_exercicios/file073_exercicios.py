""""""
"""
Exercicios python

#01
with open('daquest1.txt', 'w') as arquivo1:
    while True:
        entrada = input(f'digite caracteres: ')
        if entrada != '0':
            arquivo1.write(f'{entrada}\n')
        else:
            break

print(arquivo1.closed)
print('-------lendo---------')

with open('daquest1.txt', 'r') as arquivo1:
    print(arquivo1.read())

print('fechado ? :', arquivo1.closed)

print('-----------------------------------')


#02

with open('daquest02.txt', 'r') as arquivo2:
    print(arquivo2.readlines())
    arquivo2.seek(0)
    print(f'numero de linhas: {len(arquivo2.readlines())}')

print('-----------------------------------')


#03
from unidecode import unidecode

contador = 0

with open('daquest02.txt', 'r') as arquivo3:
    vetor = arquivo3.readlines()
    for linha in vetor:
        for letra in linha:
            #print(unidecode(letra).lower())
            if unidecode(letra).lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                  #print(letra)
                  contador += 1

print('total de vogais:', contador)

print(unidecode('café'))
print(unidecode('à'))
print(unidecode('ü'))
print(unidecode('À'))
print(unidecode('Ü'))
print(unidecode('Ô').lower())

print('-----------------------------------')


"""



#04







print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')
print('-----------------------------------')




