"""
Novos metadados

"""
from importlib import metadata

print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')

# lista de metadados
print(list(metadados_pip))
#print(metadados_pip)
print(metadados_pip['Project-URL'])

print('1---------------------')

# quantidade de arquivos
print(len(metadata.files('pip')))

print('2---------------------')

# o que o pip requer
print(metadata.requires('pip'))

"""
no terminal:    pip install django
"""

print('3---------------------')
print('4---------------------')