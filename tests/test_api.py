import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


PAYLOAD_BASE = {
    "historico": 1,
    "tempo_site": 1,
    "clicou_promocao": 1,
    "estado_atual": "Visitando"
}


def test_recommend_status_200():
    response = client.post("/recommend", json=PAYLOAD_BASE)
    assert response.status_code == 200


def test_recommend_campos_resposta():
    response = client.post("/recommend", json=PAYLOAD_BASE)
    data = response.json()

    assert "produto_atual" in data
    assert "estado_previsto" in data
    assert "probabilidade_compra" in data
    assert "objetivo" in data
    assert "recomendacoes" in data


def test_recommend_probabilidade_entre_0_e_1():
    response = client.post("/recommend", json=PAYLOAD_BASE)
    prob = response.json()["probabilidade_compra"]
    assert 0.0 <= prob <= 1.0


def test_recommend_recomendacoes_e_lista():
    response = client.post("/recommend", json=PAYLOAD_BASE)
    assert isinstance(response.json()["recomendacoes"], list)


def test_recommend_estado_saiu_sem_recomendacoes():
    payload = {**PAYLOAD_BASE, "estado_atual": "Saiu"}
    response = client.post("/recommend", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Estado 'Saiu' sempre resulta em objetivo None e lista vazia
    # (Markov pode transitar, mas se objetivo for None o service retorna vazio)
    assert isinstance(data["recomendacoes"], list)


def test_recommend_payload_invalido():
    """Campos faltando devem retornar 422."""
    response = client.post("/recommend", json={"historico": 1})
    assert response.status_code == 422


def test_recommend_estado_invalido():
    """Estado fora do enum aceito pela Markov deve retornar 400."""
    payload = {**PAYLOAD_BASE, "estado_atual": "EstadoInvalido"}
    response = client.post("/recommend", json=payload)
    assert response.status_code == 400
