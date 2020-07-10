"""
Sistema de Arquivos e Navegação

para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do
modulo os(Operating System).
"""

import os

# getcwd() -> current work directory (diretorio de trabalho atual)
print(os.getcwd())

# mudando diretorio
os.chdir('../..')  # '../..' , assim sucessivamente

print(os.getcwd())

# podemos checar se um diretório e absoluto(começa da raiz) ou relativo()
print(os.path.isabs('C:\\olddoc'))  # windows

print(os.path.isabs('..'))

print('geek\\university')

print('------------------------')

# podemos identificar o sitema operacional com o modulo os
print(os.name)  # se 'nt' -> windows, se 'posix' -> linux ou mac

# podemos ter mais detalhes do sistema operacional
import sys

print(sys.platform)  # para linux ou mac -> os.uname()


print('------------------------')
print('------------------------')
print('------------------------')
print('------------------------')















