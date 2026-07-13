import numpy as np

ESTADOS = [
    "Visitando",
    "Explorando",
    "Interessado",
    "Comprando",
    "Saiu"
]

TRANSICOES = [

    [0.20,0.60,0.15,0.05,0.00],

    [0.05,0.30,0.50,0.10,0.05],

    [0.00,0.20,0.30,0.45,0.05],

    [0.00,0.00,0.10,0.80,0.10],

    [0.00,0.00,0.00,0.00,1.00]

]


class CadeiaMarkov:

    def prever(self, estado):

        indice = ESTADOS.index(estado)

        return np.random.choice(

            ESTADOS,

            p=TRANSICOES[indice]

        )