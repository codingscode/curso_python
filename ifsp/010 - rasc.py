# funcções

def imprimir_saudacao():
  print('Olá')

imprimir_saudacao()   # chama

print('-----------------')

def cubo(numero):
    val_retornar = numero**3
    return(val_retornar)

mostrar = cubo(2)
print(mostrar)

print('-----------------')

def raiza_quadrada(valor):
    retornar = valor**0.5
    return retornar

mostrar2 = raiza_quadrada(16)
print(mostrar2)

print('-----------------')

def mais_um(valor=7):
   retornar = valor + 1
   return  retornar

mostrar3 = mais_um()
print(mostrar3)

print('-----------------')

def mostrar_dados(nome, idade):
    print(f'Olá meu nome é {nome} e tenho {idade} anos')

mostrar_dados(idade=20, nome='samuel')  # ou 'samuel', 20

print('-----------------')

# args e kwargs não são palavras reservadas, são de livre nomeação


def mostrar_argumentos(*args):   # como listas
    for parametro in args:
        print(parametro)


mostrar_argumentos('Olá', 'Python', 'ok')

print('-----------------')


def mostrar_dado(**kwargs):    # como dicionarios
    for parametro, valor in kwargs.items():
        print(f'{parametro} - {str(valor)}')


mostrar_dado(nome='simon', idade=18, nacionalidade='brasil')

print('-----------------')


def mostrar_dados2(nome, idade, **kwargs):
    print('Nome: ' + nome)
    print('Idade: ' + str(idade))

    print('\nInformações adicionais:')
    for parametro, valor in kwargs.items():
        print(f'{parametro} - {str(valor)}')


mostrar_dados2(nome='simon', idade=30, nacionalidade='uruguai', telefone='88888888')

print('-----------------')








