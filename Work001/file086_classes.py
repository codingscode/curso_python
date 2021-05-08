"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos projetos do mundo real sendo representados computacionalmente.
Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
- Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos
representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos
querer saber se a lampada é 110 ou 220 V, se ela é branca, amarela, verde ou outra cor, qual é a
luminosidade dela e etc.

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
 realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito
 provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar a mesma.

obs: quando nomeamos nossas classes em python utilizamos por convenção o nome com inicial em maiusculo.
 Se o nome for composto usa-se camelcase todas juntas

- classes internas do python começam com letra minuscula
obs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos estes objetos que serão mapeados para classes de entidade.

"""

idade = 23
preco = 1200.95
nome = 'moto_bis'

print(type(idade))
print(type(preco))
print(type(nome))

print('-------------------1')
# tipo criado


class Lampada:
    pass


class ContaPoupanca:  # Conta_Poupanca não
    pass


lamp = Lampada()

print(type(lamp))

valor = int('12')  # cast

print('-------------------2')

print(help(int))  # int é classe

print('--------------------')
print('--------------------')
