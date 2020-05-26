from base.basepage import BasePage
from utilities import custom_logger as cl
import logging
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _all_courses = "//a[contains(text(),'All Courses')]"
    _search_box = "search-courses"
    _search_btn = "search-course-button"
    _course = "//div[contains(text(),'{0}')]"
    _enroll_btn = "enroll-button-top"
    _num_frame = '__privateStripeFrame12'
    _num_box = "//input[@aria-label='Numer karty płatniczej']"
    _exp_frame = '__privateStripeFrame13'
    _exp_box = "//input[@placeholder='MM / RR']"
    _cvc_frame = '__privateStripeFrame14'
    _cvc_box = "//input[@placeholder='Kod CVC']"
    _confirm_btn = 'confirm-purchase'

    #def clickAllCourses(self):
    #    self.clickElement(self._all_courses, locatorType='xpath')
    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType='id')
        self.clickElement(self._search_btn, locatorType='id')
        time.sleep(1)

    def selectCourseToEnroll(self, fullCourseName):
        self.clickElement(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickEnrollBtn(self):
        self.clickElement(self._enroll_btn, locatorType='id')

    def enterCardNum(self, num):
        self.switchToFrame(self._num_frame)
        time.sleep(1)
        self.sendKeys(num, self._num_box, locatorType='xpath')
        # self.switchFrameByIndex(self._num_box, locatorType='xpath')
        # self.sendKeysWhenReady(num, locator=self._num_box, locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(self._exp_frame)
        time.sleep(1)
        self.sendKeys(exp, self._exp_box, locatorType='xpath')
        # self.switchFrameByIndex(self._exp_box, locatorType='xpath')
        # self.sendKeysWhenReady(exp, locator=self._exp_box, locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardCvc(self, cvc):
        self.switchToFrame(self._cvc_frame)
        time.sleep(1)
        self.sendKeys(cvc, self._cvc_box, locatorType='xpath')
        # self.switchFrameByIndex(self._cvc_box, locatorType='xpath')
        # self.sendKeysWhenReady(cvc, locator=self._cvc_box, locatorType='xpath')
        self.switchToDefaultContent()

    def clickCheckBox(self):
        self.clickElement("agreed_to_terms_checkbox", locatorType='id')

    def enterCreditCard(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCvc(cvc)
        self.clickCheckBox()

    def enrollCourse(self, num='', exp='', cvc=''):
        self.clickEnrollBtn()
        self.util.sleep(4)
        self.scrollPage(800)
        self.enterCreditCard(num, exp, cvc)

    def verifyPurchaseBtn(self):
        result = self.isEnabled('confirm-purchase', locatorType='id', info='Enroll button')
        return not result