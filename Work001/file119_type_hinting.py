"""
type hinting

"""


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Python'))
print('1-------------------')
"""
def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'*'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('codando em python'))
print(cabecalho('usando django em python', alinhamento=False))  # ou cabecalho('usando python em django', False)

"""
print('2-------------------')


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'*'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('codando em python'))
print(cabecalho('usando django em python', alinhamento=False))  # ou cabecalho('usando python em django', False)
print(cabecalho('code em python', alinhamento='geek'))

print('3-------------------')
