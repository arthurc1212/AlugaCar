class Carro:
    def __init__(self, marca, modelo, ano, preco_dia, dono, disponivel=True, dias_alugado=0, valor_total=0.0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_dia = preco_dia
        self.dono = dono
        self.disponivel = disponivel
        self.dias_alugado = dias_alugado
        self.valor_total = valor_total

    def alugar(self, dias):
        if not self.disponivel:
            raise ValueError("Carro não está disponível")
        self.disponivel = False
        self.dias_alugado = dias
        self.valor_total = float(self.preco_dia) * int(dias)
        return self.valor_total

    def devolver(self):
        if self.disponivel:
            raise ValueError("Carro já está disponível")
        self.disponivel = True
        self.dias_alugado = 0
        self.valor_total = 0.0

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "preco_dia": self.preco_dia,
            "dono": self.dono,
            "disponivel": self.disponivel,
            "dias_alugado": self.dias_alugado,
            "valor_total": self.valor_total
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["marca"], d["modelo"], d["ano"], d["preco_dia"], d["dono"], d.get("disponivel", True), d.get("dias_alugado",0), d.get("valor_total",0.0))
