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

# podemos checar se um diretório é absoluto(começa da raiz) ou relativo()
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

print(os.getcwd()) #

os.chdir('./PycharmProjects/Work001')

print(os.getcwd())  #
res = os.path.join(os.getcwd(), 'file063_pacotes') #, 'dentro do pacote anterior..)'  # acessa outro diretorio

os.chdir(res)

print(os.getcwd())  #

"""
veja que o os.path.join() recebe dois parametros, sendo o 1º o diretorio atual e o 2º o diretório 
que será juntado ao atual.
"""

print('------------------------')

# podemos listar os arquivos e diretorios com o listdir()

os.chdir('..')
print(os.listdir())
print(os.listdir('C:\\'))

print('------------------------')
# podemos listar os arquivos e diretorios com mais detalhes com scandir()

print(list(os.scandir()))

arquivos = list(os.scandir())

print(arquivos)
print(arquivos[0])
print(dir(arquivos[0]))
print(arquivos[0].name)  # nome do arquivo escolhido
print('inode: ->', arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].path)
print(arquivos[0].stat())  # estatisticas

# OBS: quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

print('------------------------')
# forma mais adequada
scanner = os.scandir()

arquivos2 = list(scanner)

print(arquivos2)
print(arquivos2[0])
print(dir(arquivos2[0]))
print(arquivos2[0].name)  # nome do arquivo escolhido
print('inode: ->', arquivos2[0].inode())
print(arquivos2[0].is_dir())
print(arquivos2[0].is_file())
print(arquivos2[0].is_symlink())
print(arquivos2[0].path)
print(arquivos2[0].stat())  # estatisticas

scanner.close()

print('------------------------')