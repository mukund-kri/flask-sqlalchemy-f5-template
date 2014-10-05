# A simple Flask template #

This is a simple template for creating modular applications with flask. It uses SQLAlchemy for DB access. 
Blueprints are used for modularity. It also includes the full Zurb Foundation 5 css & js.

### Main Features ###

 1. Flask 
 2. SQLAlchemy
 3. Foundation 5 (for frontend)
 
### Also uses ###

 1. Flask-Script
 2. Flask-Testing
 3. Flask-Migrate
 
### How to use this project ###

 1. Clone to project folder
 2. use "python run.py runserver" to run you app in development mode
 3. use "python run.py test" to run your test cases
 2. Write your models in [project folder]/models
 3. Write your model tests in [project folder]/tests/models
 4. Add blueprints to in the root folder. Look at [project folder]/home for examples
 5. Write templates which extend from base.html for foundation 5 look and feel

### TODO ###

 1. Convert this into a cookiecutter template
 2. Put a setup.py for dependencies
