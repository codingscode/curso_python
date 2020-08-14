"""
Geradores(Generators) são iterators

obs: o contrário não é verdadeiro. Ou seja, nem todo iterator é um generator


Outras informações:
- generators podem ser criados com funções geradoras;
- funções geradoras utilizam palavra reservada yield;
- generators podem ser criados com expressoes geradoras;

Diferenças entre funções e generator functions (funções geradoras):
funções:
-> utilizam return
-> retorna uma vez
-> quando executada, retorna um valor


funções geradoras:
-> utilizam yield
-> podem utilizar yield multiplas vezes
-> quanto executada, retorna um generator



"""
# exemplo generator function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

#obs: uma generator function não é um generator. ela gera um generator

gen = conta_ate(5)

#print(type(gen))  # <class 'generator'>
print(next(gen))
print(next(gen))
print(next(gen))  # assim até passar do limite dá StopIteration

print('-----------------')

gen2 = conta_ate(10)

for cada in gen2:
    print(cada)

print('-----------------')

gen3 = conta_ate(7)

print('por fora', next(gen3))

for cada2 in gen3:
    print(cada2)

print('-----------------------------')

gen4 = list(conta_ate(4))

print(gen4)

print('-----------------------------')


