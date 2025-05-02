import json


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

def read_db():
    with open("./app/models/user_database.json", "r") as file:
        users = json.load(file)
        return users


def get_user_by_email(email):
    user_db = read_db()
    
    # return the user with the email_key of email param
    return user_db.get(email)

# just check if the POST'ed creds are valid entries in the pseudo database
def validate_credentials(email, password):
    user = get_user_by_email(email)
    
    if user and user["password"] == password:
        return True
    
    return False