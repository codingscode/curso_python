"""
Leitura de arquivos


Para ler o conteudo de um arquivo em Python, utilizamos a funcao integrada open().

open() -> Na forma mais simples de utilização nos passamos apenas um parametro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

OBS: por padrão, a funcao open() abre o arquivo para leitura. Este arquivo deve existir, ou então
teremos o erro FileNotFoundError

mode r -> modo de leitura. r -> read() -> ler


"""

arquivo1 = open('file065_arquivo1.txt')

print(arquivo1)
print(type(arquivo1))
"""
<_io.TextIOWrapper name='file065_arquivo1.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>
"""
print('---------------')

"""
Para ler o conteudo de um arquivo, após sua abertura, devemos utilizar a função read().
"""

arquivo1_1 = open('file065_arquivo1.txt')

print(arquivo1_1.read()) # imprime inclusive o espaço em branco

print('---------------')

"""

Obs: o python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona
 como o cursor quando estamos escrevendo.
Obs: a função read() lê todo o conteudo do arquivo
"""
print(arquivo1_1.read())  # nao imprime nada

print('---------------')

arquivo1_2 = open('file065_arquivo1.txt')

ret = arquivo1_2.read()

print(type(ret))
print(ret)

print('---------------')
