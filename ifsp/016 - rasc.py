# Arquivos

# https://docs.python.org/3.6/library/functions.html#open

"""
r - abre arquivo só para leitura
w - abre arquivo só para editar e/ou criar
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

arquivo3 = open('novo_texto.txt', 'w')  # cria outro arquivo ou o edita
arquivo3.write('Testando, testando\n')
arquivo3.write('mais uma linha')
arquivo3.close()


print('-----------------')

arquivo4 = open('novo_texto.txt', 'w')    # sobrescreve o arquivo3
arquivo4.write('Novo texto, no mesmo arquivo')
arquivo4.close()


print('-----------------')

arquivo5 = open('novo_texto.txt', 'a')    # adiciona ao final do arquivo
arquivo5.write('\nTexto adicionado ao arquivo com o modo "a"')
arquivo5.close()

print('-----------------')


# abrindo no modo r+

arquivo6 = open('novo_arquivo.txt', 'r+')
arquivo6.write('Testando r+')
#arquivo6.seek(10)
arquivo6.write('Novo teste do r+')
#arquivo6.close()

arquivo6.seek(0)
print(arquivo6.read())
arquivo6.close()

print('-----------------')

"""

"""
