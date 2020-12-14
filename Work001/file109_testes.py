
import unittest
from file109_atividades import comer, dormir

#descomentar esse e comentar o outro


"""
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

"""

# no terminal do arquivo: python file109_testes.py

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

"""
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
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()

"""

# no terminal do arquivo: python file109_testes.py
"""
FFFF
======================================================================
FAIL: test_comer_gostosa (__main__.AtividadesTestesref2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "file109_testes.py", line 66, in test_comer_gostosa
    self.assertEqual(
AssertionError: None != 'Estou comendo pizza porque a gente só vive uma vez.'

======================================================================
FAIL: test_comer_saudavel (__main__.AtividadesTestesref2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "file109_testes.py", line 60, in test_comer_saudavel
    self.assertEqual(
AssertionError: None != 'Estou comendo salada porque quero manter a forma.'

======================================================================
FAIL: test_dormir_muito (__main__.AtividadesTestesref2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "file109_testes.py", line 78, in test_dormir_muito
    self.assertEqual(
AssertionError: None != 'Ptz! Dormi muito! Estou atrasado para o trabalho!'

======================================================================
FAIL: test_dormir_pouco (__main__.AtividadesTestesref2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "file109_testes.py", line 72, in test_dormir_pouco
    self.assertEqual(
AssertionError: None != 'Continuo cansado após dormir por 4 horas :('

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=4)

"""

print('3----------------')

"""

"""


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


if __name__ == '__main__':
    unittest.main()


print('4------------------')
"""
Para executar os testes com unittest no modo verbose
no terminal: python nome_do_modulo.py -v
"""




