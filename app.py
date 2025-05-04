from flask import Flask
from app import auth_bp, main_bp, init_login_mgr, book_bp

app = Flask(__name__)

app.secret_key = "1234"

# ADD ROUTES FROM ./app/controllers/<>_routes.py HERE!!!
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(book_bp)
init_login_mgr(app)

if __name__ == "__main__":
    app.run(port=8888, use_reloader=False)
