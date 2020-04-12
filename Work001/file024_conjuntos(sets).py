"""
Conjuntos

se refere a Teoria dos Conjuntos(Matemática)
no python chama-se Set.

Sets não possuem valores duplicados
Sets não possuem valores ordenados
Elementos não são acessados via índice, ou seja, não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos
com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

os conjuntos são referenciados por '{}'
conjuntos não tem chaves/valores, apenas valor(es).

"""

# Definindo um conjunto
# forma 1

conjunto_1 = set({2, 3, 4, 2, 3, 5, 3, 5})  # há valores repetidos

print(f'{conjunto_1} || seu tipo: {type(conjunto_1)}')

# forma 2 (mais comum)

conjunto_2 = {3, 21, 5, 10, 21, 10, 3}
print(f'{conjunto_2} || seu tipo: {type(conjunto_2)}')

print('------------\n')

uma_string1 = 'paçoca'
paraset1 = set(uma_string1)
print(paraset1)

uma_lista = [2, 2, 4, 0, 4, 5, 6]
paraset2 = set(uma_lista)
print(paraset2)

uma_tupla = (2, 2, 4, 0, 4, 5, 6)
paraset3 = set(uma_tupla)
print(paraset3)

# verificar se o conjunto contem determinado elemento

conjunto_3 = {0, 2, 4, 5, 6}

if 4 in conjunto_3:
    print('possui o 4')
else:
    print('não possui o 4')

print('---------------\n')

# não temos valores repetidos e nem ordem em conjuntos

dados = [13, 4, 42, 17, 21, 21, 4, 10]

lista_1 = list(dados)
print(f'lista: {lista_1} || tamanho: {len(lista_1)}')

tupla_1 = tuple(dados)
print(f'tupla: {tupla_1} || tamanho: {len(tupla_1)}')

dicionario_1 = {}.fromkeys(dados, 'dict')  # n aceita chaves repetidas
print(f'Dicionario: {dicionario_1} || tamanho: {len(dicionario_1)}')

conjunto_4 = {13, 4, 42, 17, 21, 21, 4, 10}  # n aceita valores repetidos
print(f'conjunto: {conjunto_4} || tamanho: {len(conjunto_4)}')

print('---------------\n')

# pode-se misturar tipos de valores
conjunto_5 = {1.2, 4, True, 'codigo', 0}
print(f'{conjunto_5} || seu tamanho: {len(conjunto_5)}')

# podemos iterar em um set
for valor in conjunto_5:
    print(valor)

print('---------------\n')

# usos interessantes com set
"""
Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
informam manualmente a cidade de onde vieram.

Nós adicionamos cada cidade em uma lista Pyhon, já que em uma lista podemos adicionar novos 
elementos e ter repetição.
 
"""
cidades = ['taubaté', 'jundiaí', 'taubaté', 'santos', 'niterói', 'cuiabá', 'santos']
print(f'{cidades} || numero de pessoas: {len(cidades)}')
print(f'numeros de cidades: {len(set(cidades))}')

print('---------------\n')

# adicionando elementos a um conjunto
conjunto_6 = {2, 3, 4, 5}
conjunto_6.add(6)
conjunto_6.add(6)
conjunto_6.add(10)
print(conjunto_6)

# removendo elementos de um conjunto
conjunto_7 = {10, 11, 12, 13}
    # forma 1
conjunto_7.remove(13)  # é valor, não é indice.
#conjunto_7.remove(41) dá erro
print(conjunto_7)

    # forma 2
conjunto_7.discard(11)
conjunto_7.discard(72)  # n dá erro
print(conjunto_7)

print('--------------------\n')

# copiando um conjunto para outro...
     # aceita deep copy e shallow copy
conjunto_7.clear()
print(conjunto_7)

print('--------------------')
# Métodos matemáticos de conjuntos

estudantes_python = {'simon', 'vicente', 'larissa', 'geovana', 'samuel', 'tobias'}
estudantes_java = {'tom', 'vicente', 'gilbert', 'geovana', 'steve'}

# Precisamos gerar um conjunto com nomes de estudantes únicos
# Forma 1 - utilizando union

unicos1 = estudantes_python.union(estudantes_java)
unicos2 = estudantes_java.union(estudantes_python)

print(f'unicos1: {unicos1}')
print(f'unicos2: {unicos2}')   # igual ao de cima

# Forma 2 - utilizando o caractere pipe |
unicos3 = estudantes_python | estudantes_java
print(f'unicos3: {unicos3}')

# gerar um conjunto de alunos que estão em ambos os cursos
# Forma 1 - utilizando o intersection()

ambos1 = estudantes_python.intersection(estudantes_java)
print(f'ambos1: {ambos1}')

# Forma 2 - utilizando o &
ambos2 = estudantes_python & estudantes_java
print(f'ambos2: {ambos2}')


# gerar um conjunto de estudantes que só pertencem ou ao curso python ou ao curso java
    # só python
somente_python = estudantes_python.difference(estudantes_java)
print(f'somente python: {somente_python}')

    # só java
somente_java = estudantes_java.difference(estudantes_python)
print(f'somente java: {somente_java}')

print('-------------------\n')

# Soma de valores, máximo, mínimo, tamanho

   # se os valores forem todos inteiros ou reais
conjunto_atual = {5, 7, 20, 12, 30, 15}
print(f'soma: {sum(conjunto_atual)}')
print(f'maximo: {max(conjunto_atual)}')
print(f'minimo: {min(conjunto_atual)}')
print(f'tamanho: {len(conjunto_atual)}')








