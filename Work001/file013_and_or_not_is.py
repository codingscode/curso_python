# Estruturas lógicas : And, Or, Not e Is

ativo = True
logado = False

if ativo:
    print('Usuário ativo')

if ativo and logado:
    print('Usuário bem vindo')
else:
    print('Ative sua conta')

ir = 'onibus'

if ir == 'onibus' or 'carro':
    print('tudo bem')

situacao = 'favoravel'
if not situacao == 'favoravel':
    print('precisa melhorar')
else:
    print('que bom!')

print(not True)

cartaoVerificado = True
if cartaoVerificado is True:
    print('cartão verificado')

print(cartaoVerificado is False)

nome = 'Arvore'
print(nome.isupper())
print(f'nome começa com maiuscula {nome.istitle()}')




