# CREATE PAGE OBJECT PATTERN
# stworz klase, ktora przyjmie driver i polaczy Twoj test z metodami z 'base'
# every page class should inherit from SeleniumDriver
from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # pages URLs
    _home_page = 'https://letskodeit.teachable.com/'
    _my_courses = "https://letskodeit.teachable.com/courses/enrolled"
    _all_courses = "https://letskodeit.teachable.com/courses"
    _practice = "https://letskodeit.teachable.com/p/practice"

    def navigateToHomePage(self):
        self.driver.get(self._home_page)
    def navigateToMyCourses(self):
        self.driver.get(self._my_courses)
    def navigateToAllCourses(self):
        self.driver.get(self._all_courses)
    def navigateToPractice(self):
        self.driver.get(self._practice)