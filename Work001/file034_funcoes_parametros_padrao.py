"""
Funções com parametro Padrão

Funções onde a passagem de parametros seja opcional;


"""
# exemplo 1

print('Codando em Python')
print()   # sem passar
print('-------------------')


def exponencial(numero, expoente=2):
    return numero**expoente


print(exponencial(4, 3))
print(exponencial(5))  # já informado antes
print('-----------------------')

# OBS: Em funções Python, os parametros com valores default(padrão) devem sempre estar ao final da
# declaração


def mostrar_informacao(nome='CodePython', instrutor=False):
    if nome == 'CodePython' and instrutor:
        return 'Bem vindo instrutor CodePython'
    elif nome == 'CodePython':
        return 'Achava q era o instrutor'
    return f'olá {nome}'


print(mostrar_informacao())
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao('Jerry'))
print('---------------------')

# exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 3, subtracao))

print('-------------------\n')

# Evitar problemas e confusões...
# variaveis globais
# variaveis locais

instrutor = 'Geek'  # v global


def diz_oi():
    ling = 'Python'  # v local
    return f'Oi {instrutor}, estudando {ling}'


print(diz_oi())
#print(ling)   # dá erro
print('--------------')


total = 0


def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
print('--------------')

# Podemos ter funções que são declaradas dentro de funções, e também uma forma especial de
# escopo de variavel


def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
#print(dentro())  # dá erro
