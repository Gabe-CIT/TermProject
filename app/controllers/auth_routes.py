from flask import Blueprint, render_template, redirect, url_for, request, Response
from flask_login import login_required, logout_user, login_user, current_user
from app.services.user_mgmt import validate_credentials, get_user_by_email, is_advisor, is_student
from app.services.login_mgmt import User

from colorama import Fore

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

"""
This file is for routes that are related to authentication, like LOGIN and LOUGOUT.

Generally, we don't want to put anything in here besides LOGIN and LOGOUT.
"""

@auth_bp.route("/login_dashboard")
def login_dashboard():
    """
    This is for the Student Login button in the header.\n
    if user is currently logged in, then it redirects to dashboard, if not logs in and redirects to homepage
    """
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard_redirect", email=current_user.id))
    
    return redirect(url_for('auth.student_login'))
        
# LOGIN ROUTE > 127.0.0.1:8888/auth/login
@auth_bp.route("/login", methods=["GET", "POST"])
def student_login():
    # If the user is sending data to the /login page via the forms
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]

        # Get 'next' from the form data (for POST requests)
        next_page = request.form.get("next")
        # print(Fore.BLUE, "GRAB ME:", next_page, Fore.RESET)

        if validate_credentials(email, password) == True:
            
            if not is_student(email):
                return render_template("auth/student_login.html", error_code=403, error_msg="You are not authorized to use student login portal!")
            
            user_data = get_user_by_email(email)

            # Create a new user object
            user = User(email, user_data)

            # Send user object into login_user
            login_user(user)

            if next_page and next_page != "/auth/logout":
                print(Fore.GREEN, "auth_routes.py: Login successful! Redirecting...", Fore.RESET)
                return redirect(next_page)

            print(Fore.GREEN, "auth_routes.py: Login successful! Redirecting...", Fore.RESET)
            return redirect(url_for("main.homepage"))
        
        else:
            return render_template("auth/student_login.html", error_code=404, error_msg="Invalid credentials! Please check email or password again!")

    # Return statement IF user sends a GET request
    return render_template("auth/student_login.html")

@auth_bp.route("/advisor_login", methods=["GET", "POST"])
def advisor_login():
    # If the user is sending data to the /login page via the forms
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]

        # Get 'next' from the form data (for POST requests)
        next_page = request.form.get("next")
        # print(Fore.BLUE, "GRAB ME:", next_page, Fore.RESET)

        if validate_credentials(email, password) == True:
            
            if not is_advisor(email):
                return render_template("auth/advisor_login.html", error_code=403, error_msg="You are not authorized to use advisor login portal!")
            
            user_data = get_user_by_email(email)

            # Create a new user object
            user = User(email, user_data)

            # Send user object into login_user
            login_user(user)

            if next_page and next_page != "/auth/logout":
                print(Fore.GREEN, "auth_routes.py: Login successful! Redirecting...", Fore.RESET)
                return redirect(next_page)

            print(Fore.GREEN, "auth_routes.py: Login successful! Redirecting...", Fore.RESET)
            return redirect(url_for("main.homepage"))
        
        else:
            return render_template("auth/advisor_login.html", error_code=404, error_msg="Invalid credentials! Please check email or password again!")

    # Return statement IF user sends a GET request
    return render_template("auth/advisor_login.html")

# LOGOUT ROUTE > 127.0.0.1:8888/auth/logout
@auth_bp.route("/logout")
@login_required # just for integrity reasons, it feels weird to logout_user a user that isnt logged in
def logout():
    logout_user()
    return redirect(url_for("main.homepage"))

#  FORGOT PASSWORD ROUTE > 127.0.0.1:8888/auth/forgot
@auth_bp.route('/forgot')
def forgot_pass():
    """
    IM GOING TO BE REFACTORING THE ENTIRE FILE HIERARCHY, IT IS JUST A MESS TO LOOK AT
    A COMPLETE EYE SORE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    
    return render_template("auth/forgot_password.html")