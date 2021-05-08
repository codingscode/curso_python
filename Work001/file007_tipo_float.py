
#errado
valor = 1, 44
print(f'valor é {valor} e seu tipo é {type(valor)}')

#certo
valor = 1.44
print(f'valor é {valor} e seu tipo é {type(valor)}')

#É possível
valor1, valor2 = 2, 3
print(f'valor1 é {valor1} e valor2 é {valor2}')
print(f'tipo de valor1 é {type(valor1)} e tipo de valor2 é {type(valor2)}')

#Converter float para int
valor3 = 2.6
print(f'valor3 convertido é {int(valor3)} e o novo tipo fica {type(int(valor3))}')

#Podemos trabalhar com números complexos
numcomplex = 3j
print(f'numcomplex é {numcomplex} e seu tipo é {type(numcomplex)}')

numcomplex1 = 5j
print(f'numcomplex1 ao quadrado é {numcomplex1**2}, novo tipo é {type(numcomplex1**2)}')

#Converter int para float
valor4 = 500
print(f'valor4 em float é {float(valor4)}')
