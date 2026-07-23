import pytest
from app import create_app
from app.models import init_db, create_user
import os


@pytest.fixture
def client():
    os.environ["DATABASE_PATH"] = "test.db"

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        create_user("testuser", "test@test.com", "test123")
        yield client

    if os.path.exists("test.db"):
        os.remove("test.db")


def test_login_valido(client):
    response = client.post("/login", data={
        "login": "testuser",
        "password": "test123"
    }, follow_redirects=True)

    assert response.status_code == 200


def test_login_invalido(client):
    response = client.post("/login", data={
        "login": "testuser",
        "password": "senhaerrada"
    })

    assert response.status_code == 401


def test_login_campos_vazios(client):
    response = client.post("/login", data={
        "login": "",
        "password": ""
    })

    assert response.status_code == 400


def test_logout(client):
    client.post("/login", data={
        "login": "testuser",
        "password": "test123"
    })

    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200