import pytest
from bayes.compra import RedeBayesiana
from models.cliente import Cliente


@pytest.fixture
def bayes():
    return RedeBayesiana()


def test_probabilidade_minima(bayes):
    cliente = Cliente(historico=0, tempo_site=0, clicou_promocao=0)
    assert bayes.calcular(cliente) == 0.1


def test_probabilidade_maxima(bayes):
    cliente = Cliente(historico=1, tempo_site=1, clicou_promocao=1)
    assert bayes.calcular(cliente) == 0.9


def test_probabilidade_intermediaria(bayes):
    cliente = Cliente(historico=1, tempo_site=0, clicou_promocao=1)
    assert bayes.calcular(cliente) == 0.7


def test_todas_combinacoes(bayes):
    """Garante que todas as 8 combinações existem e retornam float entre 0 e 1."""
    for h in (0, 1):
        for t in (0, 1):
            for c in (0, 1):
                cliente = Cliente(historico=h, tempo_site=t, clicou_promocao=c)
                prob = bayes.calcular(cliente)
                assert 0.0 <= prob <= 1.0
