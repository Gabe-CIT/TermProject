from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, login_user
from app.services.user_mgmt import validate_credentials, get_user_by_email, is_advisor
from app.services.login_mgmt import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

"""
This file is for routes that are related to authentication, like LOGIN and LOUGOUT.

Generally, we don't want to put anything in here besides LOGIN and LOGOUT.
"""

# LOGIN ROUTE > 127.0.0.1:8888/auth/login
@auth_bp.route("/login", methods=["GET", "POST"])
def student_login():
    # if the user is sending data to the /login page via the forms
    print("Request method: " + request.method)
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]
        
        next_page = request.args.get("next")
        
        if validate_credentials(email, password):
            user_data = get_user_by_email(email)
            
            # safeguard to prevent other roles from using student_login
            if user_data["role"] != "student":
                return "<h1>Error! Login through the Advisor login page</h1>"
            
            # create a new user object
            user = User(email, user_data)
            
            # send user object into login_user, and stuff
            login_user(user)
            
            if next_page:
                return redirect(next_page)
            
            return redirect(url_for("main.homepage"))
        
        else:
            return "<h1>LOGIN FAILED</h1>", 401 # pls make an error page for me to send data into ty
    
    # return statement IF user sends a GET request
    return render_template("student_login.html")

@auth_bp.route("/advisor_login", methods=["GET", "POST"])
def advisor_login():
    # if the user is sending data to the /login page via the forms
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]
        
        next_page = request.args.get("next")
        
        if validate_credentials(email, password):
            user_data = get_user_by_email(email)
            
            # safeguard to prevent other roles from using student_login
            if user_data["role"] != "advisor":
                return "<h1>Error! Login through the Student login page</h1>"
            
            # create a new user object
            user = User(email, user_data)
            
            # send user object into login_user, and stuff
            login_user(user)
            
            if next_page:
                return redirect(next_page)
            
            return redirect(url_for("main.homepage"))
        
        else:
            return "<h1>LOGIN FAILED</h1>", 401 # pls make an error page for me to send data into ty
    
    # return statement IF user sends a GET request
    return render_template("advisor_login.html")

# LOGOUT ROUTE > 127.0.0.1:8888/auth/logout
@auth_bp.route("/logout")
@login_required # just for integrity reasons, it feels weird to logout_user a user that isnt logged in
def logout():
    logout_user()
    return redirect(url_for("auth.student_login"))