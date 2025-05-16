from flask import Blueprint, render_template

error_bp = Blueprint("error_bp", __name__)

@error_bp.app_errorhandler(404)
def not_found(e):
    return render_template("testing/error.html", err_code=404, err_msg=e), 404