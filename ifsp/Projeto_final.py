"""



"""

q = 2   # quantidade de alunos

todos = []

alunos_todosm = []
alunas_todasf = []

for cada in range(q):
    todos_com_dados = dict()
    todos_com_dados['nome'] = input(f'Digite o nome do {cada+1}º aluno: ')
    todos_com_dados['sexo'] = input(f'Digite o sexo do {cada+1}º aluno: ')

    pri_nota = float(input(f'Digite a 1ª nota do {cada+1}º aluno: '))
    seg_nota = float(input(f'Digite a 2ª nota do {cada+1}º aluno: '))
    ter_nota = float(input(f'Digite a 3ª nota do {cada+1}º aluno: '))
    todos_com_dados['notas'] = [pri_nota, seg_nota, ter_nota]
    todos_com_dados['media'] = sum(todos_com_dados['notas'])/len(todos_com_dados['notas'])
    notas_corretas = all(0 <= cada <= 10 for cada in todos_com_dados['notas'])

    if notas_corretas:
        todos.append(todos_com_dados)
    else:
        print(f"alguma nota de {todos_com_dados['nome']} está fora do intervalo")

print(todos)


def aprovados(vetor):
    direto = list(filter(lambda cada1: cada1['media'] >= 7, vetor))
    masculino = list(filter(lambda cada1: cada1['sexo'] == 'm', direto))
    feminino = list(filter(lambda cada2: cada2['sexo'] == 'f', direto))

    return [len(masculino), len(feminino)]  # m/f




print(f'total de alunos cadastrados: {q}')
print(aprovados(todos))





