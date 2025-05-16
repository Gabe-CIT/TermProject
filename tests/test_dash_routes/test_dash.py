import pytest
from main import application as app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def login(client, email, password):
    return client.post('/auth/login', data={'email_address_data': email, 'password_data': password}, follow_redirects=True)

def test_dashboard_redirect(client):
    login(client, "ncao5@my.bcit.ca", "5678")

    res = client.get("/dashboard/student/ncao@my.bcit.ca")

    assert res.status_code == 302

def test_dashboard_redirect_dashboard(client):
    login(client, "ncao5@my.bcit.ca", "5678")

    res = client.get("/dashboard/student/ncao@my.bcit.ca", follow_redirects=True)

    assert res.status_code == 200
    assert b'Welcome' in res.data