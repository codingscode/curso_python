# Exceções

print('Inserção de 2 números: ')
numero1 = input('valor do número 1: ')
numero2 = input('valor do número 2: ')  # digite 0 ou letra aqui
resultado = 0.0

try:
    resultado = float(numero1) / float(numero2)
    print(f'o resultado da divisão do 1º pelo 2º # é  : {resultado}')
except ZeroDivisionError:
    print('o 2º número não pode ser 0')
except ValueError:
    print('o valor deve ser número')

print('--------------------')

print('Inserção de 2 números: ')
numero3 = input('valor do número 3: ')
numero4 = input('valor do número 4: ')  # digite 0 ou letra aqui
resultado2 = 0.0

try:
    resultado2 = float(numero3) / float(numero4)
    print(f'o resultado da divisão do 1º pelo 2º # é  : {resultado2}')
except:
    print('uma das entradas é inválida. Insira dois números, sendo o 2º diferente de 0')

# https://docs.python.org/3/library/exceptions.html

print('------------------------')

numero5 = input('valor do número 1: ')
numero6 = input('valor do número 2: ')  # digite 0 ou letra aqui
resultado3 = 0.0

try:
    resultado3 = float(numero5) / float(numero6)
    print(f'o resultado da divisão do 1º pelo 2º # é  : {resultado3}')
except ZeroDivisionError:
    print('o 2º número não pode ser 0')
except ValueError:
    print('o valor deve ser número')
else:  # else só ocorre caso não haja erro
    print('divisão feita.')
finally:  # ocorre independente de erro
    print('ação concluída')

print('----------------------')

tipo_musica = input('qual seu tipo de música: ')

try:
    if tipo_musica == 'funk':
        raise NameError('não gostei disso')
    print(f'{tipo_musica} deve ser legal')
except NameError:
    print('o programa não gostou de seu tipo')











