"""
#01
matriz1 = [[5, 8, 12, 2], [21, 50, 15, 3], [11, 0, 3, 2], [16, 8, 1, 9]]
contador = 0

for cadamatriz in matriz1:
    for cada in cadamatriz:
        if cada > 10:
            contador += 1


print(f'quantos valores maiores que 10: {contador}')


#02
#https://kharisecario.wordpress.com/2017/03/25/create-nxn-matrix-in-pythonnumpy/


ordem = 5
matriz = []

for i in range(ordem):
    matriz.append([])
for cada in matriz:
    for j in range(ordem):
        cada.append(0)
for c in range(len(matriz)):
    for l in range(len(matriz[c])):
        if c == l:
            matriz[c][l] = 1
        else:
            matriz[c][l] = 0


print(matriz)

#02.1

lista = []
ordem = 5
linha = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    lista.append(linha)

print(lista)

#03
lista = []
ordem = 4
linha = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append((i+1)*(j+1))
    lista.append(linha)

print(lista)


#04
matriz = [[2, 0, 9, 5], [4, 10, 21, 6], [12, 10, 2, 5], [11, 3, 15, 3]]
ref = matriz[0][0]
posicao = []

for i_coluna in range(len(matriz)):
    for i_linha in range(len(matriz[i_coluna])):
        if matriz[i_coluna][i_linha] > ref:
            ref = matriz[i_coluna][i_linha]
            posicao = [i_coluna+1, i_linha+1]

print(f'o maior valor é : {ref}, posição(coluna, linha): {posicao}')


#05
valor = int(input('digite o valor a ser procurado: '))

matriz = [[2, 0, 9, 5, 6], [4, 10, 21, 6, 1], [12, 10, 2, 5, 15], [11, 3, 15, 3, 13], [9, 20, 1, 8, 5]]
ref = valor
posicao = []
contador = 0

for i_coluna in range(len(matriz)):
    for i_linha in range(len(matriz[i_coluna])):
        if matriz[i_coluna][i_linha] == ref:
            contador += 1
            posicao = [i_coluna+1, i_linha+1]

if contador == 0:
    posicao = 'valor não encontrado'

print(f'valor procurado : {ref}, posição(coluna, linha): {posicao}')
print(f'ocorrência: {contador} vezes')









"""



#11















"""







"""