import pytest
from main import application as app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def login(client, email, password):
    return client.post('/auth/login', data={'email_address_data': email, 'password_data': password}, follow_redirects=True)


def test_confirm_booking(client):
    """
    testing to see if form on booking_page gets posted into database
    """
    login(client, "testUser@my.bcit.ca", "1234")


    res = client.post('/booking/confirm', data={
        'appt_advisor': 1,
        'appt_purpose': "i need help",
        'appt_type': 'In-Person',
        'appt_date': '2025-05-09',
        'appt_time': "09:00"
    })
    
    assert res.status_code == 302

def test_create_booking(client):
    """
    testing to see if booking page will get rendered
    """
    login(client, "testUser@my.bcit.ca", "1234")

    res = client.get('/booking/1')

    assert b'Booking appointment with:' in res.data
    assert res.status_code == 200