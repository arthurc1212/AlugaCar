import unittest
from package.carro import Carro

class TestCarro(unittest.TestCase):
    def setUp(self):
        self.carro = Carro("Fiat Uno", 2020, 100.0, "Arthur")

    def test_criacao_carro(self):
        self.assertEqual(self.carro.modelo, "Fiat Uno")
        self.assertTrue(self.carro.disponivel)

    def test_alugar_carro(self):
        resultado = self.carro.alugar()
        self.assertTrue(resultado)
        self.assertFalse(self.carro.disponivel)

    def test_alugar_carro_indisponivel(self):
        self.carro.alugar()
        resultado = self.carro.alugar()
        self.assertFalse(resultado)

    def test_devolver_carro(self):
        self.carro.alugar()
        self.carro.devolver()
        self.assertTrue(self.carro.disponivel)

if __name__ == "__main__":
    unittest.main()

