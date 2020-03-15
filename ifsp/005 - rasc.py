# continuação

alunos = ['joao', 'vicente', 'paulo', 'ricardo', 'gabriel', 'vicente','larissa', 'geovana', 'fabiola']
print(alunos)

#slicing
print(alunos[1:6])  # do indice 1 a ?-1
print(alunos[3:7])
print(alunos[:4])   # 0 a ?-1
print(alunos[4:])   # 4 ao final
print(alunos[1:-1])
print(alunos[2:-2])

print('------------------')

numeros = [8, -3, 20, 49, 83, 16, 54, -1, 5]
print(f'comprimento é : {len(numeros)}')

print(f'o maior é : {max(numeros)}')
print(f'o menor é : {min(numeros)}')

outrosalunos = ['samuel', 'patrick', 'mario', 'leticia', 'jordana']
copiaautonoma = outrosalunos.copy()
copianaoautonoma = outrosalunos

outrosalunos.append('elise')

print(copiaautonoma)
print(copianaoautonoma)

print('--------------------')

alunos2 = ['samuel', 'mario', 'patrick', 'mario', 'leticia', 'jordana', 'mario', 'leticia']
qmario = alunos2.count('mario')
qleticia = alunos2.count('leticia')
qluigi = alunos2.count('luigi')

print(f'quantas vezes aparece mario : {qmario}')
print(f'quantas vezes aparece leticia : {qleticia}')
print(f'quantas vezes aparece luigi : {qluigi}')

print('------------')

alunos3 = ['vicente', 'fabiola', 'adina', 'ziraldo', 'mauricio', 'leonardo']
alunos3.sort()

print(alunos3)
alunos3 = ['vicente', 'fabiola', 'adina', 'ziraldo', 'mauricio', 'leonardo']  #sobrescrevendo

alunos3.reverse()
print(alunos3)
print(alunos3.reverse())

print('-----------------')

# constatar presença de item com 'in'
transportes = ['bicicleta', 'moto', 'carro', 'avião', 'metrô']

print('patinete' in transportes)

# join ;split transforma string em lista
cor = 'vermelho'
cor2 = 'violeta'
cor3 = 'laranja'
cor4 = 'vermelho, azul, roxo, verde, laranja'
cor5 = 'laranja'

cor_asterisco = '**'.join(cor)   # criterio entre elementos
print(cor_asterisco)

cor_espacotriplo = '   '.join(cor2)
print(cor_espacotriplo)

cor_semcriterio = cor3.split()  # nenhum criterio para separar
print(cor_semcriterio)

cor_virgula = cor4.split(',')
print(cor_virgula)

cor_criterio_a = cor5.split('a')
print(cor_criterio_a)

print('-----------')

