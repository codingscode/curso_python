"""
Exercicios POO

"""

"""



# 01)

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir(self):
        return f'nome: {self.__nome}, idade: {self.__idade}, altura: {self.__altura}'

    def setar_nome(self, valor_nome):
        self.__nome = valor_nome

    def setar_idade(self, valor_idade):
        self.__idade = valor_idade

    def setar_altura(self, valor_altura):
        self.__altura = valor_altura


pessoa1 = Pessoa('Paulo', 21, 1.85)

print(pessoa1.__dict__)
print(pessoa1._Pessoa__nome)
print(pessoa1._Pessoa__idade)
print(pessoa1._Pessoa__altura)

pessoa1.setar_nome('Samuel')
pessoa1.setar_idade(32)
pessoa1.setar_altura(1.78)
print(pessoa1.__dict__)

# 02)


class Agenda:
    id = 0
    pessoa = dict()

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__pessoaatual = Agenda.pessoa
        self.__lista = []
        Agenda.pessoa = dict()

    def armazenar_pessoa(self, nome, idade, altura):
        colocar_pessoa = {'id': Agenda.id, 'nome': nome, 'idade': idade, 'altura': altura}
        self.__lista.append(colocar_pessoa)
        Agenda.id += 1

    def remover_pessoa(self, nome):
        todos = self.__lista

        nova_lista = list(filter(lambda cada: cada['nome'] is not nome, todos))
        self.__lista = nova_lista
        return nova_lista

    def buscar_pessoa(self, nome):
        todos = self.__lista
        pessoa_procurada = list(filter(lambda cada: cada['nome'] is nome, todos))
        return f'{pessoa_procurada[0]} | posição: {pessoa_procurada[0]["id"] + 1}'

    def imprimir_agenda(self):
        return self.__lista

    def imprir_pessoa(self, indice):
        todos = self.__lista
        pessoa_indice = list(filter(lambda cada: cada['id'] is indice, todos))
        return pessoa_indice


# adicionando pessoas
agenda1 = Agenda('silas', 21, 1.7)
agenda1.armazenar_pessoa('donatello', 33, 1.9)
agenda1.armazenar_pessoa('bob', 17, 1.73)
agenda1.armazenar_pessoa('lucia', 25, 1.8)
agenda1.armazenar_pessoa('aladin', 16, 1.6)
agenda1.armazenar_pessoa('jessy', 22, 1.71)
agenda1.armazenar_pessoa('dennis', 12, 1.4)
agenda1.armazenar_pessoa('dino', 26, 1.85)
agenda1.armazenar_pessoa('fabian', 23, 1.78)

# mostrando todos
#print(agenda1.imprimir_agenda())
[print(cada) for cada in agenda1.imprimir_agenda()]
print(len(agenda1.imprimir_agenda()))
print('1------------------------------')

# removendo uma pessoa
print(agenda1.remover_pessoa('jessy'))
#print(agenda1.imprimir_agenda())
[print(cada) for cada in agenda1.imprimir_agenda()]
print(len(agenda1.imprimir_agenda()))
print('2------------------------------')

# buscando pessoa pelo nome
print(agenda1.buscar_pessoa('lucia'))

print('3------------------------------')
# imprimir pessoa pela posição

print(agenda1.imprir_pessoa(6))

print('4------------------------------')


# 03)


class Elevador:

    def __init__(self, andar_atual, total_andares, capacidade_elev, quant_pessoas):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade_elev = capacidade_elev
        self.__quant_pessoas = quant_pessoas

    def inicializa(self, capacidade_elevador, total_andares):
        self.__andar_atual = 0
        self.__quant_pessoas = 0
        self.__capacidade_elev = capacidade_elevador
        self.__total_andares = total_andares

    def entra(self, adicionar_pessoas):
        if self.__quant_pessoas + adicionar_pessoas > self.__capacidade_elev:
            self.__quant_pessoas = self.__capacidade_elev
            print('Não é possível acrescentar mais pessoas')
        else:
            self.__quant_pessoas += adicionar_pessoas

    def sai(self, retirar_pessoas):
        if self.__quant_pessoas > 0:
            if self.__quant_pessoas >= retirar_pessoas:
                self.__quant_pessoas -= retirar_pessoas
            else:
                self.__quant_pessoas = 0
                print('Quantidade a ser retirada maior que a quantidade de pessoas presentes')
        else:
            print('Não há pessoas no elevador')

    def sobe(self, n_andares_subir):
        if self.__andar_atual + n_andares_subir > self.__total_andares:
            self.__andar_atual = self.__total_andares
            print('Não é possível subir além do limite')
        else:
            self.__andar_atual += n_andares_subir

    def desce(self, n_andares_descer):
        if self.__andar_atual - n_andares_descer < 0:
            print('Não é possível descer abaixo do térreo')
            self.__andar_atual = 0
        else:
            self.__andar_atual -= n_andares_descer


elevador1 = Elevador(1, 12, 8, 3)  # andar_atual, total_andares, capacidade_elev, quant_pessoas

print(elevador1.__dict__)

print('1----------------------------------\n')
elevador1.inicializa(10, 15)
print(elevador1.__dict__)

print('2----------------------------------\n')
elevador1.entra(7)
print(elevador1.__dict__)
elevador1.entra(4)
print(elevador1.__dict__)

print('3----------------------------------\n')
elevador1.sobe(12)
print(elevador1.__dict__)
elevador1.sobe(4)
print(elevador1.__dict__)

print('4----------------------------------\n')
elevador1.sai(6)
print(elevador1.__dict__)
elevador1.sai(5)
print(elevador1.__dict__)

print('5----------------------------------\n')
elevador1.desce(8)
print(elevador1.__dict__)
elevador1.desce(9)
print(elevador1.__dict__)

print('6----------------------------------\n')

"""
# 04)


class ControleRemoto:
    botoes = ['ch+', 'ch-', 'vol+', 'vol-']

    def __init__(self, botao):
        self.__botao_pressionado = botao

    def emitir(self, valor):
        self.__botao_pressionado = valor
        return self.__botao_pressionado


class Televisao:

    def __init__(self, volume_atual=0, canal_atual=1):
        self.__volume_atual = volume_atual
        self.__canal_atual = canal_atual

    def receber_sinal(self, valor):
        if type(valor) == type('x'):
            if valor == 'ch+':
                if self.__canal_atual >= 190:
                    self.__canal_atual = 190
                else:
                    self.__canal_atual += 1
            elif valor == 'ch-':
                if self.__canal_atual <= 1:
                    self.__canal_atual = 1
            elif valor == 'vol+':
                if self.__volume_atual < 20:
                    self.__volume_atual += 1
                else:
                    self.__volume_atual = 20
            elif valor == 'vol-':
                if self.__volume_atual == 0:
                    self.__volume_atual = 0
                else:
                    self.__volume_atual -= 1
            else:
                print('valor pressionado inexistente')
        elif type(valor) == type(1):
            if 0 < valor <= 190:
                self.__canal_atual = valor
            else:
                print('valor pressionado fora do limite')


controle1 = ControleRemoto(3)

print(controle1.__dict__)
print(controle1._ControleRemoto__botao_pressionado)
# print(controle1.__botao_pressionado)

aparelho = Televisao()

controle1._ControleRemoto__botao_pressionado = 'ch+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
controle1._ControleRemoto__botao_pressionado = 'ch+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
controle1._ControleRemoto__botao_pressionado = 'ch+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
controle1._ControleRemoto__botao_pressionado = 'vol+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
print(aparelho.__dict__)

print('1----------------------')
controle1._ControleRemoto__botao_pressionado = 'vol+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
controle1._ControleRemoto__botao_pressionado = 'vol+'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
print(aparelho.__dict__)

print('2-----------------------')
controle1._ControleRemoto__botao_pressionado = 21
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
print(aparelho.__dict__)

print('3-----------------------')
controle1._ControleRemoto__botao_pressionado = 'oi'
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
print(aparelho.__dict__)

print('4-----------------------')
controle1._ControleRemoto__botao_pressionado = 501
aparelho.receber_sinal(controle1._ControleRemoto__botao_pressionado)
print(aparelho.__dict__)


print('-----------------------')
print('-----------------------')

"""
"""