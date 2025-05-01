from db import db

class Advisors(db.Model):
    __tablename__ = 'Advisors'
    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    surname = db.mapped_column(db.String(50), nullable=False)
    service_id = db.mapped_column(db.Integer, db.ForeignKey("Services.id"), nullable=False)
    service = db.relationship("Services", back_populates="advisors")