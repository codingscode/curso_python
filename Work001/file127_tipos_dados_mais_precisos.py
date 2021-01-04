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

from typing import Literal, Union


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
calcular_v1('/', 10, 5)  # chama o erro, mas o mypy nao acha
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
calcular_v2('/', 10, 5)  # chama o erro, mas o mypy acha


print('3---------------------')
# Union


def somar(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado






print('4---------------------')
print('5---------------------')
print('6---------------------')
