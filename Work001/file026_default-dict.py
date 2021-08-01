"""

Modulo Collections - Default Dict

Default Dict - Ao criar um dicionario utilizando-o, nós informamos um valor default(padrão), podendo
utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor de default
será atribuído.

OBS: lambdas são funções sem nome, que podem ou não receber parametros de entrada e retornar
valores.

https://docs.python.org/3/library/collections.html#collections.defaultdict

"""

dicionario_1 = {'curso': 'Programando em Python'}

print(f'{dicionario_1} || {dicionario_1["curso"]}')

#print(dicionario_1['outro']) # dá erro, chave não existente
print('-----------\n')

# fazendo import
from collections import defaultdict

dicionario_2 = defaultdict(lambda: 0)
print(dicionario_2)

dicionario_2['curso'] = 'ML com Python'  # criando atributo/propriedade
print(dicionario_2)

print(dicionario_2['outro'])   # não dá erro, KeyError, vem o 0 de lambda
print(dicionario_2)
print('------------')