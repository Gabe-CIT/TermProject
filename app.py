from flask import Flask
from app import auth_bp, main_bp, init_login_mgr

app = Flask(__name__)

app.secret_key = "1234"

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

init_login_mgr(app)

if __name__ == "__main__":
    app.run(port=8888, use_reloader=False)