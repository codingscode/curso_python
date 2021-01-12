"""
Tipos de Dados mais precisos

int, str, float, List, Set, Dict, etc


- Literal type
- Union
- Final
- Typed dictionaries
- Protocols


"""


def dobro(valor: int) -> int:
    return valor*2


print(dobro(8))
print(dobro(8.7))
print(dobro('pula-pula '))

"""
executar no terminal da pasta do arquivo: mypy file127_tipos_dados_mais_precisos.py
"""

print('1---------------------')
# Literal type

from typing import Literal, Union, Final, final, TypedDict, Protocol


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcular_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcular_v1('+', 4, 5)
calcular_v1('-', 10, 7)
#calcular_v1('/', 10, 5)  # chama o erro, mas o mypy nao acha
"""
usar o mypy
"""

print('2---------------------')


def calcular_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcular_v2('+', 4, 5)
calcular_v2('-', 10, 7)
#calcular_v2('/', 10, 5)  # chama o erro, mas o mypy acha


print('3---------------------')
# Union


def somar(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado


print('4---------------------')
# Final

NOME: Final = 'Geek'
print(NOME)

NOME = 'University'
print(NOME)
"""
usar o mypy
"""

print('5---------------------')


@final  # isto significa que nenhuma classe pode estender esta. Verificar os erros com o mypy
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')

"""
no terminal da pasta:  mypy file127_tipos_dados_mais_precisos.py
"""

print('6---------------------')
# Typed Dictionaries


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)
outro = CursoPython(algo='vai', coisa=True)
print(outro)
"""
no terminal da pasta:  mypy file127_tipos_dados_mais_precisos.py
"""

print('7---------------------')
# Protocols


class Curso(Protocol):
    titulo: str




"""
class Curso(Protocol):
    titulo: str

    def __init__(self):
        self.titulo = 'Codando em Python'

"""


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    pass


"""
class Venda:
    titulo = 'Oi'
"""


v1 = Venda()
estudar(v1)  # dá erro, 'Venda' object has no attribute 'titulo'


#c1 = Curso()
#estudar(c1)



print('8---------------------')
print('9---------------------')
