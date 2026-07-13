from data.produtos import *


class MotorDecisao:

    FATORES = {
        "Visitando": 0.8,
        "Explorando": 1.0,
        "Interessado": 1.2,
        "Comprando": 1.5,
        "Saiu": 0.0
    }

    def fator(self, estado):
        return self.FATORES.get(estado, 1.0)

    def objetivo(self, estado, produto):
        """
        Escolhe dinamicamente o objetivo da busca
        considerando o estado do cliente e o produto
        que ele está visualizando.
        """

        if estado == "Saiu":
            return None

        # Cliente está vendo um notebook
        if produto == NOTEBOOK:

            if estado == "Visitando":
                return MOUSE

            if estado == "Explorando":
                return MONITOR

            if estado == "Interessado":
                return HEADSET

            if estado == "Comprando":
                return SSD

        # Cliente está vendo um mouse
        elif produto == MOUSE:

            if estado == "Visitando":
                return TECLADO

            if estado == "Explorando":
                return HEADSET

            if estado == "Interessado":
                return HEADSET

            if estado == "Comprando":
                return HEADSET

        # Cliente está vendo um SSD
        elif produto == SSD:

            if estado == "Visitando":
                return MONITOR

            if estado == "Explorando":
                return MONITOR

            if estado == "Interessado":
                return MONITOR

            if estado == "Comprando":
                return MONITOR

        # Cliente está vendo um teclado
        elif produto == TECLADO:

            return HEADSET

        # Cliente está vendo uma mochila
        elif produto == MOCHILA:

            return MONITOR

        # Cliente está vendo um monitor
        elif produto == MONITOR:

            return HEADSET

        # Cliente já está vendo o headset
        elif produto == HEADSET:

            return None

        return None