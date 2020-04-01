"""
Dicionarios

chave/valor.   chave e valor podem ser de qualquer tipo de dado.
pode se misturar tipos de dados


"""

# Forma 1: (forma mais comum)

print(type({}))

paises = {'br': 'Brasil', 'il': 'Israel', 'py': 'Paraguai'}

print(paises)
print(type(paises))
print('--------------')

print(paises['br'])
print()

# Forma 2: (menos comum)

paises2 = dict(pt='Portugal', eua='Estados Unidos', fr='França')

print(f'{paises2} || seu tipo: {type(paises2)}')
print('------------------------')

# acessando elementos

pais = {'nome': 'Brasil', 'ufs': 27, 'populacao': 210000000}
print(pais)

     # forma 1 : acessando via chave
print(pais['nome'])
print(pais['ufs'])
print(pais['populacao'])
#print(pais['pib'])   # dá erro
print('------------------------')

     # Forma 2 - Acessando via get - recomendado
print(pais.get('nome'))
print(pais.get('pib'))   # não dá erro

print('------------------------')

localizacao = {'continente': 'america do norte', 'pais': 'México', 'cidade': 'Cidade do México', 'idh': 0.767}

hermosillo = localizacao.get('estado')

if hermosillo:
    print('Encontrei o estado')
else:
    print('Estado não encontrado')

populacao_cidade = localizacao.get('populacao', 'Não encontrado')
idh = localizacao.get('idh', 'Não encontrado')

print(f'Encontrado a populacao {populacao_cidade}')
print(f'Encontrado o idh {idh}')
print('------------------------')


pedido = {'tipo': 'transporte', 'produto': 'bicicleta', 'preco': 400}

print('tipo' in pedido)
print('marca' in pedido)
print('garantia' in pedido)
print('preco' in pedido)
print('bicicleta' in pedido)   # busca chave, mas valor não








