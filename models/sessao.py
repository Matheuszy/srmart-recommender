from models.cliente import Cliente
from models.produto import Produto


class SessaoCliente:

    def __init__(
        self,
        cliente: Cliente,
        estado_atual: str,
        produto_atual: Produto
    ):
        self.cliente = cliente
        self.estado_atual = estado_atual
        self.produto_atual = produto_atual

    def atualizar_estado(self, novo_estado):
        self.estado_atual = novo_estado

    def atualizar_produto(self, produto):
        self.produto_atual = produto