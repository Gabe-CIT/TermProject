import pytest
from application import application as app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def login(client, email, password):
    return client.post('/auth/login', data={'email_address_data': email, 'password_data': password}, follow_redirects=True)


def test_booking_page_form_post(client):
    """
    testing to see if form on booking_page gets posted into database
    """
    login(client, "ncao5@my.bcit.ca", "5678")


    res = client.post('/booking/confirm', data={
        'appt_advisor': 7,
        'appt_purpose': "i need help",
        'appt_type': 'In-Person',
        'appt_date': '2025-05-09',
        'appt_time': "09:00"
    })
    
    assert res.status_code == 302

def test_get_booking_page(client):
    """
    testing to see if booking page will get rendered
    """
    login(client, "ncao5@my.bcit.ca", "5678")

    res = client.get('/booking/7')

    assert b'Booking appointment with:' in res.data
    assert res.status_code == 200