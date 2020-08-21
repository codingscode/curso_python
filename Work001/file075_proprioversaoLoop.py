"""
Propria versão de Loop

"""

for cada in [2, 3, 4, 5, 6]:
    print(cada)

print('-------------------')

for cada in 'borboleta':
    print(cada)

print('-------------------')

iter([2, 3, 4, 5, 6])


def meu_for(iteravel):
    ite = iter(iteravel)
    while True:
        try:
            print(next(ite))
        except StopIteration:
            break


meu_for('jiboia')
print('-------------')

meu_for([23, 8, 6, 10])
