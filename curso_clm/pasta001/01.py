"""
jogo da adivinhação


"""
import random

#n = int(input('digite um número inteiro: '))

aleatorio = int(random.uniform(0, 11))

total_tentativas = 3
chutes = [-2]

print(aleatorio)

while ((len(chutes) == 3 + 1) or (chutes[-1] == aleatorio)) is False:
    n = int(input('digite um número inteiro: '))
    chutes.append(n)
    print(chutes)
    print(f'tamanho: {len(chutes)} || ultimo: {chutes[-1]}')
    print(f'aleatorio: {aleatorio}')














