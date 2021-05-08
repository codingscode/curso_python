"""
Funções com parametros:
- recebem dados para serem processados dentro da mesma.
entrada -> processamento -> saída




"""

# refatorando uma função

def quadrado(num):
    return num**2


print(quadrado(3))
print(quadrado(5))
print(quadrado(7))

print('-------------------')


def frase(nome, local):
    return f'{nome} mora em {local}.'


print(frase('simon', 'campo grande'))

"""
funções podem ter 'n' parametros de entrada

"""


def repete(a, b, msg):
    return (a + b) * msg


print(repete(2, 3, 'repete '))
print(repete(1, 2, 'python '))

print('------------------')
# Nomeando parametros


def nometodo(nome, sobrenome):
    return f'Seu nome é : {nome} {sobrenome}'


print(nometodo('Vicente', 'di Paolo'))

# diferença entre parametros e argumentos
"""
Parametros são variaveis declaradas na definição de uma função;
Argumentos são dados passados durante a execução de uma função;
a ordem dos parametros importa 
"""

# argumentos nomeados (keyword arguments)

"""
caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos utilizar 
qualquer ordem.



"""
nome = 'Bob'
sobrenome = 'Simpson'

print(nometodo(nome='Kyle', sobrenome='Adams'))
print(nometodo(nome=nome, sobrenome=sobrenome))
print(nometodo(sobrenome='Smith', nome='Jimmy'))

print('-------------------------------')
# erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total = total + numero
            #return total erro
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))










