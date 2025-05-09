from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from db import db
from app.models import Appointments, Users
from app.services.user_mgmt import is_student
from datetime import datetime, timedelta

book_bp = Blueprint("booking", __name__, url_prefix="/booking")

@book_bp.route("/")
@login_required
# BOOKING ROUTE
def create_booking():
    advisors = db.session.execute(db.select(Users).where(Users.role == "advisor")).scalars()
    return render_template("booking.html", advisors=advisors)

# form method to post appointment data to datatbase
@book_bp.route("/confirm", methods=["POST"])
@login_required
def confirm_booking():
    # this is linking to the form on booking.html
    # need to update that html to allow for form posting
    # get the data from the form
    appt_date = datetime.strptime(request.form["appt_date"], "%Y-%m-%d")
    # convert the string to a date object
    appt_start_time = datetime.strptime(request.form["appt_time"], "%H:%M").time()
    # convert the string to a time object
    
    appt_type = request.form["appt_type"]
    advisor_id = request.form["appt_advisor"] # output advisor id from the form


    # get the user id from the current user
    appt_end_time = Appointments.create_end_time(request.form["appt_time"]) # 1-hour-long appointment

    user = db.session.execute(db.select(Users).where(Users.email == current_user.id)).scalar()
    user_email = user.email  # get the user id from the current user
    
    # optional comment
    if request.form['appt_purpose']:
        appt_comment = request.form['appt_purpose']
    else:
        appt_comment = None

    # create new apponitment object
    new_appt = Appointments.create_appointment(
        user_email=user_email, # user email from the current user
        advisor_id=advisor_id, # advisor id from the form
        date=appt_date, # date from the form
        start_time=appt_start_time, # start time from the form
        end_time=appt_end_time, # end time from the form
        meeting_type=appt_type, # appointment type from the form
        comment=appt_comment # comment from the form
    )

    db.session.add(new_appt)
    db.session.commit()
    print("Appointment created successfully!")
    print("Sending appointment confirmation email...")
    return redirect(url_for("main.homepage"))

# BOOKING ROUTE > http://127.0.0.1:8888/booking/schedule
@book_bp.route("/schedule")
def schedule():
    return render_template("schedule.html")