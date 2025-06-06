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


# SERVICES ROUTE > http://127.0.0.1:8888/services
@main_bp.route("/services")
# make a route have the requirement of a user being auth'ed !!!TEMP BECAUSE GUEST USER SHOULD BE ABLE TO ACCESS SERVICES, PROMPT THEM TO LOGIN TO BOOK SERVICE
def services():
    """
    flask route to access services page
    it will query all services and will be able to access each service name and each advisor in every service
    """
    services = db.session.execute(db.select(Services)).scalars()
    navs = db.session.execute(db.select(Services)).scalars()
    # used 2 differnet variables since we needed 2 different for loops

    return render_template("main/services.html", services=services, navs=navs)