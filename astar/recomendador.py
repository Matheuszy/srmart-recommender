import heapq
from itertools import count

from data.grafo import grafo


class Recomendador:

    def __init__(
        self,
        probabilidade_cliente,
        fator_estado
    ):

        self.grafo = grafo
        self.probabilidade_cliente = probabilidade_cliente
        self.fator_estado = fator_estado
        self.contador = count()

    def heuristica(self, produto):

        return 1 - (

            produto.conversao *

            self.probabilidade_cliente *

            self.fator_estado

        )

    def buscar(
        self,
        inicio,
        objetivo
    ):

        fila = []

        heapq.heappush(

            fila,

            (

                0,

                next(self.contador),

                inicio

            )

        )

        veio_de = {
            inicio: None
        }

        custo = {
            inicio: 0
        }

        while fila:

            _, _, atual = heapq.heappop(fila)

            if atual == objetivo:
                break

            for vizinho in self.grafo.get(atual, []):

                novo_custo = custo[atual] + 1

                if (

                    vizinho not in custo

                    or

                    novo_custo < custo[vizinho]

                ):

                    custo[vizinho] = novo_custo

                    prioridade = (

                        novo_custo +

                        self.heuristica(vizinho)

                    )

                    heapq.heappush(

                        fila,

                        (

                            prioridade,

                            next(self.contador),

                            vizinho

                        )

                    )

                    veio_de[vizinho] = atual

        if objetivo not in veio_de:
            return []

        caminho = []

        atual = objetivo

        while atual is not None:

            caminho.append(atual)

            atual = veio_de[atual]

        caminho.reverse()

        return caminho