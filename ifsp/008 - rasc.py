# Sets
# Os sets são listas ou coleções não ordenadas de itens únicos.
# retorna itens excluindo repetições

nomes1 = ['tony', 'vicente', 'tony', 'allan', 'dmitry', 'angela', 'vicente', 'angela']
set1 = set(nomes1)
print(set1)

set2 = {'chipanzé', 'gato', 'cachorro', 'chipanzé', 'pardal', 'cachorro', 'chipanzé', 'beija-flor'}
print(set2)
print('---------------')

#transformando string em set
paraset = set('cachorro')
paraset2 = set('Piauí')

print(paraset)
print(paraset2)
print('---------------')

# removendo elementos de um set
esteset = {'celta', 'uno', 'gol', 'palio', 'golf', 'pampa', 'palio'}
print(esteset)

esteset.remove('gol')
print(esteset)
print('--------------------')

maissets = {'curitiba', 'cuiaba', 'porto alegre', 'florianopolis', 'cuiaba', 'florianopolis'}
print(maissets)
print(f'tamanho é {len(maissets)}')
print('maceio' in maissets)
print('----------------')

conjunto1 = {'vicente', 'fabiola', 'ana', 'leticia', 'samuel', 'mario', 'clarice', 'angela'}
conjunto2 = {'samuel', 'leticia', 'fabiola', 'israel', 'gabriel', 'daniel', 'ziraldo'}

print(f'o que só tem no conjunto1 : {conjunto1.difference(conjunto2)}')
print(f'comum entre conjunto1 e conjunto2 : {conjunto1.intersection(conjunto2)}')
# print(f'comum entre conjunto1 e conjunto2 : {conjunto2.intersection(conjunto1)}') # o mesmo de cima

print(f'o que só tem no conjunto2 : {conjunto2.difference(conjunto1)}')
print('--------------------')

set3 = {1, 3, 5, 8}
print(set3)
set4 = set3
set5 = set3.copy()

set3 = {10, 20, 15, -4}
print(set3)
print(set4)
print(set5)

print('-------------------')







