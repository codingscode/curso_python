"""
List Comprehension

Usando a podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension
[dado for dado in iteravel]





"""

numeros = [3, 7, 2, 50]

res = [cada*10 for cada in numeros]
print(res)


def divisivelp2(valor):
    return valor % 2 == 0


res2 = [divisivelp2(cada) for cada in numeros]
print(res2)
print('--------------------')

# list comprehension x loop
numeros_dobrados = []

for cada in numeros:
    numeros_dobrados.append(cada*2)

print(numeros_dobrados)

print([cada*2 for cada in numeros])
print('--------------------')

nome = 'Curso Python'
print([letra.upper() for letra in nome])


def caixa_alta(valor):
    return valor.replace(valor[2], valor[2].upper())


amigos = ['vicente', 'larissa', 'rafaela', 'simon']
transportes = ['bicicleta', 'onibus', 'carro', 'aviao', 'navio']
print([amigo[0].upper() for amigo in amigos])
print([amigo.title() for amigo in amigos])
print([caixa_alta(amigo) for amigo in amigos])
print([caixa_alta(cada) for cada in transportes])

print('----------------------------')

print([indice*3 for indice in range(1, 6)])

print([bool(cada) for cada in [0, [], '', True, 1, 3.14]])

print([str(cada) for cada in [2, 3, 4, 5]])

print('----------------------------------\n parte 2\n')

"""
Podemos adicionar estruturas condicionais lógicas às nossas list comprehension

"""

numeros2 = [3, 7, 42, 21, 12, 15, 30]
print(numeros2)

pares = [cada for cada in numeros2 if cada % 2 == 0]
print('pares:', pares)
print('pares:', [cada for cada in numeros2 if not cada % 2])  # 0 é False
print('impares:', [cada for cada in numeros2 if cada % 2])  # numero positivo é True

print('------------------------')

res3 = [cada*2 if cada % 2 == 0 else cada/2 for cada in numeros2]
print(res3)




























