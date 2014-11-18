import unittest

from .home_tests import MainBlueprintTest

main_tests = unittest.TestLoader().loadTestsFromTestCase(MainBlueprintTest)


view_tests = unittest.TestSuite([main_tests])

