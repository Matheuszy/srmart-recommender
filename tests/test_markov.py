import pytest
from markov.comportamento import CadeiaMarkov, ESTADOS


@pytest.fixture
def markov():
    return CadeiaMarkov()


def test_prever_retorna_estado_valido(markov):
    for estado in ESTADOS:
        resultado = markov.prever(estado)
        assert resultado in ESTADOS


def test_estado_saiu_permanece_saiu(markov):
    """Estado 'Saiu' tem probabilidade 1.0 de permanecer em 'Saiu'."""
    for _ in range(20):
        assert markov.prever("Saiu") == "Saiu"


def test_prever_estado_inexistente(markov):
    with pytest.raises(ValueError):
        markov.prever("EstadoInvalido")
