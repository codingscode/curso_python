"""
Sistema de arquivos Manipulação


"""
import os

# descobrindo se um diretorio ou arquivo existe
   # para arquivos
print(os.path.exists('nao_existe.txt'))
print(os.path.exists('file002.py'))

   # para diretorio
print('01', os.path.exists('pasta_naotem'))
print('02', os.path.exists('file063_pacotes'))
print('03', os.path.exists('file063_pacotes/dentro'))
print('04', os.path.exists('file063_pacotes/nao_tem'))
print('05', os.path.exists('./file063_pacotes/dentro/dentro_01.py'))  # diretorio e arquivo

   # exemplo com caminho absoluto
print('06', os.path.exists('/etc'))  # C:\\data
print('07', os.path.exists('/tem_nao'))  # C:\\tem_nao
print('08', os.path.exists('/dev'))  # C:\\dosbox

print('1---------------------')
# criando arquivos

    # forma 1
open('file072_texto1.txt', 'w').close()

    # forma 2
open('file072_texto2.txt', 'a').close()

    # forma 3
with open('file072_texto3.txt', 'w') as arquivo1:
    pass

print('2---------------------')

"""
os.mknod('file072_text04.txt') n funcionou
os.mknod('dofile072/file072_text05.txt')  n funcionou

se você estiver usando no mac os, pode haver um erro de PermissionError
obs: criando um arquivo viaknode() se o arquivo já existir teremos o erro FileExistsError

"""

print('3---------------------')

try:
    os.mkdir('file072pasta')   # pode-se criar um caminho absoluto também
except FileExistsError as erro:
    print(f'*** {erro}')
    print('diretorio já existente')

"""
a funcao mkdir() cria um diretorio se este não existir. Caso não exista, teremos FileExistsError
"""

print('4---------------------')

try:
    os.mkdir('file072pasta2/dentro1/dentro2') # fora daqui há erro, poderia se criar um a um
except FileNotFoundError as erro:
    print(f'*** {erro}')
    print('há erro ao se criar um diretório num diretório não existente')

print('5---------------------')
# forma abrangente

try:
    os.makedirs('file072pasta3/dentro1/dentro2')  # arvore de diretorios
except FileExistsError as erro:
    print(f'*** {erro}')
    print('já existe a árvore de diretórios')

# para evitar mostrar erro passa-se como 2ª parametro 'exist ok=True' em makedirs

print('6---------------------')

try:
    os.rename('file072_nomemudara', 'file072_nomemudou')
except FileNotFoundError as erro:
    print('diretorio não encontrado ou já renomeado')

# se o diretorio que queremos renomear não estiver vazio, teremos um OSError

try:
    os.rename('file072_nomemudara/de_dentro/x.txt', 'file072_nomemudara/de_dentro/y.txt')  # comentar o de cima para n interferir
except FileNotFoundError as erro:
    print('arquivo não encontrado ou já renomeado')

print('7---------------------')
# Removendo arquivos
# obs: atenção: tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou
# diretorio, eles nao vão para a lixeira. Eles somem

try:
    os.remove('file072_seraremovido.txt')
    print('apagado')
except FileNotFoundError as erro:
    print('arquivo nao encontrado ou já removido')

# obs: se você estiver no windows e o arquivo que você for deletar estiver em uso, você terá um erro
# obs: se você informar um diretorio ao invés de um arquivo, teremos um IsADirectoryError

try:
    os.rmdir('diretorio_naoexistente')
    print('diretorio apagado com sucesso')
except FileNotFoundError as erro1:
    print('diretorio nao existente ou já apagado')
except OSError as erro2:
    print('o diretorio contem arquivos, n pode ser removido')

print('8---------------------')
# removendo uma arvores de diretorios ???

try:
    for arquivo in os.scandir('file072_dentros'):
        if arquivo.is_file():
            os.remove(arquivo.path)
        if not arquivo.is_file():
            os.rmdir(arquivo.path)
except OSError as erro:
    print(erro)
    print('*** há erro')

print('9---------------------')
"""
no terminal digitar: pip install send2trash
"""
from send2trash import send2trash


send2trash('file_072_outroapague.txt')   # vai pra lixeira, pode ser restaurado
print('apagado ou já apagado')

print('---------------------')
print('---------------------')
