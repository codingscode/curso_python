"""
Levantando os proprios erros com raise

raise -> lança exceções.
OBS: O raise nao é uma função. é uma palavra reservada, assim como o def...

-> criamos nossas proprias excecoes e mensagens.
A forma geral de utilização é :
raise TipoDoErro('Mensagem de erro')

"""

"""
raise ValueError('valor incorreto')

raise ValueError('valor incorreto')
ValueError: valor incorreto
"""

"""

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} será impresso na cor {cor}')


colore('codando python', 'azul') # normal

colore(False, 'azul')
-->    raise TypeError('texto precisa ser uma string')
-->TypeError: texto precisa ser uma string

colore('codando python', 123)
-->    raise TypeError('cor precisa ser uma string')
-->TypeError: cor precisa ser uma string

"""

"""
def colore(texto, cor):
    cores = ('verde', 'laranja', 'roxo', 'turquesa')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'a cor precisa estar entre {cores}')
        print('depois do raise')
    print(f'o texto {texto} será impresso na cor {cor}')


colore('codando python', 'verde') # normal

colore('codando python', 'laranja') # normal

colore('codando python', 'cinza')
-->     raise ValueError(f'a cor precisa estar entre {cores}')
-->ValueError: a cor precisa estar entre ('verde', 'laranja', 'roxo', 'turquesa')

OBS: o raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""
