import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index_route_redirect(client):
    response = client.get('/')
    assert response.status_code == 302

def test_sales_cakes_route(client):
    response = client.get('/sales/cakes')
    assert response.status_code == 200
    assert b'Sales' in response.data

def test_sales_cakes_query_string(client):
    response = client.get('/sales/cakes?quarter=3&product_type=Cookie&product_type=Cake&table_attribute=product&order_by_descending=0')
    assert response.status_code == 200
    assert b'Vile Human' in response.data