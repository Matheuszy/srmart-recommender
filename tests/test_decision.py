import pytest
from decision.objetivo import MotorDecisao
from data.produtos import NOTEBOOK, MOUSE, HEADSET, SSD, MONITOR, MOCHILA, TECLADO


@pytest.fixture
def motor():
    return MotorDecisao()


def test_objetivo_saiu_retorna_none(motor):
    assert motor.objetivo("Saiu", NOTEBOOK) is None


def test_objetivo_headset_retorna_none(motor):
    assert motor.objetivo("Comprando", HEADSET) is None


def test_objetivo_notebook_visitando(motor):
    assert motor.objetivo("Visitando", NOTEBOOK) == MOUSE


def test_objetivo_notebook_comprando(motor):
    assert motor.objetivo("Comprando", NOTEBOOK) == SSD


def test_fator_comprando(motor):
    assert motor.fator("Comprando") == 1.5


def test_fator_saiu(motor):
    assert motor.fator("Saiu") == 0.0


def test_fator_estado_invalido(motor):
    assert motor.fator("EstadoDesconhecido") == 1.0
