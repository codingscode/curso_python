"""
Modos de Abertura de Arquivo

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo já exista
x -> open for exclusive creation, failing if the file already exists
a -> open for writing, appending to the end of the file if it exists, nao se controla o cursor

http://docs.python.org/3/library/functions.html#open

"""

try:
    with open('file069_teste1.txt', 'x') as arquivo1:  # fora daqui, executado mais de uma vez dá erro
        arquivo1.write('teste de conteudo 1....')
except FileExistsError:
    print('arquivo já existe')


print('--------------------')

with open('file069_fruta.txt', 'a') as arquivo1:
    while True:
        fruta = input('digite a fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo1.write(f'{fruta}\n')
        else:
            break

print('--------------------')

with open('file069_japreenchido.txt', 'a') as arquivo2:
    arquivo2.seek(0)
    arquivo2.write('No topo\n')
    arquivo2.write('Nova linha\n')
    arquivo2.write('mais uma linha\n')

print('--------------------')

# +
with open('file069_japreenchido2.txt', 'a+') as arquivo3:
    arquivo3.seek(0)
    arquivo3.write('No topo4\n')
    arquivo3.write('Nova linha\n')
    arquivo3.write('mais uma linha\n')

print('--------------------')
print('--------------------')