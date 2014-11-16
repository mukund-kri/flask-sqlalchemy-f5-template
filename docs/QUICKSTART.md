# Quick Start #

To get the sample app up and running, follow these steps ...

 1. Clone to project folder. cd into the newly cloned folder.
 1. Install all python dependencies by running inside a virtualenv
    > pip install -r requeirment.txt
 1. Create sample records in the sample database with the following command
    > python run.py sample-data
 1. Finally run the app with dev server
    > python run.py runserver
	opening url http://localhost:5000/ with a web browser should show home page of the sample app.

## Notes ##
 1. run.py is a script that wraps around Flask-Script to automate dev tasks like running
    the dev server, db migrations etc.

