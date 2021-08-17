"""
Testes de velocidade com expressões geradoras

"""


def nums():
    for num in range(1, 10):
        yield num


gen1 = nums()

print(gen1)  # generator
print(next(gen1))
print(next(gen1))

print('---------------')

# Generator Expression
gen2 = (num for num in range(1, 8))

print(gen2)   # generator expression
print(next(gen2))
print(next(gen2))

print('---------------')

print(sum(cada for cada in range(3, 8)))

print('---------------')
import time
# realizando o teste de velocidade

# generator expression
gen_inicio = time.time()
print(sum(cada for cada in range(1, 6000000)))
gen_tempo = time.time() - gen_inicio

# list comprehension
list_inicio = time.time()
print(sum([cada for cada in range(1, 6000000)]))
list_tempo = time.time() - list_inicio

print(f'generator expression: {gen_tempo}')
print(f'list comprehension:   {list_tempo}')

print('---------------')
