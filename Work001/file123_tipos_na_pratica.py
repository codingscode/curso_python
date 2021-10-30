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

print(__annotations__)

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


def distribuir_cartas(baralho):
    """gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


baralho = criar_baralho()
print(distribuir_cartas(baralho))  # tupla também ser representadas por virgula

print('4------------------')


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

print('5------------------')
