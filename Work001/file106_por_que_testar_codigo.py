"""
Por que testar nosso código

Testes automatizados

- Reduzir bugs(problemas) no código existente.
- Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos.
- Testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos.
- Testes garantem que refatoração que costumamos fazer não tragam novos bugs.


TDD - test driven development (desenvolvimento guiado por testes)

Com TDD é utilizadp estágios de desenvolvimento:
   - Você escreve seu teste primeiro;
   - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
   - Então refatora o código para realizar a funcionalidade e testa novamente
   - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
   - Red;
   - Green;
   - Refactor;



"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        return f'{self.__nome} está miando...'


animal1 = Gato('felix')

print(animal1.nome)
print(animal1.miar())

