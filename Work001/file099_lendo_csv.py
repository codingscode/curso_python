"""
Lendo arquivos csv

CSV - comma separated values - valores separados por virgula

ex:
1, 2, 3, 4, 5
'a', 'b', 'c', 'd', 'e'
obs: o separador também pode ser ';', espaço

http://dados.gov.br/dataset

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
  - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas.
  - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts.

"""

# Possível de se trabalhar, mas não é o ideal (trabalhoso)
with open('file099_lutadores.csv', encoding='utf-8') as arquivo1:
    dados = arquivo1.read()
    #print(type(dados))
    dados = dados.split(',')[2:]  # a partir do 2
    #dados = dados.split('\n')[1:]
    print(dados)

print('1---------------------')
# Reader

from csv import reader

with open('file099_lutadores.csv', encoding='utf-8') as arquivo2:
    leitor_csv = reader(arquivo2)
    #print(list(leitor_csv))
    print(type(leitor_csv))
    next(leitor_csv)  # pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centimetros')

print('2---------------------')
# DictReader

from csv import DictReader

with open('file099_lutadores.csv', encoding='utf-8') as arquivo3:
    leitor_csv = DictReader(arquivo3)
    # print(list(leitor_csv))
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura']}")

print('3---------------------')

with open('file099_lutadores.csv', encoding='utf-8') as arquivo4:
    leitor_csv = DictReader(arquivo4, delimiter=',')  # separador -> ','

    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura']}")

print('4---------------------')
