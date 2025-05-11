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

@dash_bp.route("/student/<int:ID>")
@login_required
def student_dashboard(ID):
    """
    Student dashboard route
    Displays the student's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.id == ID)).scalar()
    if user is None:
        flash("User not found", "danger")
        return redirect(url_for("main.index"))
    if not is_student(user.email):
        flash("You are not authorized to access this page", "danger")
        return redirect(url_for("main.index"))
    
    user_appointments = db.session.execute(db.select(Appointments).where(Appointments.user_id == ID)).scalars()

    return render_template("student_dashboard.html", user=user, appointments=user_appointments)

@dash_bp.route("/advisor/<int:ID>")
@login_required
def advisor_dashboard(ID):
    """
    Advisor dashboard route
    Displays the advisor's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.id == ID)).scalar()
    if user is None:
        flash("User not found", "danger")
        return redirect(url_for("main.index"))
    if not is_advisor(user.email):
        flash("You are not authorized to access this page", "danger")
        return redirect(url_for("main.index"))
    
    user_appointments = db.session.execute(db.select(Appointments).where(Appointments.advisor_id == ID)).scalars()

    return render_template("advisor_dashboard.html", user=user, appointments=user_appointments)