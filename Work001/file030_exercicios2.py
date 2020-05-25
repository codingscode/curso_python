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



"""






#02.1

lista = []  #define empty matrix
ordem = 5
linha = []  #Mistake position

for i in range(ordem):  #total row is 3
    linha = []  #Credits for Hassan Tariq for noticing it missing
    for j in range(ordem):  #total column is 3
        if i == j:
            linha.append(1)  #adding 0 value for each column for this row
        else:
            linha.append(0)
    lista.append(linha)  #add fully defined column into the row

print(lista)





