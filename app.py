from flask import Flask, render_template, redirect, url_for, request
from pathlib import Path
from db import db
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.instance_path = Path("./").resolve()

db.init_app(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    data = "this will be the data for our dashboard"
    return render_template("", data=data) # dashboard page


@app.route("/advisor_login")
def advisor_login():
    return render_template("")
    

@app.route("/try_advisor_login", methods=["GET", "POST"])
def logging_advisor():
    return redirect("")

@app.route("/cancel")
def cancel_page():
    return render_template("")


PORT = 8888
if __name__ == "__main__":
    app.run(debug=True, port=PORT)
