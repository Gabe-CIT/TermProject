from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from db import db
from app.models import Appointments, Users
from app.services.user_mgmt import is_student
from datetime import datetime, timedelta
from colorama import Fore
import resend

resend.api_key = "re_QENVUkg7_3qqudiajyvQyr2rqNzft5AEM"


book_bp = Blueprint("booking", __name__, url_prefix="/booking")

@book_bp.route("/<int:advisor_id>")
@login_required
# BOOKING ROUTE
def create_booking(advisor_id):
    selected_advisor = db.session.execute(db.select(Users).where(Users.id == advisor_id)).scalar()
    advisors = db.session.execute(db.select(Users).where(Users.role == "advisor")).scalars()
    return render_template("main/booking.html", advisors=advisors, selected_advisor=selected_advisor)

# form method to post appointment data to datatbase
@book_bp.route("/confirm", methods=["POST"])
@login_required
def confirm_booking():
    try:
        appt_date = datetime.strptime(request.form["appt_date"], "%Y-%m-%d").date()
        
        # Check if the date is a weekend
        if appt_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            flash("Appointments cannot be booked on weekends. Please choose a weekday.")
            advisor_id = request.form["appt_advisor"]
            return redirect(url_for("booking.create_booking", advisor_id=advisor_id))

        appt_start_time = datetime.strptime(request.form["appt_time"], "%H:%M").time()
        appt_type = request.form["appt_type"]
        advisor_id = request.form["appt_advisor"]

        # Check if an appointment already exists for the same advisor, date, and time
        existing_appt = db.session.execute(
            db.select(Appointments).where(
                (Appointments.advisor_id == advisor_id) &
                (Appointments.date == appt_date) &
                (Appointments.start_time == appt_start_time)
            )
        ).scalar()

        repeat_appt = db.session.execute(
            db.select(Appointments).where(
                (Appointments.date == appt_date) &
                (Appointments.start_time == appt_start_time)
            )
        ).scalar()

        if existing_appt:
            flash("This advisor already has an appointment at the selected time. Please choose a different time.")
            return redirect(url_for("booking.create_booking", advisor_id=advisor_id))
        
        if repeat_appt:
            flash("You already have another booking in the same time.")
            return redirect(url_for("booking.create_booking", advisor_id=advisor_id))

        appt_end_time = Appointments.create_end_time(request.form["appt_time"])
        user = db.session.execute(db.select(Users).where(Users.email == current_user.id)).scalar()
        user_email = user.email

        appt_comment = request.form.get('appt_purpose') or None

        new_appt = Appointments.create_appointment(
            user_email=user_email,
            advisor_id=advisor_id,
            date=appt_date,
            start_time=appt_start_time,
            end_time=appt_end_time,
            meeting_type=appt_type,
            comment=appt_comment
        )

        advisor = db.session.execute(db.select(Users).where(Users.id == advisor_id)).scalar()

        # params: resend.Emails.SendParams = {
        #     "from": "Acme <onboarding@resend.dev>",
        #     "to": ["delivered@resend.dev"],
        #     "subject": "Appointment Booked",
        #     "html": f"<p>Hello {user.name} {user.surname}, <br> This is a confimation email regarding your appointment. <br> You have booked an appointment with {advisor.name} {advisor.surname}. <br> Your appointment is on {appt_date} at {appt_start_time} - {appt_end_time}.</p>"
        # }

        # email = resend.Emails.send(params)

        db.session.add(new_appt)
        db.session.commit()
        print("\n" * 15 + Fore.GREEN + "Appointment created successfully!")
        # print(f"Email Info: {email}") # prints email id of resend email
        print(Fore.GREEN + "Sending appointment confirmation email..." + "\n" * 15)
        
        return redirect(url_for('dashboard.dashboard_redirect'))

    except Exception as e:
        print(Fore.RED + "\n" * 8 + f"ERROR: {e}" + "\n" * 8)
        return redirect(url_for("booking.create_booking", advisor_id=advisor_id))