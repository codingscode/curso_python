"""
Escrever em arquivos


OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma
forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.


"""
# escrita - modo 'w' -> writing

with open('file068_texto.txt', 'w') as arquivo1:
    arquivo1.write('Escrever dados em arquivo é bacana.\n')
    arquivo1.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo1.write('Esta é a última linha.')

print('novo arquivo criado.')
"""
caso já exista um arquivo com o mesmo nome especificado, este será sobrescrito
"""
print('-----------------')

with open('file068_outro.txt', 'w') as arquivo2:
    arquivo2.write('Python\n'*8)

print('-----------------')

with open('file068_fruta.txt', 'w') as arquivo3:
    while True:
        fruta = input('digite a fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo3.write(f'{fruta}\n')
        else:
            break

print('-----------------')