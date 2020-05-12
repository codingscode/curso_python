"""
Documentando funções com docstrings




"""

print(help(print))
print('--------------------------\n')


def diz_oi():
    """ uma função simples que retorna 'Oi' """
    return 'Oi'


from file035_doc_f_com_docstrings import diz_oi

print(f'1-> {diz_oi()}')
print('---------------')
print(f'2-> {help(diz_oi)}')
print('---------------')
print(f'3-> {diz_oi.__doc__}')
