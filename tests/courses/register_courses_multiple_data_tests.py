from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import CheckStatus
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class RegisterMultiCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)

    # we provide multiple data 'packs' as tuples (watch the order!) which we unpack
    @data(('JavaScript for beginners', '1111 2222 3333 4444', '1122', '123'),
          ("Learn Python 3 from scratch", '5555 6666 7777 8888', '0722', '666'))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvc):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCvc)
        result1 = self.courses.verifyPurchaseBtn()
        self.cs.markFinal("test_invalidEnrollment", result1,
                          'Checking Purchase Button')
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()