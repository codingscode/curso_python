"""
Debuggando com PDB

PDB - Python Debugger

Bug -> inseto

"""

"""
podemos fazer isso em diferentes IDEs, como o PyCharm ou o PDB(Python Debbuger)
"""
# com o pycharm
     # clicar em debbug, antes marcar breakpoints


def dividir(a, b):
    try:
        return float(a)/float(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'ocorreu um problema: {erro}'


print(dividir(5, 2))

print('-----------------------------')
# exemplo com PDB
      # importa-se a biblioteca pdb e depois a função set_trace
      # exemplo 1
"""
comandos básicos do PDB:
l -> listar onde estamos no código
n -> próxima linha
p -> imprime variavel
c -> continua a execucao (finaliza o debugging)
nome_da_variavel ->


"""
# exemplo 2
import pdb

nome = 'Felicia'
sobrenome = 'Stone'
#pdb.set_trace()   # desmarcar
nome_completo = f'{nome} {sobrenome}'
curso = 'programando em Python'
final = f'{nome_completo} faz o curso {curso}'
print(final)

print('-----------------------------')

nome2 = 'Stefani'
sobrenome2 = 'oliveira'
#import pdb; pdb.set_trace()  # desmarcar
nome_completo2 = f'{nome2} {sobrenome2}'
curso2 = 'programando em javascript'
final2 = f'{nome_completo2} faz o curso {curso2}'
print(final2)

"""
por que o utilizar este formato?
o debug é utilizado durante o desenvolvimento. é costume usar os imports no inicio do arquivo.
por isso, ao invés de colocarmos o import do pdb no inicio do arquivo, nós colocamos somente onde 
vamos debuggar, e ao finalizar já fazemos a remoção.

"""

print('-----------------------------')
# exemplo 3
"""
a partir da versao 3.7, nao é mais necessario importar a biblioteca pdb, pois o comando de debug
foi incorporado como funcao built-in(funcao integrada) chamada breakpoint()
"""

nome2 = 'Stefani'
sobrenome2 = 'oliveira'
#breakpoint()   # desmarcar
nome_completo2 = f'{nome2} {sobrenome2}'
curso2 = 'programando em javascript'
final2 = f'{nome_completo2} faz o curso {curso2}'
print(final2)

print('-----------------------------')
"""
OBS: cuidado com conflitos entre nomes de variaveis e os comandos do pdb
"""


def soma(l, n, p, c):  # os nomes dos parametros coincidem com os comandos l, n, p e c
    #breakpoint()  # desmarcar
    return l + n + p + c


print(soma(1, 2, 3, 4))
"""
como os nomes das variaveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para 
imprimir as variaveis ou seja: p nome da variavel
"""
