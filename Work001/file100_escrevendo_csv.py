"""
Escrevendo em arquivo .csv

reader() (leitor) writer() (escritor)
writerow() -> Escreve uma linha


"""

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. utilizamos o metodo writerow para escrever cada linha. Este metodo recebe uma lista.
from csv import writer

with open('file100_criandoarquivo.csv', 'w', encoding='utf-8') as arquivo:  # 'a' -> adiciona ao conteudo presente
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])



print('-----------------')
print('-----------------')
print('-----------------')
