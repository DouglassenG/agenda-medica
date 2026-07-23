import pytest
from api_mock.server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_listar_todos_agendamentos(client):
    response = client.get("/api/agendamentos")
    dados = response.get_json()

    assert response.status_code == 200
    assert len(dados) == 6


def test_busca_por_paciente(client):
    response = client.get("/api/agendamentos?busca=maria")
    dados = response.get_json()

    assert response.status_code == 200
    assert len(dados) == 1
    assert dados[0]["paciente"] == "Maria Silva"


def test_busca_sem_resultado(client):
    response = client.get("/api/agendamentos?busca=inexistente")
    dados = response.get_json()

    assert response.status_code == 200
    assert len(dados) == 0


def test_health_check(client):
    response = client.get("/api/health")
    dados = response.get_json()

    assert response.status_code == 200
    assert dados["status"] == "ok"