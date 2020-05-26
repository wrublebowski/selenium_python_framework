# HERE WE JUST RUN TEST SCENARIOS AND COMBINE FIXTURES FROM CONFTEST
# FIXTURES CONSTRUCTED HERE ARE ABOUT login_tests.py ONLY!!!

from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import CheckStatus
from pages.home.navigation_page import NavigationPage

# unittest.TestCase to make it a test case
@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.cs = CheckStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    # @pytest.fixture()
    # def methSetUp(self, setUp):

    @pytest.mark.run(order=2)
    def test_ValidLogin(self):
        self.nav.navigateToHomePage()
        self.lp.login('test@email.com', 'abcabc')
        result1 = self.lp.verifyLoginPageTitle()
        self.cs.mark(result1, 'We verify title... ###')
        result2 = self.lp.verifySuccessLogin()
        self.cs.markFinal('test_ValidLogin', result2, 'We test correct login/password ###')

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.logout()
        self.lp.login('andrzej@gmail.com', 'gunwo')
        result0 = self.lp.verifyFailLogin()
        self.cs.markFinal('test_InvalidLogin', result0, 'We test wrong login/password ###')