"""


"""
uma_string = 'primeiro_teste'

print(f'{uma_string} || {type(uma_string)} || tamanho: {len(uma_string)}')

# números imaginarios(complexo):  real + imaginario*j
imaginario = 4 + 5j

print(f'{imaginario} || {type(imaginario)}')

""" 
palavras que não podem ser usadas na nomeação de variaveis(33):
and, del, from, None, True, as, elif, global, nonlocal, try, assert, else, if, not, while,
break, except, import, or, with, class, False, in, pass, yield, continue, finally, is, raise,
def, for, lambda, return 
"""

# operações : +, -, *, /, **, //, %

oito_por_3 = 8//3

print(oito_por_3)
print('-----------\n')

uma_string2 = 'goiabada de marmelo'

print(f'{uma_string2} || {uma_string[2]}  || {uma_string2[3:]}')

# concatenando 2 strings
texto1 = 'antes separados, '
texto2 = 'e agora juntos'
textos1_2 = texto1 + texto2

print(f'como fica agora: {textos1_2}\n')

texto4 = 'snake '
print(f'3 vezes: {texto4*3}\n')

#colocando uma texto em maiusculo e minusculo
para_maiusculo = 'em maiusculo'
para_minusculo = 'EM MINUSCULO'
primeira_maiuscula = 'primeira letra em maiusculo'

print(para_maiusculo.upper())
print(para_maiusculo.lower())
print(primeira_maiuscula.capitalize())
print('----------------\n')

# comparação
el_1 = 1
el_2 = '1'
true_1 = True
true_2 = 'True'

print(f'el_1 é igual a el_2: {el_1 == el_2}')
print(f'true_1 é igual a true_2: {true_1 == true_2}\n')

print(f'{1 > 2} || {3 != 2} || {2 == 2}\n')

# usando bool(x), retorna se x é booleano

print(f'{bool(0)} || {bool("")} || {bool(None)} ')
print(f'{bool(1)} || {bool(-100)} || {bool(13.5)}')
print(f'{bool("teste")} || {bool(True)}\n')

# outros operadores booleanos
valor_1 = 5
valor_2 = 3
lista_1 = [2, 7, -2, 15, 23]
elemento = 7

print(f'{valor_1 is valor_2} || {valor_1 is not valor_2} || {elemento in lista_1} || {elemento not in lista_1}\n')

# == e is não são totalmente iguais

lista_2 = [8, 47, 51]
lista_3 = [8, 47, 51]

print(f'{lista_2 == lista_3} || {lista_2 is lista_3}')
"""
== verifica valores, is verifica se são o mesmo objeto
 
"""

print('-------------------\n')

uma_string3 = 'aranha'
#para_int = int(uma_string3)   dá erro
#print(f'para_int: {para_int}')

uma_string4 = '5'
para_int2 = int(uma_string4)
print(f'para_int2: {para_int2}')
