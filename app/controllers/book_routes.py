from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

book_bp = Blueprint("booking", __name__, url_prefix="/booking")

@book_bp.route("/")
@login_required
def create_booking():
    return render_template("booking.html")

# form method to post appointment data to datatbase
@book_bp.route("/confirm", methods=["POST"])
@login_required
def confirm_booking():
    # this is linking to the form on booking.html
    # need to update that html to allow for form posting
    
    pass

# BOOKING ROUTE > http://127.0.0.1:8888/schedule
@book_bp.route("/schedule")
def schedule():
    return render_template("schedule.html")