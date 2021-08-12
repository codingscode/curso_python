"""
Pacotes

modulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos
pacote -> é um diretório contendo uma coleção de módulos


obs: nas versoes 2.x do python, um pacote python deveria conter dentro dele um arquivo chamado
 __init__.py
nas versoes do python 3.x não é mais obrigatoria a utilização deste arquivo, mas normalmente ainda
 é utilizado para manter compatibilidade.

pypi.org/account/register

"""

from file063_pacotes import modulo_01, modulo_02

from file063_pacotes.dentro import dentro_01, dentro_02

print(modulo_01.pi)

print(modulo_01.funcao1(4, 6))
print('------------------------')

print(modulo_02.curso)
print(modulo_02.funcao2())

print('------------------------')

print(dentro_01.funcao3())

print('------------------------')

print(dentro_02.funcao4())

"""
from file063_pacotes.modulo_01 import funcao1
from file063_pacotes.dentro.dentro_02 import funcao4

print(funcao1(2, 3))
print(funcao4())
"""
