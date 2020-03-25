# Arquivos

# https://docs.python.org/3.6/library/functions.html#open

"""
r - abre arquivo só para leitura
w - abre arquivo só para editar
a - abre arquivo só acrescentar no final dele
r+ - abre o arquivo tanto para ler quanto para editar



"""

arquivo = open('meu_texto.txt', 'r')  # r, w, a ou r+
print(arquivo.read())         #  se n é vazio ler tudo , read(n), n igual numero de caracteres a serem lidos

print('-----------------')

arquivo2 = open('meu_texto2.txt', 'r')

print(arquivo2.readline())
print(arquivo2.readlines())

print('-----------------')

arquivo3 = open('novo_texto.txt', 'w')  # cria outro arquivo
arquivo3.write('Testando, testando\n')
arquivo3.write('mais uma linha')
arquivo3.close()



