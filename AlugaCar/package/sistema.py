from package.usuario import Usuario
from package.carro import Carro

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.carros = []
        
    def cadastrar_usuario(self, nome, email):
        if any(u.email == email for u in self.usuarios):
            print("\n Usuário já cadastrado!")
            return
        self.usuarios.append(Usuario(nome, email))
        print(f"\n Usuário {nome} cadastrado com sucesso!")

    def cadastrar_carro(self, marca, modelo, ano, preco_dia, dono):
        self.carros.append(Carro(marca, modelo, ano, preco_dia, dono))
        print(f"\n Carro {marca} {modelo} cadastrado por {dono.nome}!")

    def listar_carros(self):
        if not self.carros:
            print("\nNenhum carro cadastrado.")
            return
        print("\n Carros disponíveis:")
        for i, c in enumerate(self.carros, 1):
            status = "Disponível" if c.disponivel else "Alugado"
            print(f"{i}. {c.marca} {c.modelo} - {status} - Dono: {c.dono.nome} - Valor da Diária: R${c.preco_dia}")

    def alugar_carro(self, indice, dias):
        try:
            carro = self.carros[indice - 1]
            if carro.alugar(dias):
                print(f"\n Você alugou o carro {carro.marca} {carro.modelo}!")
                print(f"\n Valor total: R${carro.valor_total:.2f}")
            else:
                print("\n Esse carro já está alugado.")
        except IndexError:
            print("\n Índice inválido.")

    def devolver_carro(self, indice):
        try:
            carro = self.carros[indice - 1]
            if carro.disponivel:
                print("\nÍndice inválido.") 
            else:
                carro.devolver()
                print(f"\nO carro {carro.marca} {carro.modelo} foi devolvido com sucesso!")
        except IndexError:
                print("\nÍndice inválido.")


