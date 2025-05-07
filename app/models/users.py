from db import db

class Users(db.Model):
    __tablename__ = "Users"

    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    surname = db.mapped_column(db.String(50), nullable=False)
    email = db.mapped_column(db.String(50), nullable=False, unique=True)
    password = db.mapped_column(db.String(100), nullable=False)

    # Relationship with Appointments
    appointments = db.relationship("Appointments",back_populates="user") 
    # Explicitly specify the foreign key relationship