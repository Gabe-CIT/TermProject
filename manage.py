from db import db
from app import models
from main import application
import csv

def create():
    db.create_all()
    print("Created Database")

# this function is used to import pre-made csv data to populate the database with user data
def import_users():
    try:
        # reads the files
        with open("./app/data/users.csv", 'r') as file:
            data = csv.DictReader(file)


            for row in data:
                name_data = row['name']
                surname_data = row["surname"]
                email_data = row['email']
                password_data = row['password']
                role_data = row['role']
                service_data = row['service_id']

                # creates a new user with columns filled
                user = models.Users(
                    name=name_data, 
                    surname=surname_data,
                    email=email_data, 
                    password=password_data, 
                    role=role_data, 
                    service_id=service_data
                    )

                db.session.add(user)

            db.session.commit()
            # commits all users into the database

            print("Imported User Data")
    except Exception as e:
        print(f"Error importing users: {e}")

def import_services():
    try:
        with open("./app/data/services.csv", 'r') as file:
            data = csv.DictReader(file)


            for row in data:
                name_data = row["name"]
                description = row['description']

                service = models.Services(name=name_data, description=description)

                db.session.add(service)

            db.session.commit()
        print("Imported Services")
    except Exception as e:
        print(f"Error importing services: {e}")

# this function is used to import pre-made csv data to populate the database with advisor data

def drop():
    db.drop_all()
    print("Dropped Database")

if __name__ == "__main__":
    with application.app_context():
        drop()
        create()
        import_users()
        import_services()