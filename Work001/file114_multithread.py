import time
from threading import Thread

CONTADOR = 5000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'tempo em segundos: {fim - inicio}')  # 0.631615161895752

