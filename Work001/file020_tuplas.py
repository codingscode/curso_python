# tuplas(tuple)

umatupla = ()

print(type(umatupla))

tupla1 = (2, 3, 8, 10)
print(tupla1)

tupla2 = 4, 9, 5, 16    # também é tupla sem parenteses ()
print(type(tupla2))
print(tupla2)

naotupla = (8)    # não é tupla
print(f'{naotupla}, e seu tipo é : {type(naotupla)}')

tupla3 = (8, )   # isso é uma tupla
print(f'{tupla3} ....   e seu tipo é : {type(tupla3)}')

tupla4 = 6,
print(f'{tupla4}  // seu tipo é : {type(tupla4)}')

# conclusão1: podemos concluir que tuplas são definidas pela virgula e não pelo parenteses

# podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)

tupla5 = tuple(range(11))  # 0 a ?-1
print(f'{tupla5} // e seu tipo é : {type(tupla5)}')

# desempacotamento de tupla

tupla6 = ('python é legal', 'curso python')
opiniao, curso = tupla6

print(opiniao + ' // ' + curso)

# obs: gera erro se colocarmos um numero de elementos diferentes para desempacotar

# não existe adição/remoção de tuplas, pois estas são imutáveis
print('-----------')

# Soma / Valor Maximo/ Valor Minimo/ Tamanho
#- Se os valores forem todos inteiros ou reais

tupla7 = (3, 4, 5, 6)  # uma string aqui dentro daria erro nas 3 1ª funções
print(f'soma é {sum(tupla7)}')
print(f'maximo é {max(tupla7)}')
print(f'minimo é {min(tupla7)}')
print(f'o tamanho é {len(tupla7)}')

print('-----------')
# concatenação de tuplas

tupla8 = (1, 2, 3)
tupla9 = (4, 5, 6)

print(tupla8 + tupla9)

tupla8 = tupla8 + tupla9   # tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla8)

# verificar se determinado elemento está contido na tupla
tupla10 = (2, 3, 4, 5, 6)

print(4 in tupla10)   # Booleano
print(50 in tupla10)
print('----------------')

tupla11 = (4, 5, 6, 7)

for n in tupla11:
    print(n)

print('----------------')
for indice, valor in enumerate(tupla11):
    print(indice, valor)

print('----------------')

# contando elementos dentro de uma tupla
tupla12 = ('a', 'b', 'a', 'c', 'b', 'f', 'f', 'a')

print(f'quantos a : {tupla12.count("a")}')  # quantas vezes o a
print(f'quantos f : {tupla12.count("b")}')
print(f'quantos j : {tupla12.count("j")}')

area = tuple('machine learning') # transforma a string em tupla
print(area)

print(area.count('n'))

areax = ('m', 'a', 'c', 'h', 'i', 'n', 'e', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g')
transformar = ''.join(areax)

print(transformar)
print('---------------')

# dicas na utilização de tuplas
# quando n se precisa alterar dados em uma coleção
# Exemplo 1
meses = () # dentro 'janeiro', 'fevereiro', ...

# acesso a elementos
tupla12 = (4, 5, 8, 10, 12)

print(tupla12[2])
print(tupla12[3])

# Iterar com o while
i = 0

while i < len(tupla12):
    print(f'elemento {i} : {tupla12[i]}')
    i += 1

print('---------------')

transportes = ('carro', 'moto', 'bicicleta', 'patinete', 'navio', 'avião', 'lancha')
nomes1 = ('joao', 'horacio', 'socrates', 'aristoteles', 'horacio', 'aristoteles', 'joao', 'monica')

print(transportes.index('patinete'))   # encontrar a ordem
print(transportes.index('lancha'))
#print(transportes.index('skate'))    # lancha
print(nomes1.index('horacio'))
print(nomes1.index('joao', 3))
print('----------')

#slice
# tupla[inicio:fim:passo]
print(transportes[3:])  # do indice 3 até o final
print(transportes[:4])  # do começo até o indice 4
print(transportes[1:5])
print(transportes[0:6:2])

# Por que tuplas
# tuplas são mais rápidas do que listas
# tuplas deixam seu codigo mais seguro
# isso pois elementos imutaveis
print('--------------')

# copiando uma tupla para outra
tupla13 = (5, 6, 8, 10)
outratupla = tupla13   # na tupla não há problema de shallow copy

print(tupla13)
tupla13 = (100, 200, 300)

print(tupla13)
print(outratupla)
print('----------')

tupla14 = 1, 2, 3
print(tupla14)
print(type(tupla14))

#tupla = (1, 2, 3)
# dir(tupla)   em console
