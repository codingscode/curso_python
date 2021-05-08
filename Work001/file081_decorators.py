"""
Decorators

O que são ?
- São funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de higher order functions
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar/ Açucar Sintatico)

"""
# Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) a Geek University')


teste = seja_educado(saudacao)

teste()
print('----------------')
saudacao()

print('-----------------')


def indignite():
    print('transito parado')


expressando_indig = seja_educado(indignite)
expressando_indig()

print('-----------------')

# Decorators com syntax sugar (recomendado)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Fulanis')


apresentando()

print('-----------------')

@seja_educado_mesmo
def dormir():
    print('quero dormir')


dormir()

#OBS: Não confunda Decorator com Decorator Function
print('-----------------')
