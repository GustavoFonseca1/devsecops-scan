import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_hello():
    client = app.test_client()

    response = client.get("/hello?nome=Gustavo")

    assert response.status_code == 200
