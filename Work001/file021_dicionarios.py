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

print(f'Encontrado a populacao: {populacao_cidade}')
print(f'Encontrado o idh: {idh}')
print('------------------------')

pedido = {'tipo': 'transporte', 'produto': 'bicicleta', 'preco': 400}

print('tipo' in pedido)
print('marca' in pedido)
print('garantia' in pedido)
print('preco' in pedido)
print('bicicleta' in pedido)   # busca chave, mas valor não

print('------------------------')

""" 
  Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, 
  dicionario, como chaves de dicionarios
"""
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis

localidades = {
   (35.6895, 39.6917): 'Escritorio em Tokio',
   (40.7128, 74.0060): 'Escritorio em Nova Tork',
   (37.7749, 122.4194): 'Escritorio em São Paulo'
}

print(localidades)
print(type(localidades))

print('------------------------')

# adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'marc': 300}
print(f'{receita}, e seu tipo {type(receita)}')

# forma 1
receita['abr'] = 350
print(receita)

# forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)

print(receita)
print('----------------')

# Atualizando dados em um dicionário
    # forma 1
receita['mai'] = 550
print(receita)

    # forma 2
receita.update({'mai': 700})
print(receita)
print('---------------------')

# conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# conclusão 2: Em dicionarios não podemos ter chaves repetidas

# Remover dados de um dicionário
receita2 = {'jan': 100, 'fev': 120, 'marc': 300, 'abr': 134, 'mai': 97, 'jun': 130}
print(receita2)
     # forma 1
ret = receita2.pop('marc')
print(ret)

print(receita2)
#obs1 : Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um keyError é retornado
#obs2 : Ao removermos um objeto, o valor deste objeto é sempre retornado.

    # forma 2
del receita2['mai']
print(receita2)
print('-------------')

#del receita2['mai']  # apagar elemento q não existe dá erro
# obs: neste caso o valor removido nao é retornado

""" 
Carrinho de compras:
    produto1:
        nome; quantidade; preco;
    produto2:
        nome; quantidade; preco;
        

"""

# 1 - Poderiamos utilizar uma Lista para isso? sim
carrinho = []

produto1 = ['play4', 1, 2300]   # nome/quantidade/preco
produto2 = ['god of war', 1, 150]

#carrinho.append(produto1)
#carrinho.append(produto2)   ou apenas o de baixo
carrinho.extend([produto1, produto2])

print(carrinho)

# 2 - Poderíamos utilizar uma tupla? sim
carrinho_2 = ()

produto1_t = ('play4', 1, 2300)
produto2_t = ('god of war', 1, 150)

carrinho_2 = (produto1_t, produto2_t)
print(carrinho_2)

# 3 - Poderíamos utilizar um dicionário? sim
carrinho_3 = []

produto1_d = {'nome': 'play4', 'quantidade': 1, 'preco': 2300}
produto2_d = {'nome': 'god of war 4', 'quantidade': 1, 'preco': 150}

#carrinho_3.append(produto1_d)
#carrinho_3.append(produto2_d) ou apenas
carrinho_3.extend([produto1_d, produto2_d])

print(carrinho_3)
print('-------------------------- \n')

# Métodos de dicionários
#dir({})

dicionario_1 = dict(a=1, b=2, c=3)

print(f'{dicionario_1} || tipo: {type(dicionario_1)}')


  # limpar o dicionario (zerar dados)
dicionario_1.clear()
print(f'dicionario: {dicionario_1}')


  # copiando um dicionario para outro
  # forma 1:

dicionario_2 = {'d': 4, 'e': 5, 'f': 6}
novo_dicionario = dicionario_2.copy()  # deep copy

novo_dicionario['d'] = 10
dicionario_2['g'] = 14

print(f'dicionario_2: {dicionario_2}')
print(f'novo_dicionario: {novo_dicionario}')

  # forma 2:  shallow copy

dicionario_3 = {'k': 10, 't': 2, 'y': 4}
novo_d = dicionario_3

novo_d['x'] = 7

print(f'dicionario_3: {dicionario_3}')
print(f'novo_d:       {novo_d}')

print('--------------------\n')

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(f'{outro} || {type(outro)}')

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'perfil'], 'desconhecido')
print(f'{usuario} || {type(usuario)}')

# obs: o método keysfrom() recebe 2 parametros, um iteravel e outro um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')   # em dicionario não há repetição de chaves
print(veja)

veja2 = {}.fromkeys('abcde', 'valor')
print(veja2)

veja3 = {}.fromkeys(range(1, 7), 'neo')
print(veja3)

