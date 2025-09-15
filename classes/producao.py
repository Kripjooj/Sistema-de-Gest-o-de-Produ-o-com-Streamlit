class Producao:
    def __init__(self, HORA_INICIO, HORA_TERMINO, data, setor, cliente, modelo, of, qtd_aprovada, qtd_retrabalho, motivo_falha, responsavel, turno):
        self.data = data
        self.HORA_INICIO = HORA_INICIO
        self.HORA_TÉRMINO = HORA_TERMINO
        self.setor = setor
        self.cliente = cliente
        self.modelo = modelo
        self.of = of
        self.qtd_aprovada = qtd_aprovada
        self.qtd_retrabalho = qtd_retrabalho
        self.motivo_falha = motivo_falha
        self.responsavel = responsavel
        self.turno = turno # Novo atributo

    def to_dict(self):
        return {
            "DATA": self.data,
            "HORA_INICIO": self.HORA_INICIO,
            "HORA_TÉRMINO": self.HORA_TÉRMINO,
            "Modelo": self.modelo,
            "OF": self.of,
            "CLIENTE": self.cliente,
            "QTD_PEÇAS_APROVADAS": self.qtd_aprovada,
            "MOTIVO_FALHAS": self.motivo_falha,
            "QTD_RETRABALHADA": self.qtd_retrabalho,
            "RESPONSÁVEL": self.responsavel,
            "setor": self.setor,
            "TURNO": self.turno # Adicionado ao dicionário
        }

    def resumo(self):
        return f"{self.data} | Setor: {self.setor} | {self.cliente} - {self.modelo} | Aprovadas: {self.qtd_aprovada} | Retrabalho: {self.qtd_retrabalho}"