# 003

palavra = 'Jonas'
palavra2 = 'angelina2'

print(palavra.isalnum())   # letra ou numero
print(palavra.isalpha())   # só letra
print(palavra.isnumeric()) #só numero

print('-------------')
print(palavra2.isalnum())   # letra ou numero
print(palavra2.isalpha())   # só letra
print(palavra2.isnumeric()) #só numero
print('-------------')

frase = 'o dia será bom'
print(len(frase))

numerico = 3
#print(len(numerico)) # dá erro
print('-------------')

print(frase.replace('bom', 'ótimo'))
print('-------------')

aparado = '   tire os espaços das extremidades   '
print(aparado.strip())
print(aparado.rstrip())   # tira da direita
print(aparado.lstrip())   # tira da esquerda
print('-------------')









