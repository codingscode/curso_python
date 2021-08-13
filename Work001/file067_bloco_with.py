"""
Bloco With

trabalhar arquivos -> abrir, manipular, fechar arquivo.

o bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após
o bloco with.
"""

with open('file067_texto.txt') as arquivo1:  # forma pythonica
    print(arquivo1.readlines())
    print('fechado?', arquivo1.closed)

print('----------------------')

try:
    print(arquivo1.readlines())  # dá erro
except ValueError as erro:
    print(f'****: {erro}')
    print('arquivo já fechado ou arquivo inexistente')

print('fechado?', arquivo1.closed)

print('----------------------')
