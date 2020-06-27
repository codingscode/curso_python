"""
Instalando e utilizando módulos externos


utilizamos o gerenciador de pacotes python chamado pip(Python Installer Package)

link pacotes modulos externos oficiais https://pypi.org/


"""

"""
pip no terminal

"""

"""
pesquisar colorama
pip install colorama -> digitar isso no terminal
python -m pip install --upgrade pip

"""

"""
colorama -> é utilizado para permitir impressao de textos coloridos no terminal

"""
from colorama import init

init()

from colorama import Fore, Back, Style

print(Fore.BLUE + 'Python')
print(Fore.GREEN + 'Verde')
print(Fore.CYAN + 'Ciano')
print('Mais')
print(Style.RESET_ALL + 'Resetando tudo')
print(Fore.YELLOW + 'amarelo')
"""
dir(colorama)
help(colorama.colorama_text)


"""

print(Back.MAGENTA + 'Magenta')
print(Style.RESET_ALL + 'Resetando tudo')
