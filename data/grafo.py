from data.produtos import *

grafo = {

    NOTEBOOK: [
        MOUSE,
        SSD,
        MOCHILA
    ],

    MOUSE: [
        TECLADO,
        HEADSET
    ],

    TECLADO: [
        HEADSET
    ],

    SSD: [
        MONITOR,
        NOTEBOOK
    ],

    MOCHILA: [
        NOTEBOOK,
        MONITOR
    ],

    MONITOR: [
        NOTEBOOK,
        HEADSET
    ],

    HEADSET: [
        NOTEBOOK
    ]

}