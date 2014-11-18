import unittest


from .models import model_tests
from .views import view_tests

all_tests = unittest.TestSuite([model_tests, view_tests])
