from db import db

class Advisors(db.Model):
    __tablename__ = 'Advisors'
    id = db.mapped_column(db.Integer, nullable=False, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    surname = db.mapped_column(db.String(50), nullable=False)

    # relationship between advisors and services
    service_id = db.mapped_column(db.Integer, db.ForeignKey("Services.id"), nullable=False)
    service = db.relationship("Services", back_populates="advisors")

    advisor_appointments = db.relationship("Appointments", back_populates="advisor")
    
    # string dunder method for advisors
    def __str__(self):
        return (f"Advisor info: \nID: {self.id} \nName: {self.name} {self.surname} \nService: {self.service}")