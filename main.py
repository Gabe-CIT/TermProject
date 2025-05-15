from flask import Flask
from db import db
from pathlib import Path
from app import auth_bp, main_bp, init_login_mgr, book_bp, dash_bp

application = Flask(__name__)


# Configure your app (e.g., database URI)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# This will make Flask store the database file in the path provided, if there is no file, then this will create the .db file at the specified location
application.instance_path = Path("./").resolve()

# Initialize the db instance with the app
db.init_app(application)

application.secret_key = "1234"

# ADD ROUTES FROM ./app/controllers/<>_routes.py HERE!!!
application.register_blueprint(auth_bp)
application.register_blueprint(main_bp)
application.register_blueprint(book_bp)
application.register_blueprint(dash_bp)
init_login_mgr(application)


if __name__ == "__main__":
    application.run(debug=True, port=8888)
