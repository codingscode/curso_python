"""
Len, Abs, Sum e Round

len -> retorna o tamanho(numero de itens) do iteravel

abs -> retorna o valor absoluto de um número inteiro ou real. desconsidera-se o sinal.

sum() -> recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a
soma total dos elementos, incluindo o valor inicial.
obs: o valor inicial default é 0

round() -> retorna um número arredondado para n digito de precisão após a casa decimal. Se a
precisão não for informada retorna o inteiro mais próximo da entrada.


"""

print(len([14, 4, 9, 2]))
print(len('hoje é...'))
print(len(range(0, 10)))

"""
por baixo dos panos, quando utilizamos a função len() o python faz o seguinte:
"""
print('------------------------------')
# Dunder len
print('Python'.__len__())

print('------------------------------')

print(abs(5))
print(abs(-5))
print(abs(5.76))
print(abs(-11.56))
print(abs(3/5))
print(abs(-7/8))

print('------------------------------')

print(sum([14, 5, 11]))  # também com tupla, set, dicio.values()
print(sum([3, 7, 5], 4))
print(sum([3, 7, 5], -10))
print(sum([4.6, 3.5, 1.9]))
print(sum({'a': 2.3, 'b': 5.5, 'c': 1.2}.values()))

print('------------------------------')

print(round(10.2))
print(round(10.2, 3))
print(round(10.5))
print(round(10.6))
print(round(1.212121, 2))  # 2 casas de precisao
print(round(1.212121))
print(round(3.21999999, 3))
