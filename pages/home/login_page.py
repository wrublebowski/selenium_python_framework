# CREATE PAGE OBJECT PATTERN
# stworz klase, ktora przyjmie driver i polaczy Twoj test z metodami z 'base'
# every page class should inherit from SeleniumDriver
from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class LoginPage(BasePage):
    # create instance of Page Object Model
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # implement locators (any kind):
    _login_button = "//a[@href='/sign_in']"
    _email_field = "user_email"
    _password_field = "user_password"
    _submit_button = "commit"
    _profile_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _logout_link = "//div[@id='navbar']//a[contains(text(),'Log Out')]"

    # quickly find element and click/send keys:
    def clickLoginButton(self):
        self.clickElement(self._login_button, locatorType='xpath')
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='id')
    def enterPassword(self,password):
        self.sendKeys(password,self._password_field, locatorType='id')
    def clickSubmitButton(self):
        self.clickElement(self._submit_button, locatorType='name')

    # aaaaand, ACTION!
    def login(self, email='', password=''):

        self.clickLoginButton()
        self.clearFields()
        self.enterEmail(email)
        self.util.sleep(0.5)
        self.enterPassword(password)
        self.util.sleep(0.5)
        self.clickSubmitButton()

    def verifySuccessLogin(self):
        successBulian = self.isElementPresent("//li[@class='dropdown']", locatorType='xpath')
        return successBulian

    def verifyFailLogin(self):
        failBulian = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]", locatorType='xpath')
        return failBulian

    def clearFields(self):
        self.getElement(self._email_field, locatorType='id').clear()
        self.getElement(self._password_field, locatorType='id').clear()

    def verifyLoginPageTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.clickElement(self._profile_icon, 'xpath')
        logoutLink = self.waitForElement(locator=self._logout_link, locatorType='xpath', pollFrequency=1,)
        self.clickElement(element=logoutLink)