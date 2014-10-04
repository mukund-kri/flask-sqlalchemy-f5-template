import unittest

from .simple_model_tests import SimpleModelTest

sm_tests = unittest.TestLoader().loadTestsFromTestCase(SimpleModelTest)


model_tests = unittest.TestSuite([sm_tests])
