# !!! This file hierarchy looks a bit confusing, but PLEASE READ AHEAD TO HELP UNDERSTANDING !!!

## __init__.py
This file is just to help with importing. Since I am organizing everything into seperate modules for organization, defining our imports in __init__.py
makes life much easier for backend work. 

#### See term_project/app.py for example usage of __init__.py file.

### !!! NOTE FOR <>_routes.py FILES!!! (and probably other .py files located in the ./app/ folder) !!!
We can't use:

```py
from app import User, read_db, get_user_by_email, validate_credentials
```

as it would cause a circular import. In this case, we have to directly state what we are importing:

```py
from app.services.user_mgmt import validate_credentials, get_user_by_email
from app.services.login_mgmt import User
```

## ./app/controllers/
Files located here are just where we define routes, which is where we define pages on our website. (like localhost:8000/auth/login or localhost:8000/services)
There should be definitions for what the URL is for each route as well which you can shift+click on.

If a route is defined with pass, then the route will through an error when attempting to access the route VIA browser:
```py
@<route_name>.route("/example_route")
def example_route():
    pass
```

So don't get too worried if a route seems inacessible, it probably hasn't been defined yet.

## ./app/models/
Files located here are database related files. You can define SQL models/classes here, and we can access them using:
```py
from app.models.models import <class_name>
```

As of Sprint 1, there is a pseudo JSON database (user_database.json). In later sprints, a SQL database using SQLAlchemy should be implemented instead.

## ./app/services/
Files located here are mainly modules for organization and semantic sake. 

I did not want to define user management and login management all in the same file, so I've decided to use "modules" which
we can pull defined functions, classes, etc. from to make things easier to organize in our .py files for when the project continues to grow.

## Implementing routes into the app.py
Generally, we want to make sure our routes are handled in a seperate file, just in case something goes wrong in one file, the entire backend does not crumble (especially true if we were using a statically compiled language (JS in NodeJS) rather than an interpreted language (PY in Flask)).

#### Create a <>_routes.py file inside of ./app/controllers/<<route_name>>_routes.py. (route_name should be semantic to what the routes you will be defining are).
```bash
# for windows
New-Item ./app/controllers/dashboard_routes.py
```

```bash
# for linux (and probably macOS)
touch ./app/controllers/dashboard_routes.py
```

Once we have that, we want to register the file as a blueprint for routes

#### Import Blueprint from flask lib
```py
# import only Blueprint method from flask library (ONLY IMPORT WHAT YOU NEED!!!)
from flask import Blueprint
```

#### Register <>_routes.py as a blueprint for routes
```py
dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")
```

The name of the var that you assign Blueprint() to doesn't matter, but I follow a <>_bp naming convention.
- 1 parameter ("dashboard") > Name of the route
- 2 parameter (__name__) > Tells the <>_route.py module where it is in the file hierachy
- 3 parameter (url_prefix="/dashboard") > !!! OPTIONAL !!!; Tells flask to prepend "/dashboard" to every URL string (localhost:8000/dashboard/view_calendar)

#### Create your routes in your <>_routes.py
```py
@dashboard_bp.route("/view_calendar")
def view_calendar():
    pass # flask logic here
```

### Please read flask documentation to learn more about creating routes, or look through the controller modules to get an idea of what is going on.

#### Add blueprint to __init__.py
```py
from .controllers.modules.dashboard_routes import dashboard_bp
```

#### Import NEW blueprint and register blueprint in app.py
```py
from app import dashboard_bp # there will probably be many imports from app :)

app.register_blueprint(dashboard_bp)
```