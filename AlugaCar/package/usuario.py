from package.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, email, tipo="comum"):
        super().__init__(nome, email)  
