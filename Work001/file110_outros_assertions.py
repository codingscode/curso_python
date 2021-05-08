"""
Unittest -> Outros tipos de assertions




"""

import unittest
from file110_atividades import comer, dormir, e_engracada


class AtividadesTestesref3(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('salada', True),
            'Estou comendo salada porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_e_engracada(self):  #self.assertFalse(None) -> True
        self.assertEqual(e_engracada('Sérgio Malandro'), False)
        self.assertFalse(e_engracada('Sérgio Malandro'))
        self.assertTrue(e_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()


print('4------------------')
"""
Para executar os testes com unittest no modo verbose
no terminal: python nome_do_modulo.py -v
no terminal: python file110_outros_assertions.py -v
"""

"""
None não é nem True nem False
"""

