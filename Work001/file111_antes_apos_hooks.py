"""
Unittest : antes após Hooks

hooks -> são os testes em si. Ou seja, a execução dos testes.

setup() -> é executado antes de cada método de teste. É útil para criarmos instancias de objetos e
outros dados.

tearDown() -> é executado ao final de cada métdo de teste. É útil para excluir dados ou fechar
conexões com bancos de dados.


"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDrop() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDrop() vai rodar após o teste
        pass

    def tearDown(self):
        # configurações do tearDown()
        pass







