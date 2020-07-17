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

with open('daquest1.txt', encoding='utf-8') as arquivo1:
    print(arquivo1.read())

print('fechado ? :', arquivo1.closed)

print('-----------------------------------')


#02

with open('daquest02.txt', encoding='utf-8') as arquivo2:
    print(arquivo2.readlines())
    arquivo2.seek(0)
    print(f'numero de linhas: {len(arquivo2.readlines())}')

print('-----------------------------------')


#03
from unidecode import unidecode

contador = 0

with open('daquest02.txt', encoding='utf-8') as arquivo3:
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


#04

from unidecode import unidecode

contador = [0, 0]  # vogal | consoante

with open('daquest02.txt', encoding='utf-8') as arquivo4:
    vetor = arquivo4.readlines()
    for linha in vetor:
        for letra in linha:
            if unidecode(letra).lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                contador[0] += 1
            elif unidecode(letra).lower().isalpha() and unidecode(letra).lower() not in ['a', 'e', 'i', 'o', 'u', 'y']:
                contador[1] += 1
            else:
                pass

print(f'total de vogais: {contador[0]}')
print(f'total de consoantes: {contador[1]}')
print(f'soma vogal e consoante: {sum(contador)}')


nome1 = 'bü ir'
nome2 = 'borboleta'
nome3 = 'crachá'
nome4 = 'êita'

for letra in nome1:
    #print(f'{letra}: {unidecode(letra).lower()} | {letra.isalpha()}')
    if unidecode(letra).lower().isalpha() and unidecode(letra).lower() not in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(f'{letra} é consoante')
    elif unidecode(letra).lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(f'{letra} é  vogal')
    else:
        print(f'{letra} não é nem vogal ou consoante')

print('--------------------')


#05

from unidecode import unidecode

entrada = input('digite um caractere: ')
contador = 0
x = []

with open('daquest02.txt', encoding='utf-8') as arquivo5:
    vetor = arquivo5.readlines()
    for linha in vetor:
        for letra in linha:
            if unidecode(letra.lower()) == entrada:
                x.append(letra.lower())
                contador += 1

print(x)
print(f'{entrada} aparece {contador} vezes')
print(unidecode('Ó'.lower()))  # unidecode('í').lower() == 'a'

print('----------------')



"""

#06


from unidecode import unidecode

repetido = []
nao_repetido = set()  # ou {}

with open('daquest06.txt', encoding='utf-8') as arquivo6:
    vetor = arquivo6.readlines()
    for linha in vetor:
        for letra in linha:
            if unidecode(letra.lower()).isalpha():
                repetido.append(unidecode(letra.lower()))
            if unidecode(letra.lower()).isalpha():
                nao_repetido.add(unidecode(letra.lower()))


print(repetido)
print(nao_repetido)

n_repet_lista = list(nao_repetido)
print(n_repet_lista)




print('----------------')
print('----------------')
print('----------------')