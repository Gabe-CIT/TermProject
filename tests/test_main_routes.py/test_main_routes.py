import pytest
from application import application as app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def login(client, email, password):
    return client.post('/auth/login', data={'email_address_data': email, 'password_data': password}, follow_redirects=True)

def test_homepage(client):
    """
    testing to see if homepage will get rendered
    """
    res = client.get('/')

    assert b'Book an Appointment' in res.data
    assert res.status_code == 200

def test_services_page(client):
    """
    testing to see if services page will get rendered
    """
    login(client, "ncao5@my.bcit.ca", "1234")

    res = client.get('/services')
    
    assert b'All Services' in res.data
    assert b'Counseling' in res.data
    assert b'Group Therapy' in res.data
    assert b'Psychiatry' in res.data
    assert res.status_code == 200