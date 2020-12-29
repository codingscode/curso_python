"""
jogo_cartas_v1

"""

nomes: list = ['Geek', 'Universit']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5, 6}


print(nomes)
print(versoes)
print(opcoes)
print(valores)

#print(__annotations__)

print('1------------------')

from typing import Dict, List, Tuple, Set


nomes2: List[str] = ['Geek', 'Universit']

versoes2: Tuple[int, int, int] = (3, 4, 7)

opcoes2: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores2: Set[int] = {3, 4, 5, 6}

print(nomes2)
print(versoes2)
print(opcoes2)
print(valores2)

print(__annotations__)

print('2------------------')
"""
https://www.alt-codes.net/suit-cards.php

"""

import random

NAIPES = '♠ ♥ ♣ ♦'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


print(NAIPES)
print(CARTAS)

print(criar_baralho())
print(f'{len(criar_baralho())} cartas')


print('3------------------')
print('4------------------')
print('5------------------')
print('6------------------')

