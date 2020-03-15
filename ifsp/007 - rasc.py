# dicionarios  ou dicts.  {}
# formato : "chave": "valor"

aluno = {'nome': 'Fabiola', 'idade': 23, 'nota': 9, 'cidade': 'campo grande'}
print(aluno)

dic_vazio = {}
print(dic_vazio)

#print(aluno[0])   # dá erro
print(aluno['nome'])
print(aluno['idade'])
#print(aluno['peso'])   # dá erro

print('----------------')

# modificando e acrescentando elementos
aluno['nota'] = 10
aluno['peso'] = 73
del aluno['cidade']

print(aluno)
print(f'o tamanho de aluno é : {len(aluno)}')
print('------------')

#verificando existencia de elementos
produto = {'nome': 'bicicleta', 'cor': 'verde', 'preco': 400}

print('preco' in produto)
print('marca' in produto)

#get()
print(produto.get('nome'))
print(produto.get('marca'))
print(produto.get('marca', 'não tem'))


