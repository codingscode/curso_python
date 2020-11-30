
import unittest

from file109_atividades import comer, dormir


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








