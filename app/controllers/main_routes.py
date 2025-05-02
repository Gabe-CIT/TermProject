from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

main_bp = Blueprint("main", __name__)

# INDEX/HOME ROUTE > http://127.0.0.1:8888/
@main_bp.route("/")
def homepage():
    pass

# BOOKING ROUTE > http://127.0.0.1:8888/booking
@main_bp.route("/booking")
def booking():
    pass

# SERVICES ROUTE > http://127.0.0.1:8888/services
@main_bp.route("/services")
@login_required # make a route have the requirement of a user being auth'ed !!!TEMP BECAUSE GUEST USER SHOULD BE ABLE TO ACCESS SERVICES, PROMPT THEM TO LOGIN TO BOOK SERVICE
def services():
    # we can access current_user attributes using current_user from flask_login
    print(current_user)
    return render_template("services.html")
