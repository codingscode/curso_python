"""
Seek e Cursors

seek() -> utilizada para movimentar o cursor pelo arquivo.


"""

arquivo1 = open('file066_arquivo1.txt')

print(arquivo1.read())

print('---------------------')
print('p1:\n')
print('nao tem')
print(arquivo1.read())  # fica vazio

print('---------------------')
print('p2:\n')

arquivo2 = open('file066_arquivo1.txt')

print(arquivo2.read())

print('---------------------')
print('p3:\n')

"""
seek() -> esta funcao é utilizada para movimentacao do cursor pelo arquivo. Ela recebe um parametro que
indica onde queremos colocar o cursor.

"""
# movimentando o cursor pelo arquivo com a funcao seek()

arquivo2.seek(0)
print(arquivo2.read())  # agora ler do começo

print('---------------------')
print('p4:\n')

print(arquivo2.read())

print('---------------------')
print('p5:\n')

arquivo2.seek(20)
print(arquivo2.read())

print('---------------------')
print('p6:\n')

arquivo3 = open('file066_arquivo1.txt')
retorno1 = arquivo3.readline()
"""
readLine() -> funcao que lê o arquivo linha a linha
"""

print(retorno1)  # 1ª linha
print(retorno1)  # 2ª linha
print(f'----> {type(retorno1)}')

print(retorno1.split(' '))

print('---------------------')
print('p7:\n')

arquivo4 = open('file066_arquivo1.txt')
print(arquivo4.readlines())
print(f'comprimento: {len(arquivo4.readlines())}')

arquivo4.seek(0)
print(f'comprimento: {len(arquivo4.readlines())}')

"""
Obs: quando abrimos um arquivo com a funcao open() é criada uma conexão entre o arquivo no disco do 
computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o 
arquivo devemos fechar essa conexão. Para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:
1 - abrir o arquivo; 2 - trabalhar o arquivo; 3 - fechar o arquivo
"""

print('---------------------')
print('p8:\n')

# 1
arquivo5 = open('file066_arquivo1.txt')

# 2
print(arquivo5.read())
print('está fechado:', arquivo5.closed)  # verifica se o arquivo está aberto ou fechado

# 3
arquivo5.close()
print('está fechado:', arquivo5.closed)
#print(arquivo5.read()) # dá erro
"""
Obs: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
"""

print('---------------------')
print('p9:\n')

arquivo6 = open('file066_arquivo1.txt')
print(arquivo6.read(50))  # os 50 primeiros caracteres

print('---------------------')
