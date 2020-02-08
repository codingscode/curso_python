"""
Loop e For
"""

nome = "Madagascar é uma ilha"
lista = [3, 4, 5, 6]
numeros = range(1, 10)   #é preciso transformar em lista

#exemplo1 para for (iterando em uma string)
for letra in nome:
    print(letra)

print('   ')
#exemplo2 para for (iterando sobre uma lista)
for numero in lista:
    print(numero)

print('------')
#exemplo3 para for (iterand sobre uma range)
for numero in range(1, 10):          #valor final n inclui
    print(numero)

#Enumerate
print(' com enumerate ')
for indice, letra in enumerate(nome):
    print(nome[indice])

print('---------')
frase = 'A rua bonita'
for indice, letra in enumerate(frase):
    print(letra)

print('---------')
saldacao = 'Olá'
for _, letra in enumerate(saldacao):
    print(letra)

print('------')
for valor in enumerate(frase):
    print(valor)

print('------')
for valor in enumerate(frase):
    print(valor[0])

print('------')
for valor in enumerate(frase):
    print(valor[1])

print('-------')
quant = int(input('Quantas vezes esse loop deve rodar ?: '))
for n in range(1, quant+1):
    print(f'Imprimindo {n}')

print('-------')
quantidade = int(input('Quantas vezes esse loop deve rodar ?: '))
soma = 0
for n in range(1, quantidade + 1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma += num
print(f'A soma é {soma}')

print('--------')
quoting = 'a praia é bonita'
for letra in quoting:
    print(letra, end='')  # em uma linha só

print('------')
palavra1 = 'bentivi'
print(palavra1*3)

print('---------')
#tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# U+1F606 para U0001F606, + é 000
for _ in range(1, 4):
    for num in range(1, 11):
        print('\U0001F606'*num)




