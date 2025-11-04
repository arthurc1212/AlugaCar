from package.models.usuario import Usuario
from package.models.carro import Carro
from .dbjson import JSONDB
from .auth import Auth

DB_PATH = "storage/db.json"

class Sistema:
    def __init__(self, db_path=DB_PATH):
        self.db = JSONDB(db_path)
        self.auth = Auth(db_path)
        self.current_user = None
        self._load()

    def _load(self):
        data = self.db.get_all()
        self.users = data.get("users", [])
        self.carros = [Carro.from_dict(c) for c in data.get("cars", [])]

    def _save_cars(self):
        cars_list = [c.to_dict() for c in self.carros]
        self.db.replace_list("cars", cars_list)

    def cadastrar_usuario(self, nome, email, senha):
        self.auth.register(nome, email, senha)
        self._load()

    def autenticar(self, email, senha):
        ok = self.auth.authenticate(email, senha)
        if ok:
            self.current_user = email.strip().lower()
        return ok

    def logout(self):
        self.current_user = None

    def cadastrar_carro(self, marca, modelo, ano, preco_dia):
        if not self.current_user:
            raise PermissionError("É necessário realizar login para cadastrar um carro.")
        dono_info = next((u for u in self.users if u["email"] == self.current_user), None)
        dono_nome = dono_info["nome"] if dono_info else self.current_user
        carro = Carro(marca, modelo, ano, preco_dia, dono=self.current_user, disponivel=True)
        self.carros.append(carro)
        self._save_cars()
        return carro

    def listar_carros(self):
        return list(self.carros)

    def alugar_carro(self, indice, dias):
        try:
            carro = self.carros[indice-1]
        except IndexError:
            raise IndexError("Índice inválido")
        valor = carro.alugar(dias)
        self._save_cars()
        return valor

    def devolver_carro(self, indice):
        try:
            carro = self.carros[indice-1]
        except IndexError:
            raise IndexError("Índice inválido")
        carro.devolver()
        self._save_cars()
