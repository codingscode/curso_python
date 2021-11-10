
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

"""

Código: 101 
Nome: Fiona Verde 
Data de Nascimento: 1987-09-02 00:00:00 
Cadastro: 2021-11-10
Código: 102 
Nome: Bob aladin 
Data de Nascimento: 1991-03-12 00:00:00 
Cadastro: 2021-11-10
---------------
Número da conta: 1001 
Cliente: Fiona Verde 
Saldo Total: R$ 100.00
Número da conta: 1002 
Cliente: Bob aladin 
Saldo Total: R$ 100.00
-------------------
-------------------

"""
