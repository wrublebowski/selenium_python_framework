'''
@package base
BasePage class implementation. BasePage inherits from SeleniumDriver!
Here we implement all methods which are common to all pages in webapp

IMPORTANT: this class needs to be inherited by every page class
            this should not be used by creating object instances
Example: class LoginPage(BasePage)
'''
from base.selenium_driver import SeleniumDriver
from utilities.util import Util
from traceback import print_stack

class BasePage(SeleniumDriver):
    def __init__(self, driver):
        '''
        inits BasePage class
        returns None
        '''
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        '''
        Verifies the page title
        Parameters: titleToVerify
        '''
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error('Failed to get page title')
            print_stack()