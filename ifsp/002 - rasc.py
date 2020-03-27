# 002

nome = 'Felipe'
idade = 30
print("Meu nome é %s e tenho %d anos" % (nome, idade))

nom2 = 'Gabriel'
print('Olá meu nome é : ' + nom2)

nome3 = 'Ana'
idade = 19

print('Olá meu nome é : ' + nome3 + " e idade é " + str(idade))

umastring = 'hoje é dia de sol'

print(umastring[0])
print(umastring[2])
print(umastring[5])
print(umastring[8])
print(umastring[11])
print('--------------')

nome4 = 'israel'
frase1 = 'FICA TUDO MINUSCULO'
frase2 = 'fica tudo maiusculo'

print(f'{nome4.capitalize()}, {frase1.lower()}, {frase2.upper()}')

umastring2 = 'amanhã é sol'
print(umastring2.center(20, '*'))  # center(nº caracteres, o que nas extremidades)

frase3 = 'hoje o dia foi bom'
frase4 = 'amanhã será melhor ainda'

substringfrase3 = 'bom'
substringfrase4 = 'pior'

print(frase3.find(substringfrase3, 5))  # se v, retorna a posição
print(frase4.find(substringfrase4, 4))  # se f, retorna -1


