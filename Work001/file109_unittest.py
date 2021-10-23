"""
Introdução ao Unittest

Unittest -> teste unitário

o que é ?
é a forma de se testar unidades individuais de código fonte.
Unidades individuais podem ser: funções, métodos, classes, módulos etc.

#obs: Teste unitário não é específico da linguagem Python.

Para criar nossos teste, criamos classes que herdam de unittest.TestCase é a partir de então
ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

https://docs.python.org/3/library/unittest.html
     ver as assertions
assertEqual(a, b), assertNotEqual(a, b), assertTrue(x), assertFalse(x), assertIs(a, b), assertIsNot(a, b),
assertIsNone(x), assertIsNotNone(x), assertIn(a, b), assertNotIn(a, b), assertIsInstance(a, b),
assertNotIsInstance(a, b),

testes por convenção usa-se "test_"

"""

# Prática utilizando a abordagem TDD

