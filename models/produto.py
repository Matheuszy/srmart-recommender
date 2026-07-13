class Produto:

    def __init__(self, id, nome, categoria, conversao):

        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.conversao = conversao

    def __repr__(self):
        return f"{self.nome} ({self.categoria})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id