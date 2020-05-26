import unittest
from tests.home.login_tests import TestLogin
from tests.courses.register_courses_csv_data import RegisterMultiCoursesTests

# get all tests from test classes:
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterMultiCoursesTests)

# create a test suite combining all test cases
smokeTest = unittest.TestSuite([tc1, tc2])

# release text runner
unittest.TextTestRunner(verbosity=2,).run(smokeTest)