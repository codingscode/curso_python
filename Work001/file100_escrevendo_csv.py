"""
Escrevendo em arquivo .csv

reader() (leitor) writer() (escritor)
writerow() -> Escreve uma linha

"""
"""
writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. utilizamos o metodo writerow para escrever 
cada linha. Este metodo recebe uma lista.
"""

from csv import writer

with open('file100_criandoarquivo.csv', 'a', encoding='utf-8', newline='') as arquivo:  # 'a' -> adiciona ao conteudo presente
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])

print('1-----------------')
# DictWriter
# obs: as chaves do dicionario devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('file100_criandoarquivo2.csv', 'w', encoding='utf-8', newline='') as arquivo2:  # experimentar 'a' no lugar de 'w'
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo2, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (minutos): ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao': duracao})

print('2-----------------')
