from flask_login import LoginManager, UserMixin
from flask import Flask
from app.services.user_mgmt import *
from colorama import Fore

login_manager = LoginManager()

# inheriting from UserMixin to get default
# implementations of is_authenticated, is_active, is_anonymous, and get_id()
# https://flask-login.readthedocs.io/en/latest/#your-user-class
class User(UserMixin):
    def __init__(self, email, data):
        self.id = email
        self.name = data.name
        self.surname = data.surname
        self.password = data.password
        self.role = data.role
        
    def __repr__(self):
        return Fore.BLUE + f"""
        !!! User Data Printed !!!
        
        Email: {self.id} (stored as self.id)
        Name: {self.name} (stored as self.name)
        Password: {self.password} (stored as self.password)
        Role: {self.role} (stored as self.role)
        
        !!! For more information, check ./data/user_database.json to see how pseudo database works. !!!
        """ + Fore.RESET

# type hint that we want the app to a Flask instance (app: Flask)
def init_login_mgr(app: Flask):
    login_manager.init_app(app)
    login_manager.login_view = "auth.student_login" 
    
# we must return User object or None
@login_manager.user_loader 
def load_user(user_id):
    try:
        # user_id will be the email for now. user_id must be a str ID. we need to return a user OBJ
        user_data = get_user_by_email(user_id)
        
        if user_data:
            return User(user_id, user_data)
        
        return None
    
    except Exception as e:
        print(e)
