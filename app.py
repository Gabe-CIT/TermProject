from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from data.manage_user import validate_credentials, get_user_by_email
from auth import User, init_login_mgr

app = Flask(__name__)
app.secret_key = "1220"

init_login_mgr(app) # our login manager, see auth.py for more details

# LOGIN ROUTE > 127.0.0.1:5000/login
@app.route("/login", methods=["GET", "POST"])
def login():
    # if the user is sending data to the /login page
    if request.method == "POST":
        email = request.form["email_address_data"]
        password = request.form["password_data"]
        
        if validate_credentials(email, password):
            # create a new user object
            user = User(email, get_user_by_email(email))
            
            # send user object into login_user, and stuff
            login_user(user)
            return redirect(url_for("services"))
        
        else:
            return "<h1>LOGIN FAILED</h1>", 401
        
    return render_template("login.html")

# LOGOUT ROUTE > 127.0.0.1:5000/logout
@app.route("/logout")
@login_required # just for integrity reasons, it feels weird to logout_user a user that isnt logged in
def logout():
    logout_user()
    return redirect(url_for("login"))

# SERVICES ROUTE > http://127.0.0.1:5000/services
@app.route("/services")
@login_required # make a route have the requirement of a user being auth'ed
def services():
    # we can access current_user attributes using current_user from flask_login
    print(current_user)
    return render_template("services.html")

if __name__ == "__main__":
    app.run()