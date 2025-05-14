from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from db import db
from app.models import Appointments, Users, Services
from app.services.login_mgmt import User
from app.services.user_mgmt import is_student, is_advisor
from datetime import datetime, timedelta
from colorama import Fore 

dash_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")
# DASHBOARD ROUTE

"""
/dashboard
def func_name()
@login_required
- check for rule
    - check email

    - if student:
        - get student email@my.bcit.ca
        - redirect to /student/<string:email>

    if advisor:
        - get advisor email@bcit.ca
        - redirect to /advisor/<string:email>
"""

@dash_bp.route("/")
@login_required
def dashboard_redirect():
    user_email = current_user.id
        
    if not user_email:
        return redirect(url_for('main.error'))

    if is_student(user_email):
        return redirect(url_for('dashboard.student_dashboard', email=user_email))

    if is_advisor(user_email):
        return redirect(url_for('dashboard.advisor_dashboard', email=user_email))        


@dash_bp.route("/student/<string:email>")
@login_required
def student_dashboard(email):
    """
    Student dashboard route
    Displays the student's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
    if user is None:
        flash("User not found", "danger")
        return redirect(url_for("main.index"))
    if not is_student(user.email):
        flash("You are not authorized to access this page", "danger")
        return redirect(url_for("main.index"))
    
    # Searches for appointments with same user email
    user_appointments = db.session.execute(db.select(Appointments).where(Appointments.user_email == email)).scalars()
    len_appts = list(db.session.execute(db.select(Appointments).where(Appointments.user_email == email)).scalars())
    advisor = db.session.execute(db.select(Users).where(Users.id == Appointments.advisor_id)).scalar()
    return render_template("student_dashboard.html", user=user, appts=user_appointments, advisor=advisor, appt_length=len_appts)

@dash_bp.route("/advisor/<string:email>")
@login_required
def advisor_dashboard(email):
    """
    Advisor dashboard route
    Displays the advisor's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
    if user is None:
        flash("User not found", "danger")
        return redirect(url_for("main.index"))
    if not is_advisor(user.email):
        flash("You are not authorized to access this page", "danger")
        return redirect(url_for("main.index"))
    
    user_appts = db.session.execute(db.select(Appointments).where(Appointments.advisor_id == email)).scalars()

    return render_template("advisor_dashboard.html", user=user, appts=user_appts)


# cancel booking route
@dash_bp.route("/cancel/<int:appt_id>")
@login_required
def cancel_appt(appt_id):
    pass