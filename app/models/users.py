from db import db

class Users(db.Model):
    __tablename__ = "Users"

    id = db.mapped_column(db.Integer, nullable=False, unique=True, primary_key=True) # use email as identifier
    name = db.mapped_column(db.String(50), nullable=False)
    surname = db.mapped_column(db.String(50), nullable=False)
    email = db.mapped_column(db.String(50), nullable=False, unique=True)
    password = db.mapped_column(db.String(100), nullable=False)
    role = db.mapped_column(db.String(20), nullable=False)  # e.g., "user", "admin", etc.

    # Relationship with Appointments
    appointments = db.relationship("Appointments",back_populates="user") 
    # Explicitly specify the foreign key relationship

    # relationship with Services
    service_id = db.mapped_column(db.Integer, db.ForeignKey("Services.id"), nullable=True)
    service = db.relationship("Services", back_populates="advisors")

    # relationship with Advisors
    # advisor_appointments = db.relationship("Appointments", back_populates="advisor")