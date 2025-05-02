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
