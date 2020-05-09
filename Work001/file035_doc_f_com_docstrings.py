"""
Documentando funções com docstrings




"""

print(help(print))
print('--------------------------\n')


def diz_oi():
    """ uma função simples que retorn 'Oi' """
    return 'Oi'


from file035_doc_f_com_docstrings import diz_oi

print(diz_oi())
print('---------------')
print(help(diz_oi))
print('---------------')
print(diz_oi.__doc__)




