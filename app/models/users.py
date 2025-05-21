from db import db

class Users(db.Model):
    __tablename__ = "Users"

    id = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    surname = db.mapped_column(db.String(50), nullable=False)
    email = db.mapped_column(db.String(50), nullable=False, unique=True)
    password = db.mapped_column(db.String(100), nullable=False)
    role = db.mapped_column(db.String(20), nullable=False)

    appointments = db.relationship(
        "Appointments",
        foreign_keys="Appointments.user_email",
        back_populates="user"
    )

    advisor_appointments = db.relationship(
        "Appointments",
        foreign_keys="Appointments.advisor_id",
        back_populates="advisor"
    )

    service_id = db.mapped_column(db.Integer, db.ForeignKey("Services.id"), nullable=True)
    service = db.relationship("Services", back_populates="advisors")