"""
algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
- unidimensionais (arrays/vetores), - multidimensionais(matrizes ou listas aninhadas)


"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
print(type(listas))
print(listas[1])
print(listas[2][1])
print(listas[0][2])
print(listas[2])
print(listas[-1])
print(listas[-2][-1])
print('----------------------------------')

# Iterando com loops em uma lista aninhada
for el_linha in listas:
    for el_coluna in el_linha:
        print(el_coluna)

print('------------------------------')

# Iterando com list comprehension

[[print(el) for el in linha] for linha in listas]

print('------------------------------')

#gerando um tabuleiro/matriz

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 5)] # [[0 for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha
velha = [['x' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 3)])
