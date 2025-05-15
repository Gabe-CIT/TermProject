# this file is to be able to access all of the functions and classes and objects inside of app/ folder FROM other parts of the file hierachy
# this means, we only need to do "from app import main_bp" for example inside of app.py, instead of doing "from app.controllers.main_routes.py import main_bp"
# it just makes life simple, and we can be more lazy

# import routes
from .controllers.auth_routes import auth_bp
from .controllers.main_routes import main_bp
from .controllers.book_routes import book_bp
from .controllers.dash_routes import dash_bp

# import services
from .services.login_mgmt import User, init_login_mgr, load_user
from .services.user_mgmt import get_user_by_email, validate_credentials
from .models import Users, Appointments, Services