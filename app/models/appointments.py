from db import db
from datetime import datetime, timedelta
from flask import request

class Appointments(db.Model):
    __tablename__ = "Appointments"

    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    
    # relationship between appointments and users
    user_email = db.mapped_column(db.Integer, db.ForeignKey("Users.email"), nullable=False)
    user = db.relationship("Users", back_populates="appointments")

    # relationship between appointments and advisors
    advisor_id= db.mapped_column(db.Integer, nullable=False, unique=True)
    # advisor = db.relationship("Users", back_populates="advisor_appointments")

    # appointment attributes 
    date = db.mapped_column(db.Date, nullable=False)
    start_time = db.mapped_column(db.Time, nullable=False)
    end_time = db.mapped_column(db.Time, nullable=False)
    confirmed = db.mapped_column(db.Boolean, nullable=False, default=False)
    completed = db.mapped_column(db.Boolean, nullable=False, default=False)
    meeting_type = db.mapped_column(db.String, nullable=False)
    comment = db.mapped_column(db.String, nullable=True)

    @staticmethod
    def create_end_time(start_time):
        # Create an end time based on the start time and duration
        end_time = (datetime.strptime(str(start_time), "%H:%M") + timedelta(hours=1)).time()
        return end_time
    
    @staticmethod
    def create_appointment(user_email, advisor_id, date, start_time, end_time, meeting_type, comment=None):
        # Create a new appointment object
        new_appt = Appointments(
            user_email=user_email,
            advisor_id=advisor_id,
            date=date,
            start_time=start_time,
            end_time=end_time,
            meeting_type=meeting_type,
            comment=comment
        )
        return new_appt
    
    def get_appointments_by_user(user_id):
        # Get all appointments for a specific user
        return db.session.execute(db.select(Appointments).where(Appointments.user_id == user_id)).scalars().all()
    
    def get_appointments_by_advisor(advisor_id):
        # Get all appointments for a specific advisor
        return db.session.execute(db.select(Appointments).where(Appointments.advisor_id == advisor_id)).scalars().all()
    
    def get_appointments_by_date(date):
        # Get all appointments for a specific date
        return db.session.execute(db.select(Appointments).where(Appointments.date == date)).scalars().all()
    