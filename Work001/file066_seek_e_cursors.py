"""
Seek e Cursors

seek() -> utilizada para movimentar o cursor pelo arquivo.


"""

arquivo1 = open('file066_arquivo1.txt')

print(arquivo1.read())

print('---------------------')
print('nao tem')
print(arquivo1.read())  # fica vazio

print('---------------------')

arquivo2 = open('file066_arquivo1.txt')

print(arquivo2.read())



print('---------------------')

"""
seek() -> esta funcao é utilizada para movimentacao do cursor pelo arquivo. Ela recebe um parametro que
indica onde queremos colocar o cursor.

"""
# movimentando o cursor pelo arquivo com a funcao seek()

arquivo2.seek(0)
print(arquivo2.read())  # agora ler do começo

print('---------------------')

print(arquivo2.read())

print('---------------------')



