"""
Sintaxe:
{chave:valor for valor in iteravel}






"""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(numeros)

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros_lista = [3, 4, 5, 6, 7, 4]  #  funciona também com tupla e conjuntos
quadrado2 = {valor: valor**2 for valor in numeros_lista}  #  não aceita repetição

print(quadrado2)

print('----------------------------------')

chaves = 'abcde'
valores = [3, 11, 4, 21, 6]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# exemplos com lógica condicional
res = {num: ('par' if num % 2 == 0 else 'impar') for num in valores}
print(res)