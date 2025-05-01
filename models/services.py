from db import db

class Services(db.Model):
    __tablename__ = "Services"

    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    description = db.mapped_column(db.String, nullable=True)
    advisors = db.relationship("Advisors", back_populates="service")