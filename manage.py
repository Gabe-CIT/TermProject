from db import db
from app import models
from application import application
import csv

def create():
    db.create_all()
    print("Created Database")

# this function is used to import pre-made csv data to populate the database with user data
def import_users():
    try:
        # reads the files
        with open("./data/users.csv", 'r') as file:
            data = csv.DictReader(file)


            for row in data:
                name_data = row['name']
                surname_data = row["surname"]
                email_data = row['email']
                password_data = row['password']

                # creates a new user with columns filled
                user = models.Users(name=name_data, surname=surname_data, email=email_data, password=password_data)

                db.session.add(user)

            db.session.commit()
            # commits all users into the database

            print("Imported User Data")
    except Exception as e:
        print(f"Error importing users: {e}")

def import_services():
    try:
        with open("./data/services.csv", 'r') as file:
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
def import_advisors():
    try:
        with open("./data/advisors.csv", 'r') as file:
            data = csv.DictReader(file)

            for row in data:
                name_data = row['name']
                surname_data = row['surname']
                service_id = row['service_id']

                advisor = models.Advisors(name=name_data, surname=surname_data, service_id=service_id)

                db.session.add(advisor)
            db.session.commit()
        print("Imported Advisors")
    except Exception as e:
        print(f"Error importing advisors: {e}")

def drop():
    db.drop_all()
    print("Dropped Database")

if __name__ == "__main__":
    with application.app_context():
        drop()
        create()
        import_users()
        import_services()
        import_advisors()