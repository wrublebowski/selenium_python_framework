from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import CheckStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVdata
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class RegisterMultiCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    # we provide getCSVdata method as *args
    @data(*getCSVdata('C:/Users/Lenovo/workspace_python/probastrony/testdata.csv'))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvc):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCvc)
        result1 = self.courses.verifyPurchaseBtn()
        self.cs.markFinal("test_invalidEnrollment", result1,
                          'Checking Purchase Button')