'''
We implement a WebDriverFactory class with browser given
We use getWebDriver.. method to return driver and perform driver methods on page
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
'''
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        '''
        Creates webdriver instance, based on given browser

        :return: 'webdriver instance'
        '''
        if self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            # set chrome driver
            chromedriver = "C:/Users/Lenovo/workspace_python/drivers/chromedriver"
            os.environ['webdriver.chrome.driver'] = chromedriver
            driver = webdriver.Chrome()
        elif self.browser == 'ie':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(6)
        return driver