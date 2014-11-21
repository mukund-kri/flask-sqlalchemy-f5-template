import unittest
from flask.ext.script import Command

from tests import all_tests


class TestingCommand(Command):
    ''' Run tests '''

    def run(self):
        print("running all tests")
        unittest.TextTestRunner().run(all_tests)

