"""
Modulo collection - Counter

Collections -> High-performance Container Datatypes

Counter -> Recebe um interável como parametro e cria um objeto do tipo Collections Counter
que é parecido com um dicionario, contendo como chave o elemento da lista passada como
parametro e como valor a quantidade de ocorrencias desse elemento.



"""

# Utlizando o counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista_1 = [3, 7, 40, 3, 7, 3, 7, 16, 3, 40, 7, 21, 7]

resultado = Counter(lista_1)   # chave/valor

print(f'resultado: {resultado} || seu tipo: {type(resultado)}')
# obs: cada elemento da lista ficou como chave e o valor o número de ocorrencias
print('--------------\n')

# Exemplo 2

print(f'Nasca de bacana: \n {Counter("Nasca de bacana")}')

print('--------------\n')

texto = """Minha terra tem palmeiras, Onde canta o Sabiá;
As aves, que aqui gorjeiam, Não gorjeiam como lá.
Nosso céu tem mais estrelas, Nossas várzeas têm mais flores,
Nossos bosques têm mais vida, Nossa vida mais amores. """

palavras = texto.split()

#print(palavras)
resultado2 = Counter(palavras)

print(f'ocorrencias de palavras: {resultado2}')

# as 'n' mais comuns
print(f'as "5" mais comuns: {resultado2.most_common(5)}')
print("----------------------")

print(dir(Counter))
