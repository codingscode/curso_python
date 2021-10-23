import unittest

from file111_robo import Robo

#descomentar, testar 1 de cada vez



class RoboTestes(unittest.TestCase):

    def test_carregar(self):
        megaman = Robo('Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)

    def test_dizer_nome(self):
        megaman = Robo('Mega Man', bateria=50)
        self.assertEqual(megaman.dizer_nome(), 'tik tik tik tik. Eu sou MEGA MAN')
        self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%')


if __name__ == '__main__':
    unittest.main()


#no terminal da pasta do arquivo:
#   python file111_robo_testes.py -v

"""

class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'tik tik tik tik. Eu sou MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')


if __name__ == '__main__':
    unittest.main()
"""

"""
class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp sendo executado...')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'tik tik tik tik. Eu sou MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('tearDown sendo executado...')


if __name__ == '__main__':
    unittest.main()
"""

"""
no terminal da pasta do arquivo:
   python file111_robo_testes.py -v
   
"""

