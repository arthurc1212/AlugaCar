class Carro:
    def __init__(self, marca, modelo, ano, preco_dia, dono, disponivel=True):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_dia = preco_dia
        self.dono = dono
        self.disponivel = disponivel
        self.dias_alugado = 0
        self.valor_total = 0.0

    def alugar(self, dias):
        if self.disponivel:
            self.disponivel = False
            self.dias_alugado = dias
            self.valor_total = dias * self.preco_dia
            return True
        return False

    def devolver(self):
        self.disponivel = True
        self.dias_alugado = 0
        self.valor_total = 0.0

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "preco_dia": self.preco_dia,
            "dono": self.dono.nome if hasattr(self.dono, "nome") else self.dono,
            "disponivel": self.disponivel
        }

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Alugado ({self.dias_alugados} dias)"
        dono = self.dono.nome if hasattr(self.dono, "nome") else str(self.dono)
        return f"{self.marca} {self.modelo} ({self.ano}) - R${self.preco_dia}/dia - {status} - Dono: {dono}"
