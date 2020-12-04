
import unittest
from file109_atividades import comer, dormir

"""
#descomentar esse e comentar o outro


class AtividadesTestes(unittest.TestCase):

    def test_comer(self):
        self.assertEqual(
            comer('salada', True),
            'Estou comendo salada porque quero manter a forma.'
        )

        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )


if __name__ == '__main__':
    unittest.main()

# no terminal do arquivo: python file109_testes.py
"""



print('1----------------')

"""
class AtividadesTestesref1(unittest.TestCase):

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('salada', True),
            'Estou comendo salada porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )


if __name__ == '__main__':
    unittest.main()

"""

print('2----------------')


class AtividadesTestesref2(unittest.TestCase):

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('salada', True),
            'Estou comendo salada porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas :('
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()





