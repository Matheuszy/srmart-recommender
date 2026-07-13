import random

from models.produto import Produto


NOTEBOOK = Produto(
    1,
    "Notebook Dell",
    "Notebook",
    0.90
)

MOUSE = Produto(
    2,
    "Mouse Logitech",
    "Periféricos",
    0.80
)

TECLADO = Produto(
    3,
    "Teclado Mecânico",
    "Periféricos",
    0.75
)

HEADSET = Produto(
    4,
    "Headset HyperX",
    "Áudio",
    0.70
)

MONITOR = Produto(
    5,
    "Monitor LG",
    "Monitor",
    0.85
)

MOCHILA = Produto(
    6,
    "Mochila Dell",
    "Acessórios",
    0.60
)

SSD = Produto(
    7,
    "SSD Kingston",
    "Hardware",
    0.65
)

produtos = [
    NOTEBOOK,
    MOUSE,
    TECLADO,
    HEADSET,
    MONITOR,
    MOCHILA,
    SSD
]


def produto_aleatorio():
    return random.choice(produtos)