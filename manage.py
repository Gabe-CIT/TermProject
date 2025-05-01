from db import db
import models
from app import app
import csv

def create():
    db.create_all()
    print("Created Database")

def import_data():
    with open("users.csv", 'r') as data:
        reader = csv.reader(data)

    for row in reader:
        name_data = row['name']
        surname_data = row['surename']
        email_data = row['email']

        user = models.Users()

        db.session.add()


    
    pass

def drop():
    db.drop_all()
    print("Dropped Database")

if __name__ == "__main__":
    with app.app_context():
        drop()
        create()