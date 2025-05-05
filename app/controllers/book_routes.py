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
    pass