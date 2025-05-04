from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

book_bp = Blueprint("booking", __name__, url_prefix="/booking")

@book_bp.route("/booking")
@login_required
def create_booking():
    return render_template("booking.html")