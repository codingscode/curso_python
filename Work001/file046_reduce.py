"""
Reduce

Obs: já foi função integrada. A partir do Python3+ a função reduce() não é mais uma função
integrada (built-in)
Agora temos que importar e utilizar esta função a partir do modulo functools.

reduce() -> recebe dois parametros (função e iterável)
age de par em par, e guarda o resultado e compara com o elemento seguinte

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

"""
from functools import reduce

# multiplicando elementos
lista = [2, 10, 7, 10, 0.01]

# a função que fica dentro de reduce() usa recebe 2 parametros
multiplicar = lambda x, y: x*y  # dois parametros obrigatoriamente

resultado = reduce(multiplicar, lista)

print(resultado)
print('-------------------')

# Usando um loop normal
res = 1

for cada in lista:
    res *= cada

print(res)
