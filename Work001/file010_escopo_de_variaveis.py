# Escopo de variaveis

numero = 80  # variavel global
print(f'o nome é numero e o valor é {numero}')

algo = 12  # variavel global
print(f'o tipo de algo primeiro é {type(algo)}')

algo = 'novo tipo'  # variavel global
print(f'o tipo de algo segundo é {type(algo)}')

outro = 8
#novo = 0

if outro > 10:
    novo = outro + 10    # novo é variavel local
    print(novo)            # se outro fosse maior que 10 seria ok

print(novo)
