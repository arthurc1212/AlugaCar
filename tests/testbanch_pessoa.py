import unittest
from package.pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def test_criacao_pessoa(self):
        p = Pessoa("Arthur", "arthur@email.com")
        self.assertEqual(p.nome, "Arthur")
        self.assertEqual(p.email, "arthur@email.com")

