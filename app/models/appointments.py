from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from db import db
from datetime import datetime, timedelta

class Appointments(db.Model):
    __tablename__ = "Appointments"

    id = db.mapped_column(db.Integer, primary_key=True)

    user_email = db.mapped_column(db.String, ForeignKey("Users.email"), nullable=False)
    user = relationship("Users", foreign_keys=[user_email], back_populates="appointments")

    advisor_id = db.mapped_column(db.Integer, ForeignKey("Users.id"), nullable=False)  # <-- MUST HAVE THIS
    advisor = relationship("Users", foreign_keys=[advisor_id], back_populates="advisor_appointments")

    date = db.mapped_column(db.Date, nullable=False)
    start_time = db.mapped_column(db.Time, nullable=False)
    end_time = db.mapped_column(db.Time, nullable=False)
    completed = db.mapped_column(db.Boolean, nullable=False, default=False)
    meeting_type = db.mapped_column(db.String, nullable=False)
    comment = db.mapped_column(db.String, nullable=True)

    @staticmethod
    def create_end_time(start_time):
        end_time = (datetime.strptime(str(start_time), "%H:%M") + timedelta(hours=1)).time()
        return end_time
    
    @staticmethod
    def create_appointment(user_email, advisor_id, date, start_time, end_time, meeting_type, comment=None):
        """ 
        Create a new appointment object
        """
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