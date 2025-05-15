import pytest
from app.models import Appointments
from datetime import datetime, timedelta

def test_create_end_time():
    # Test the create_end_time function with a sample start time
    start_time = "10:00"
    expected_end_time = datetime.strptime("11:00", "%H:%M").time()  # Expected end time after adding 1 hour
    result = Appointments.create_end_time(start_time)
    assert result == expected_end_time

def test_create_appointment():
    # Test the create_appointment function with sample data
    user_email = "test@email.com"
    advisor_id = 1
    date = datetime.strptime("2023-10-01", "%Y-%m-%d").date()
    start_time = datetime.strptime("10:00", "%H:%M").time()
    end_time = datetime.strptime("11:00", "%H:%M").time()
    meeting_type = "In-Person"
    comment = "Test appointment"

    appt = Appointments.create_appointment(
    user_email=user_email,
    advisor_id=advisor_id,
    date=date,
    start_time=start_time,
    end_time=end_time,
    meeting_type=meeting_type,
    comment=comment
)

    assert isinstance(appt, Appointments)
    assert appt.user_email == user_email
    assert appt.advisor_id == advisor_id
    assert appt.date == date
    assert appt.start_time == start_time
    assert appt.end_time == end_time
    assert appt.meeting_type == meeting_type
    assert appt.comment == comment