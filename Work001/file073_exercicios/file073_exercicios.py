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

#print(repetido)
#print(nao_repetido)

n_repet_lista = list(nao_repetido)
#print(n_repet_lista)

frequencias = dict()

for caract_nr in n_repet_lista:
    frequencias[caract_nr] = repetido.count(caract_nr)

print(frequencias)
#print(list(frequencias.keys()))

[print(f'{cada} : {frequencias[cada]} vezes') for cada in frequencias]


print('----------------')


#07

from unidecode import unidecode

texto = ''
texto_enviado = ''

with open('daquest07.txt', encoding='utf-8') as arquivo7:
    vetor = arquivo7.readlines()
    for linha in vetor:
        texto += linha

print(texto)

for letra in texto:
    if unidecode(letra.lower()) in ['a', 'e', 'i', 'o', 'u', 'y']:
        letra = '*'
    texto_enviado += letra

print(texto_enviado)

with open('daquest07_enviado.txt', 'w', encoding='utf-8') as arquivo7_2:
    arquivo7_2.write(texto_enviado)

print('----------------')

#08

from unidecode import unidecode

texto = ''
texto_modificado = ''

with open('daquest08.txt', encoding='utf-8') as arquivo8:
    vetor = arquivo8.readlines()
    for linha in vetor:
        texto += linha

print(texto)

for letra in texto:
    texto_modificado += letra.upper()

print(texto_modificado)

with open('daquest08_enviado.txt', 'w', encoding='utf-8') as arquivo8_2:
    arquivo8_2.write(texto_modificado)

print('----------------')


#09

texto_1 = ''
texto_2 = ''
texto_enviado = ''

with open('daquest09.1.txt', encoding='utf-8') as arquivo9_1:
    vetor = arquivo9_1.readlines()
    for linha in vetor:
        texto_1 += linha

with open('daquest09.2.txt', encoding='utf-8') as arquivo9_2:
    vetor = arquivo9_2.readlines()
    for linha in vetor:
        texto_2 += linha

with open('daquest09_enviado', 'w', encoding='utf-8') as arquivo9_env:
    arquivo9_env.write(texto_1)
    arquivo9_env.write(texto_2)


print('----------------')

#10

lista = dict()

with open('daquest10_1.txt', encoding='utf-8') as arquivo10:
    vetor = arquivo10.readlines()
    for linha in vetor:
        par = linha.replace('\n', '').split(',')
        #print(par)
        lista[par[0]] = float(par[1])

print(lista)

maior = {'cidade': 'x', 'populacao': 0}

for cada in lista:
    if lista[cada] == max(lista.values()):
        maior['cidade'] = cada
        maior['populacao'] = max(lista.values())

print(maior)

with open('daquest10_env.txt', 'w', encoding='utf-8') as arquivo10_env:
    arquivo10_env.write(f'{maior["cidade"]} - {maior["populacao"]} habitantes')

# experimentar usando map

print('----------------')

#11
palavra = input('digite a palavra ser procurada: ')

contador = 0
texto = ''
texto_m = []

with open('daquest11.txt', encoding='utf-8') as arquivo11:
    vetor = arquivo11.readlines()
    for linha in vetor:
        texto += linha
        texto = texto.replace(',', '').replace('.', '').replace(';', '').replace('(', '').replace(')', '').replace('\n', ' ').replace('  ', ' ')
        texto_m = texto.split(' ')
    for cada in texto_m:
        if cada.lower() == palavra:
            contador += 1


print(texto_m)
print(f'{palavra} : {contador} vezes')

print('----------------')

#13

relacao = dict()
texto = ''


def colocar_dados(colocar):
    nome = ''
    telefone = ''
    while telefone != '0':
        nome = input('digite o nome: ')
        telefone = input('digite o telefone: ')
        colocar[nome] = telefone


colocar_dados(relacao)

print(relacao)


def para_texto():
    v = ''
    for cada in relacao:
        v += f'nome: {cada}, telefone: {relacao[cada]}\n'
    return v


texto = para_texto()
print(texto)

with open('daquest13.txt', 'w', encoding='utf-8') as arquivo13:
    arquivo13.write(texto)

print('----------------')


#14
from datetime import date, datetime

print(date(2020, 3, 1))
print(datetime.now())
print(date.today())

bob = date(1993, 7, 15)
idade_bob = date.today() - bob

print(idade_bob)
print(idade_bob.days // 365)  # anos

texto = []


with open('daquest14.txt', encoding='utf-8') as arquivo14:
    vetor = arquivo14.readlines()
    x = ''
    for linha in vetor:
        x = linha.replace('\n', '').split(', ')
        x[1] = x[1].split(' ')
        texto.append(x)


def para_texto(vetor):
    transf_texto = ''
    for cada in vetor:
        ano = int(cada[1][2])
        mes = int(cada[1][1])
        dia = int(cada[1][0])
        transf_texto += f'{cada[0]} {(date.today() - date(ano, mes, dia)).days//365} anos\n'
    return transf_texto


relacao = para_texto(texto)
print(relacao)


with open('daquest14_env.txt', 'w', encoding='utf-8') as arquivo14_env:
    arquivo14_env.write(relacao)

print('----------------')

#15
from datetime import date, datetime

print(date(2020, 3, 1))
print(datetime.now())
print(date.today())

bob = date(1993, 7, 15)
idade_bob = date.today() - bob

print(idade_bob)
print(idade_bob.days // 365)  # anos

texto = []


with open('daquest15.txt', encoding='utf-8') as arquivo15:
    vetor = arquivo15.readlines()
    x = ''
    for linha in vetor:
        x = linha.replace('\n', '').split(', ')
        x[1] = x[1].split(' ')
        texto.append(x)


def verificar_idade(anos):
    if anos < 18:
        return 'menor de idade'
    elif anos > 18:
        return 'maior de idade'
    return 'entrando na maior idade'


def para_texto(iteravel):
    transf_texto = ''
    for cada in iteravel:
        ano = int(cada[1][2])
        mes = int(cada[1][1])
        dia = int(cada[1][0])
        idade = (date.today() - date(ano, mes, dia)).days/365
        transf_texto += f'{cada[0]} {int(idade)} anos, {verificar_idade(idade)}\n'
    return transf_texto


relacao = para_texto(texto)
print(relacao)


with open('daquest15_saida.txt', 'w', encoding='utf-8') as arquivo15_saida:
    arquivo15_saida.write(relacao)

print('----------------')

#16

meu_vetor = [1, 2, 14, 21, 10, 30, 40, 7, 5, 50]

print(meu_vetor)


def minha_saida(entrada):
    uma_string = ''
    for cada in entrada:
        uma_string += f'{bin(cada)[2:]}\n'
    return uma_string


enviar = minha_saida(meu_vetor)

with open('daquest16_saida.txt', 'w', encoding='utf-8') as arquivo16_saida:
    arquivo16_saida.write(enviar)

x = 'borboleta'
print(x[2:])

k = '100'
y = '201'
print(int(k, 2))  # binario para int base 10
print(int(y, 3))


print('----------------')


"""

#19
nomes_notas = []


def pares(vetor):
    matriz = []
    for cada in vetor:
        cada = cada.replace('Nome: ', '').replace('\n', '')
        cada = cada.split(' Nota: ')
        cada[1] = float(cada[1])
        matriz.append(cada)
    return matriz


with open('daquest19.txt', encoding='utf-8') as arquivo19:
    lista = arquivo19.readlines()
    #print(lista)
    nomes_notas = pares(lista)


print(nomes_notas)
maior = max(nomes_notas, key=lambda cada: cada[1])
print(maior)

print('----------------')




print('----------------')
print('----------------')