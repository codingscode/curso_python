def comer(comida, e_saudavel):
    if e_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'
    return f'Estou comendo {comida} porque {final}.'


def dormir(numero_horas):
    if numero_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {numero_horas} horas. :('


def e_engracada(pessoa):
    pass