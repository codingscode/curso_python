# pasta 4


"""


#01
numero = int(input('Digite um número inteiro : '))
print(f'o número é {numero}')

#02
numero = float(input('Digite um numero: '))
print(numero)


#03
vezes = 3
soma = 0

for n in range(1, vezes + 1):
   numero = int(input(f'Digite o {n}º de {vezes} valor: '))
   soma += numero
print(f'A soma deles é {soma}')

#04
numero = float(input('Digite o numero: '))
quadrado = pow(numero, 2)
print(f'o quadrado de {numero} é {quadrado}')


#05
numero = float(input('digite um número: '))
print(f'a quinta parte dele é {numero/5}')

#10
velocidade = float(input('digite a velocidade em km/h : '))
print(f'a velocidade em m/s é : {velocidade/3.6}')


#12.....


#28
vezes = 3
soma = 0

for n in range(1, vezes + 1):
    numero = float(input(f'digite o número {n} de {vezes}: '))
    soma += pow(numero, 2)

print(f'a soma dos quadrados é {soma}')


#29
vezes = 4
soma = 0
for n in range(1, vezes+1):
    nota = float(input(f'digite a {n}ª nota : '))
    soma += nota

print(f'a média é {soma/vezes}')


#45
frase = input('digite uma frase ou uma palavra: ')

for n in range(0, len(frase)):
    if (frase[n].isupper()):
        print(frase[n].lower())
    else:
        print(frase[n])


#46

numero = int(input('Digite um número de 3 dígitos: '))

if (isinstance(numero, int)):
    conv = str(numero)
    print(f"quantidade de digitos {len(conv)}")
    if len(conv) == 3:
        print(conv[::-1])
    else:
        print('o número não tem 3 dígitos')
else:
    print("não é número")

#47
numero = input('Digite um número de 4 dígitos: ')

if (len(str(numero))) != 4:
    print('o numero n tem 4 digitos')
elif (int(numero) >= 100 and int(numero)<= 9999) is False:
    print('fora do intervalo')
else:
    for n in range(0, len(numero)):
        print(numero[n])

#51
x = float(input('digite o valor de x : '))
y = float(input('digite o valor de y : '))

distancia = ((x)**2 + (y)**2)**0.5
print(f'a distancia até a origem (0, 0) é : {distancia}')

#52

premio = float(input('Qual o valor do premio ? : '))

jogador1 = float(input('Valor dado pelo jogador1: '))
jogador2 = float(input('Valor dado pelo jogador2: '))
jogador3 = float(input('Valor dado pelo jogador3: '))

k = jogador1 + jogador2 + jogador3

print(f'jogador1 ganha : {(jogador1/k)*premio}, jogador2 ganha : {(jogador2/k)*premio}, jogador3 ganha : {(jogador3/k)*premio}')

#53
print('dimensões do terreno:')
comprimento = float(input('Qual o comprimento(m) do terreno : '))
largura = float(input('Qual a largura(m) do terreno : '))
preco = float(input('preco por m²: '))

custotoal = comprimento*largura*preco
print(custotoal)

"""
