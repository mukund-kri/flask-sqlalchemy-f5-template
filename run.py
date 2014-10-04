'''
Simple script to run the server in dev mode and to run tests.
'''
import unittest

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app


app = create_app('develop')
manager = Manager(app)

# for testing
@manager.command
def test():
    # unittest.main()
    print("running all tests")
    from tests import all_tests
    unittest.TextTestRunner().run(all_tests)


# use flask migrate for DB migarations
from models import db
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()

