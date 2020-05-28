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
print('--------------------')























