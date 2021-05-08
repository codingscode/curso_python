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
import colorama
dir(colorama):
        ['AnsiToWin32', 'Back', 'Cursor', 'Fore', 'Style', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'ansi', 'ansitowin32', 'colorama_text', 'deinit', 'init', 'initialise', 'reinit', 'win32', 'winterm']
help(colorama.colorama_text)

"""

print(Back.MAGENTA + 'Magenta')
print(Style.RESET_ALL + 'Resetando tudo')
