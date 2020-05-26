from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import CheckStatus
import unittest
import pytest

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)

    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll('JavaScript for beginners')
        self.courses.enrollCourse('1111 2222 3333 4444', '1122', '123')
        result1 = self.courses.verifyPurchaseBtn()
        self.cs.markFinal("test_invalidEnrollment", result1, 'Checking Purchase Button')