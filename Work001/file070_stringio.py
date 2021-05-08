"""
StringIO

OBS: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissao:
    - Permissao de leitura: para ler o arquivo
    - Permissao de escrita: para escrever o arquivo

StringIO -> utilizado para ler e criar arquivos em memória.

"""

from io import StringIO

mensagem = 'Esta é uma string comum'

#Podemos criar um arquivo em memoria já com uma string inserida ou mensagem vazia para inserirmos texto
# depois

arquivo1 = StringIO(mensagem)
# arquivo1 = open('file070_texto1.txt', 'w')  sao equivalentes

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo1.read())

# escrevendo outros textos
print(arquivo1.write(' Outro texto'))

print(arquivo1.read())

# movimentando cursor
arquivo1.seek(0)
print(arquivo1.read())

print('---------------')