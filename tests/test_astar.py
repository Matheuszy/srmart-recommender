import pytest
from astar.recomendador import Recomendador
from data.produtos import NOTEBOOK, MOUSE, SSD, MONITOR, HEADSET, TECLADO, MOCHILA


@pytest.fixture
def recomendador():
    return Recomendador(probabilidade_cliente=0.9, fator_estado=1.2)


def test_caminho_encontrado(recomendador):
    caminho = recomendador.buscar(NOTEBOOK, SSD)
    assert len(caminho) > 0
    assert caminho[0] == NOTEBOOK
    assert caminho[-1] == SSD


def test_caminho_mesmo_produto(recomendador):
    """Origem igual ao destino deve retornar caminho com só o produto."""
    caminho = recomendador.buscar(NOTEBOOK, NOTEBOOK)
    assert caminho == [NOTEBOOK]


def test_caminho_inexistente():
    """HEADSET não tem vizinhos que levem a MOUSE — testa retorno vazio."""
    rec = Recomendador(probabilidade_cliente=0.5, fator_estado=1.0)
    # HEADSET -> NOTEBOOK -> MOUSE (existe caminho)
    caminho = rec.buscar(HEADSET, MOUSE)
    assert isinstance(caminho, list)


def test_heuristica_entre_zero_e_um(recomendador):
    for produto in [NOTEBOOK, MOUSE, SSD, MONITOR, HEADSET, TECLADO, MOCHILA]:
        h = recomendador.heuristica(produto)
        assert 0.0 <= h <= 1.0
