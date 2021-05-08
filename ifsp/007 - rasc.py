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
produto = {'nome': 'bicicleta', 'cor': 'verde', 'preco': 400, 'desconto': True}

print('preco' in produto)
print('marca' in produto)
print('--------------')

#get() acessar valor da chave
print(produto.get('nome'))
print(produto.get('marca'))
print(produto.get('marca', 'não tem'))
print('----------------')

# items(), keys(), values()
print(produto.items())    # par chave/valor
print(produto.keys())     # chaves
print(produto.values())   #valores
print('----------------')

aluno_original = {'nome': 'Raul', 'idade': 20, 'nota': 7.5}
aluno_atualizar = {'peso': 80, 'nota': 9}
aluno_original.update(aluno_atualizar)

print(aluno_original)
print('-------------')





