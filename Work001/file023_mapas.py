"""
Mapas -> conhecidos em python como dicionarios
representação {}



"""

receita = {'jan': 100, 'fev': 250, 'marc': 400}
print(receita)

# Interar sobre dicionarios
for chave in receita:
    print(f'{chave} - {receita[chave]}')

print('-------\n')

print(receita.keys())   # mostra as chaves

for chave in receita.keys():  # modo pythonico
    print(receita[chave])

print('-------\n')

# acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

print('-------\n')

# desempacotamento de dicionarios
print(receita.items())

for chave, valor in receita.items():
    print(f'chave: {chave}, valor: {valor}')

print('-------\n')

# soma, maximo, minimo e tamanho

# *Se os valores forem todos inteiros ou reais

print(f'soma: {sum(receita.values())}')
print(f'maximo: {max(receita.values())}')
print(f'minimo: {min(receita.values())}')
print(f'tamanho: {len(receita)}')
