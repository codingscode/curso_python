"""
try / except / else / finally


Dica de quando e onde tratar codigo:
Toda entrada deve ser tratada !

obs: a função do usuario é destruir seu sistema.
else -> é executado somente se não ocorrer o erro.


"""
num = 0

try:
    num = float(input('digite um número: '))
except ValueError:
    print(f'valor incorreto  | tipo: {type(num)}')
else:
    print(f'vc digitou {num}')













