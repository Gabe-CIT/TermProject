from db import db
from datetime import time, timedelta
from flask import request

class Appointments(db.Model):
    __tablename__ = "Appointments"

    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    
    # relationship between appointments and users
    user_id = db.mapped_column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    user = db.relationship("Users", back_populates="appointments")

    # relationship between appointments and advisors
    advisor_id = db.mapped_column(db.Integer, db.ForeignKey("Advisors.id"), nullable=False)
    advisor = db.relationship("Advisors", back_populates="advisor_appointments")

    # appointment attributes 
    day = db.mapped_column(db.Date, nullable=False)
    start_time = db.mapped_column(db.Time, nullable=False)
    end_time = db.mapped_column(db.Time, nullable=False)
    confirmed = db.mapped_column(db.Boolean, nullable=False, default=False)
    completed = db.mapped_column(db.Boolean, nullable=False, default=False)
    meeting_type = db.mapped_column(db.String, nullable=False)
    comment = db.mapped_column(db.String, nullable=True)
