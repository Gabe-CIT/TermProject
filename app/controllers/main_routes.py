from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from db import db
from app.models import Users, Services

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
# make a route have the requirement of a user being auth'ed !!!TEMP BECAUSE GUEST USER SHOULD BE ABLE TO ACCESS SERVICES, PROMPT THEM TO LOGIN TO BOOK SERVICE
def services():
    services = db.session.execute(db.select(Services)).scalars()
    navs = db.session.execute(db.select(Services)).scalars()

    return render_template("services.html", services=services, navs=navs)

@main_bp.route("/cancel")
@login_required
def cancel_booking():
    return render_template('cancel.html') # cancellation page

@main_bp.route('/advisor')
def advisor_log_page():
    return render_template('advisor.html')

# filter out the advisors through this page
@main_bp.route("/services<int:service_id>")
@login_required # make a route have the requirement of a user being auth'ed !!!TEMP BECAUSE GUEST USER SHOULD BE ABLE TO ACCESS SERVICES, PROMPT THEM TO LOGIN TO BOOK SERVICE
def filter_services(service_id):
    advisors = db.session.execute(db.select(Users).where(Users.service_id == service_id)).scalars()
    return render_template("services.html", advisors=advisors)