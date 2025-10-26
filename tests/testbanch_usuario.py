import unittest
from package.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_criacao_usuario(self):
        u = Usuario("Arthur", "arthur@email.com")
        self.assertEqual(u.nome, "Arthur")
        self.assertEqual(u.email, "arthur@email.com")

    def test_to_dict(self):
        u = Usuario("Arthur", "arthur@email.com")
        esperado = {"nome": "Arthur", "email": "arthur@email.com"}
        self.assertEqual(u.to_dict(), esperado)

    def test_str(self):
        u = Usuario("Arthur", "arthur@email.com")
        self.assertEqual(str(u), "Arthur (arthur@email.com)")

if __name__ == "__main__":
    unittest.main()

