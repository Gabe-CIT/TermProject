from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

main_bp = Blueprint("main", __name__)

"""
These routes are for pages that don't technically fall under any category of page. 

For example, /login page fall under auth_routes, however, /homepage page wouldn't fall under any category, so we place /homepage here.
"""

# INDEX/HOME ROUTE > http://127.0.0.1:8888/
@main_bp.route("/")
def homepage():
    return render_template("index.html")

# BOOKING ROUTE > http://127.0.0.1:8888/schedule
@main_bp.route("/schedule")
def schedule():
    return render_template("schedule.html")

# SERVICES ROUTE > http://127.0.0.1:8888/services
@main_bp.route("/services")
@login_required # make a route have the requirement of a user being auth'ed !!!TEMP BECAUSE GUEST USER SHOULD BE ABLE TO ACCESS SERVICES, PROMPT THEM TO LOGIN TO BOOK SERVICE
def services():
    # we can access current_user attributes using current_user from flask_login
    print(current_user)
    return render_template("services.html")

@main_bp.route("/cancel")
@login_required
def cancel_booking():
    return render_template('cancel.html') # cancellation page

@main_bp.route('/advisor')
def advisor_log_page():
    return render_template('advisor.html')
