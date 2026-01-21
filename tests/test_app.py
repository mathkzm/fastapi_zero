from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    3 etapas (AAA):
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Assert  - Garante que A é A
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo!'}


def test_hello():
    client = TestClient(app)

    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello, world!</h1>' in response.text
