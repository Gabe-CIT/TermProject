import pytest
from application import application  # Import your Flask app
from flask import Flask
from db import db
from app.models import Appointments, Users
from datetime import datetime

@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client
