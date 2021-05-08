from file135_models.cliente import Cliente
from file135_models.conta import Conta


fiona: Cliente = Cliente('Fiona Verde', 'fionaspantanis@gmail.com', '123.456.789-01', '02/09/1987')
bob: Cliente = Cliente('Bob aladin', 'bob@gmail.com', '751.456.789-01', '12/03/1991')

print(fiona)
print(bob)
print('---------------')


contaf: Conta = Conta(fiona)
contaa: Conta = Conta(bob)

print(contaf)
print(contaa)
print('-------------------')
print('-------------------')








