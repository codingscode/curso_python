"""
Módulos e Módulo random

em python, modulos são nada mais que outros arquivos python.

módulo random -> possui varias funcoes para geração de numeros pseudo-aleatorio

"""
"""
obs: existem duas formas de se utilizar um modulo ou funcoes deste
"""
# forma 1 -> importando todo o módulo (não recomendado)

"""
ao realizar o import de todo o modulo, todas as funções, atributos, classese e propriedades que 
estiverem dentro do modulo ficarão disponíveis (ficarão em memória).
caso você saiba quais funções você precisa utilizar deste modulo, então esta não seria a forma ideia
 de utilização. a forma 2 é melhor
# dir(random)
# help(random.random)
"""

import random

print(random.random())

"""
random() -> gera um numero pseudo-aleatorio entre 0 e 1
para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da 
função separados por ponto.
nao confunda pois neste caso tanto um quanto outro tem o mesmo nome
"""
print('------------------')
# forma 2 -> recomendada

from random import random

for i in range(10):
    print(f'{i}: {random()}')


print('------------------')

# uniform() -> gerar um numero pseudo-aleatorio entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(f'{i}: {uniform(3, 7)}')  # o 7 não é incluido


print('------------------')
# randint() -> gera valores pseudo-aleatorios(pode haver repetição) entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=' ')  # 1 a 61-1

print('\n------------------')
# choice() -> mostra um valor aleatorio entre um iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
uma_string = 'codando python'

print(choice(jogadas))
print(f'-> {choice(uma_string)}')

print('------------------')

from random import shuffle
# shuffle -> tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', 4, 7, 9, 2]

print(cartas)
shuffle(cartas) # modifica a original

print(cartas)
print(cartas.pop())
