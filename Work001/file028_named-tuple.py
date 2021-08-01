"""
Modulo Collections - named tuple

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também
parametros.

"""

# importando
from collections import namedtuple

# precisamos definir o nome e parametros
  # forma 1 - declaração named tuple
cachorro = namedtuple('cachorro', 'idade raca nome')
print(cachorro)

  # forma 2 - declaração named tuple
cachorro2 = namedtuple('cachorro2', 'idade, raca, nome')

  # forma 3 - declaração named tuple
cachorro3 = namedtuple('cachorro3', ['idade', 'raca', 'nome'])

# usando
madruguinha = cachorro3(idade=2, raca='pitchie', nome='madruguinha')

# acessando dados.        Forma 1
print(madruguinha)
print(f'{madruguinha[0]} | {madruguinha[1]} | {madruguinha[2]}')  # idade | raca | nome

#                       Forma 2
print(f'{madruguinha.idade} | {madruguinha.raca} | {madruguinha.nome}')

print(f'{madruguinha.index("pitchie")} | {madruguinha.count("pitchie")}')
print('--------------------------')
print(dir(madruguinha))
print(dir(namedtuple))
