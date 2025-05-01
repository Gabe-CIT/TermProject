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
    return render_template("services.html")

PORT = 8888
if __name__ == "__main__":
    app.run(debug=True, port=8888)