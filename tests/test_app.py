from chalice.test import Client
from app import app

def test_index_function():
    with Client(app) as client:
        response = client.http.get('/')
        assert response.status_code == 200
        assert response.json_body == {'hello': 'world'}