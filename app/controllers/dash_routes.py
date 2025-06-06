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

@dash_bp.route("/")
@login_required
def dashboard_redirect():
    user_email = current_user.id
        
    if not user_email:
        return redirect(url_for('main.error'))

    if is_student(user_email):
        return redirect(url_for('dashboard.student_dashboard', email=user_email))

    if is_advisor(user_email):
        advisor = db.session.execute(db.select(Users).where(Users.email == current_user.id))
        return redirect(url_for('dashboard.advisor_dashboard', advisor_id=advisor.id))        


@dash_bp.route("/student/<string:email>")
@login_required
def student_dashboard(email):
    """
    Student dashboard route
    Displays the student's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
    
    # Searches for appointments with same user email
    user_appointments = db.session.execute(db.select(Appointments).where(Appointments.user_email == email)).scalars()
    len_appts = list(db.session.execute(db.select(Appointments).where(Appointments.user_email == email)).scalars())
    return render_template("dash/student_dashboard.html", user=user, appts=user_appointments, appt_length=len_appts)

@dash_bp.route("/advisor/<string:email>")
@login_required
def advisor_dashboard(email):
    """
    Advisor dashboard route
    Displays the advisor's information and their appointments.
    """
    user = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
    user_appts = db.session.execute(db.select(Appointments).where(Appointments.advisor_id == user.id)).scalars()
    len_appts = list(db.session.execute(db.select(Appointments).where(Appointments.advisor_id == user.id)).scalars())
    return render_template("dash/advisor_dashboard.html", user=user, appts=user_appts, appt_length=len_appts)


# cancel booking route
@dash_bp.route("/cancel/<int:appt_id>")
@login_required
def cancel_appt(appt_id):
    appt = db.session.execute(db.select(Appointments).where(Appointments.id == appt_id)).scalar()

    db.session.delete(appt)
    db.session.commit()

    flash(f"Appointment has been canceled")
    return redirect(url_for('dashboard.dashboard_redirect'))

@dash_bp.route("/edit/<int:appt_id>", methods=["GET", "POST"])
@login_required
def edit_comment(appt_id):
    user = db.session.execute(db.select(Users).where(Users.email == current_user.id))
    appt = db.session.execute(db.select(Appointments).where(Appointments.id == appt_id)).scalar()

    if request.method == "POST":
        new_comment = request.form.get("comment")
        appt.comment = new_comment
        db.session.commit()
        flash("Appointment details updated.")
        return redirect(url_for("dashboard.dashboard_redirect"))

    return render_template("dash/student_edit.html", appt=appt, user=user)