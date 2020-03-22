# estruturas de controle
# if, else, elif

resposta = input('Digite qualquer coisa : ')

if resposta != '':
    print(f'Olá sua resposta é : {resposta}')

print('----------')

resposta2 = input('Seu nome é fulano ? (s/n) ')

if resposta2 == 's':
    print('Olá fulano')
else:
    print('Olá, visitante')

print('----------')

resposta2 = input('Sua idade é maior de 18 anos (s/n) ? ')

if resposta2 == 's':
    print('vc é adulto')
elif resposta2 =='n':
    print('vc é menor de idade')
else:
    print('resposta inválida')

print('------------')

# for
frutas = ['jaca', 'goiaba', 'laranja', 'melancia', 'graviola', 'abacate']

for elemento in frutas:
    print({elemento})

print('---------------')
# iterando chaves e valores

aluno1 = {'nome': 'fabiola', 'idade': 19, 'peso': 70, 'sexo': 'f'}

for chave in aluno1:
    print(f'chave: {chave}')

print('---------------')

for chave in aluno1.keys():
    print(f'chave: {chave}')

print('------------------')

for valor in aluno1.values():
    print(f'valor : {valor}')

print('------------------')

for chave, valor in aluno1.items():
    print(f'chave: {chave}, valor: {valor}')

print('------------------')


print('range com um parametro:')
for i in range(8):  # 0 a ?-1
    print(i)

print('------------------')

print('range com dois parametros')
for i in range(4, 10):  # 4 a ?-1
    print(i)

print('------------------')

carros1 = ['celta', 'pampa', 'strada', 'corsa', 'uno', 'mercedez', 'fusca', 'gol']

for i in range(len(carros1)):
    print(carros1[i])

print('------------------')

print('exemplo com break:')
for i in range(3, 10):
    if i == 8:
        break
    print(i)

print('exemplo com continue:')
for i in range(3, 10):
    if i == 8:
        continue
    print(i)

print('------------------')

# usando while
contador = 0

while contador < 5:
    print(f'contador = {contador}')
    contador += 1

print('------------------')
while True:
    resposta = input('digite algo ou "sair" : ')
    if resposta == 'sair':
        break
    else:
        print(f'resposta -> {resposta}')

print('------------------')







