"""
http://mypy-lang.org/

no terminal: pip install mypy

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'*'*len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')


print(cabecalho('codando em python'))
print(cabecalho('usando django em python', alinhamento=False))
print(cabecalho('code em python', alinhamento='geek'))  # agora checa

print('1-----------------')
"""
terminal da pasta do arquivo: mypy file120_mypy.py

file120_mypy.py:18: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
Found 1 error in 1 file (checked 1 source file)

"""

print('2-----------------')
