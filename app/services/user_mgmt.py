import json
from colorama import Fore

"""
what the pseudo database looks like:

{
    "ncao5@my.bcit.ca": {
        "password": "1234",
        "name": "Nick Cao",
        "role": "student"
    }
}

we can access a user (for now) using the email as a key, implement SQL later
"""

# !!! refactor this once SQLAlchemy is implemented
def read_db():
    with open("./app/models/user_database.json", "r") as file:
        users = json.load(file)
        return users

# !!! refactor this once SQLAlchemy is implemented
def get_user_by_email(email):
    user_db = read_db()
    
    # return the user with the email_key of email param
    return user_db.get(email)

# just check if the POST'ed credentials are valid entries in the pseudo database
def validate_credentials(email, password):
    user = get_user_by_email(email)
    
    if user and user["password"] == password:
        return True
    
    return False

# pretty simple, we are just cross referencing the user.role attribute to see what the string value is. 
# acceptable role string values: student / advisor
# we can handle logic for roles either in the <>_route.py, or by using/creating a service module (i prefer using a service module for modularity)
def is_student(email):
    user = get_user_by_email(email)
    
    if user and user["role"] == "student":
        return True
    
# you could probably make this into one function, but i like the semantics of two, even if it's redundant
def is_advisor(email):
    user = get_user_by_email(email)
    
    if user and user["role"] == "advisor":
        return False
