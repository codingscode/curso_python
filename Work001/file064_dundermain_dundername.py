"""
Dunder Main e Dunder Name

Dunder -> Double Under


dunder name -> __name__
dunder main -> __main__


em python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

em python, se executarmos um modulo python diretamente na linha de
comando, internamente o python atribuirá a variavel __name__ o valor
__main__ indicando que este modulo é o modulo de execução principal.

"""
"""
dir()
"""

"""
dir()
python file064_dundermain_dundername.py
python
dir()
print(__name__)


"""

from file064_paralelo1 import somar
from file064_paralelo2 import somar2


print(somar(2, 3))  # experimentar executar comentado

print('--------------------')

print(somar2(4, 7))

print('--------------------')

import file064_paralelo3
import file064_paralelo4

"""
dir()
import file064_paralelo3
dir()
file064_paralelo3.__name__

"""
