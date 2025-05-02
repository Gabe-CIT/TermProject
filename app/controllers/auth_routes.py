from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, login_user
from app.services.user_mgmt import validate_credentials, get_user_by_email
from app.services.login_mgmt import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# LOGIN ROUTE > 127.0.0.1:8888/auth/login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # if the user is sending data to the /login page via the forms
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]
        
        if validate_credentials(email, password):
            # create a new user object
            user = User(email, get_user_by_email(email))
            
            # send user object into login_user, and stuff
            login_user(user)
            return redirect(url_for("main.services"))
        
        else:
            return "<h1>LOGIN FAILED</h1>", 401 # pls make an error page for me to send data into ty
        
    return render_template("login.html")

# LOGOUT ROUTE > 127.0.0.1:8888/auth/logout
@auth_bp.route("/logout")
@login_required # just for integrity reasons, it feels weird to logout_user a user that isnt logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))