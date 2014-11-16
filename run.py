'''
Application runner scripts. Features ...
1. Wraps around Flask-Script
2. Includes Flask-Migrate

adds 
1. testing command
2. tools to initialize the sample app
'''
import unittest

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app


app = create_app('develop')
manager = Manager(app)

# This command adds sample data to the DB
from app.commands import SampleDataCommand
manager.add_command('sample-data', SampleDataCommand())

# This command runs the tests
from app.commands import TestingCommand
manager.add_command('test', TestingCommand)


# use flask migrate for DB migarations
from models import db
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()

