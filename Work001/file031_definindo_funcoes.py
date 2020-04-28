"""
Definindo funções

funções são pequenos trechos de códigos que realizam tarefas específicas
- pode ou não receber entradas de dados e retornar uma saída de dados
- muito uteis para executar procedimentos similares por repetidas vezes
OBS: Se você escrever uma função que realiza varias tarefas dentro dela:
 é bom fazer uma verificação para que a função seja simplificada.

Ex:
print(), len(), max(), count(), etc...



"""

# utilização funções:
cores = ['laranja', 'verde', 'azul', 'amarelo', 'branco', 'cinza']

# utilizando função integrada (built-in)
print(cores)
cores.append('purpura')   # append só usa para listas
print(cores)

print(help(print))
# DRY - don't repeat yourself

print('---------------\n')

"""
definindo funções:

def nome_funcao(parametros):
    // bloco da função
    
Onde:
nome_funcao -> sempre minusculo, 
parametros -> são opcionais. mais de um separados por virgula
bloco da função -> corpo da função. Ocorre o processamento, pode ou não ter retorno



"""

# definindo a primeira função


def diz_oi():
    print('oi')


"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Nossa função aqui, só executa uma tarefa
3 - n recebe nenhum parametro de entrada
4 - esta função não retorna nada



"""
# chamando função
diz_oi()

print('-----------------------')


def dizer_numeros():
    print('1, 2, 3, 4, 5 ...')

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função através
# da variavel


diga = dizer_numeros

diga()











