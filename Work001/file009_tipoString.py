# String

print('Isso é uma string')
nome = 'uma string'
print(nome)
print(f'o tipo de "{nome}" é {type(nome)}')

estabelecimento ="Carla's Restaurante"
print(estabelecimento)

frase = "Em cima \nEm baixo"
print(frase)

duplasdentro = "aspas \" duplas dentro"
print(duplasdentro)

maiuscula, minuscula = 'palavra1', 'PALAVRA2'
print(F'maiuscula é {maiuscula.upper()} e minuscula é {minuscula.lower()}')

frase2 = 'Isto é uma lista de strings'
print(frase2.split())

frase3, frase4, frase5 = 'canguru', "a rua é bonita", "o céu é azul"
print(frase3[0:3])  #slice de string
print(frase4[2])
print(frase4.split()[2]) # pega por parte
print(frase5.split()[3])

print(frase3[::-1]) # inverte
print(frase4[::-1])
print(frase4.replace('rua', 'praça'))
