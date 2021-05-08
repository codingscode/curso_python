"""
Projeto Final

"""
q = int(input('digite a quantidade de alunos: '))

todos = []

for cada in range(q):
    todos_com_dados = dict()
    todos_com_dados['nome'] = input(f'Digite o nome do {cada+1}º aluno: ')
    todos_com_dados['sexo'] = input(f'Digite o sexo(m/f) do aluno: ')

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
    print('')

#print(todos)
[print(cada) for cada in todos]


def aprovados(vetor):
    direto = list(filter(lambda cada: cada['media'] >= 7, vetor))
    masculino = list(filter(lambda cada: cada['sexo'] == 'm', direto))
    feminino = list(filter(lambda cada: cada['sexo'] == 'f', direto))

    return {'m': len(masculino), 'f': len(feminino)}  # m/f


def de_exame(vetor):
    lista = list(filter(lambda cada: 4 <= cada['media'] <= 7, vetor))
    masculino = list(filter(lambda cada: cada['sexo'] == 'm', lista))
    feminino = list(filter(lambda cada: cada['sexo'] == 'f', lista))

    return {'m': len(masculino), 'f': len(feminino)}


def reprovados(vetor):
    lista = list(filter(lambda cada: cada['media'] < 4, vetor))
    masculino = list(filter(lambda cada: cada['sexo'] == 'm', lista))
    feminino = list(filter(lambda cada: cada['sexo'] == 'f', lista))

    return {'m': len(masculino), 'f': len(feminino)}


print(f'total de alunos cadastrados: {q}')
#print(aprovados(todos), '\n')
#print(de_exame(todos), '\n')
#print(reprovados(todos), '\n')

print('Porcentagem:')
print(f'Quantidade porcentual de alunos aprovados: {(sum(aprovados(todos).values()))*100/q}%')
print(f'Quantidade porcentual de alunos de exame: {(sum(de_exame(todos).values()))*100/q}%')
print(f'Quantidade porcentual de alunos reprovados: {(sum(reprovados(todos).values()))*100/q}% \n')

print('Valores Absolutos:')
print(f"Quantidade de pessoas do sexo feminino aprovadas: {aprovados(todos)['f']}")
print(f"Quantidade de pessoas do sexo masculino aprovadas: {aprovados(todos)['m']}")
print(f"Quantidade de pessoas do sexo feminino de exame: {de_exame(todos)['f']}")
print(f"Quantidade de pessoas do sexo masculino de exame: {de_exame(todos)['m']}")
print(f"Quantidade de pessoas do sexo feminino reprovadas: {reprovados(todos)['f']}")
print(f"Quantidade de pessoas do sexo masculino reprovadas: {reprovados(todos)['m']}")
