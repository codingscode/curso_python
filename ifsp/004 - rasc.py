# listas

alunos = ['Jessica', 'Julia', 'Vicente']
notas = [10, 9, 8]
lista_vazia = []

print(alunos)
print(notas)
print(lista_vazia)
print('--------------')

misturado = [True, 8, 'string', ['listadentro', True, 10], 7.8]
print(misturado)
print(misturado[2])
print(misturado[3])
print(misturado[3][0])  # acessando dentro
print(misturado[-4])    # imagine um circulo
misturado[0] = False   # alterando valores
print(misturado)
print('--------------')

misturado.append('mais')  # adiciona no final da lista
print(misturado)
misturado.insert(2, 'posicao escolhida')  # escolhe a posição para adicionar
print(misturado)
print('----------------')

lista = ['uma string', 8, [1, 2], 'era final']
print(lista)
lista.extend(['inserido', 1, 2, 3])
print(lista)
print('----------------')

lista2 = [1, 2, 3]
lista3 = ['mais', 'mais2', 'mais3']
lista4 = lista2 + lista3

print(lista4)
print('----------------')

lista5 = [3, 4, 5]
dobro = lista5*2

print(dobro)
print('----------------')

alunos = ['joao', 'vicente', 'paulo', 'ricardo', 'gabriel', 'vicente','larissa', 'geovana']
print(alunos)
alunos.remove('vicente')
print(f'{alunos}')

alunoretirado1 = alunos.pop()
print(f'{alunos}, retirado: {alunoretirado1}')

alunoretirado2 = alunos.pop(3)
print(f'{alunos}, retirado: {alunoretirado2}')