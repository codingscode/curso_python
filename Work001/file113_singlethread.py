
import time
from threading import Thread

CONTADOR = 5000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'tempo em segundos: {fim - inicio}')  # 0.8874497413635254
