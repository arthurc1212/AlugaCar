from .pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, email, tipo="comum"):
        super().__init__(nome, email)
        self.tipo = tipo

    def to_dict(self):
        return {"nome": self.nome, "email": self.email, "tipo": self.tipo}

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("nome"), d.get("email"), d.get("tipo","comum"))
