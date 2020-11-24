"""
Assertions (afirmações/checagem/questionamentos)

Em python utilizamos a palavra reservada assert para realizar simples afirmações utilizadas nos
testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.

Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro
personalizado.
# Obs: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser
exclusivamente nos testes.

obs: cuidado ao usar 'assert'
Se um programa Python for executado com o parametro -O, nenhum assertion será validado. Ou seja,
todas as suas validações já eram.


"""

"""
no terminal assert 4 == 4
            assert 4 == 1
            assert 4 == 1, '4 não é 1'
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


retorno1 = soma_numeros_positivos(2, 4)
print(retorno1)

#retorno2 = soma_numeros_positivos(-3, 8)  # dá erro
#print(retorno2)


def comer_fast_food(comida):
    assert comida in ['pizza', 'sorvete', 'doces', 'batata frita', 'cachorro-quente'], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


print(comer_fast_food('pizza'))
#print(comer_fast_food('laranja'))  # dá erro

print('1------------------')
print('2------------------')
