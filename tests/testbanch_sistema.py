import unittest
import os
from package.sistema import Sistema

class TestSistema(unittest.TestCase):
    def setUp(self):
        self.sistema = Sistema()
        self.sistema.arquivo_usuarios = "db/test_usuarios.json"
        self.sistema.arquivo_carros = "db/test_carros.json"
        if os.path.exists(self.sistema.arquivo_usuarios):
            os.remove(self.sistema.arquivo_usuarios)
        if os.path.exists(self.sistema.arquivo_carros):
            os.remove(self.sistema.arquivo_carros)

    def test_cadastrar_usuario(self):
        self.sistema.cadastrar_usuario("Arthur", "arthur@email.com")
        self.assertEqual(len(self.sistema.usuarios), 1)
        self.assertEqual(self.sistema.usuarios[0].nome, "Arthur")

    def test_cadastrar_carro(self):
        self.sistema.cadastrar_usuario("Arthur", "arthur@email.com")
        dono = self.sistema.usuarios[0]
        self.sistema.cadastrar_carro("Fiat Uno", 2020, 100.0, dono)
        self.assertEqual(len(self.sistema.carros), 1)
        self.assertEqual(self.sistema.carros[0].modelo, "Fiat Uno")

    def tearDown(self):
        if os.path.exists(self.sistema.arquivo_usuarios):
            os.remove(self.sistema.arquivo_usuarios)
        if os.path.exists(self.sistema.arquivo_carros):
            os.remove(self.sistema.arquivo_carros)

if __name__ == "__main__":
    unittest.main()

