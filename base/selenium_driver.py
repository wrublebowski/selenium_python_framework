# OUR CUSTOM CLASS WITH DRIVER METHODS TO USE IN PAGE OBJECT PATTERN
# NO VARIABLE NAMES HERE - ONLY RAW METHODS

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import logging
import utilities.custom_logger as cl
import time
import os

class SeleniumDriver():

    # create logger here but copy as well to login_page.py to make logs instead of prints
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # to provide driver to class
        self.driver = driver

    def getByType(self, locatorType):

        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            self.log.info('locator type not supported!')
        return False

    def getElement(self, locator, locatorType="id"):
        '''
        Returns: element
        '''
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found with locator: ' + locator +
                          ' and locator type: ' + locatorType)
        except:
            self.log.info('Element not found with locator: ' + locator +
                          ' and locator type: ' + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        '''
        Returns: list of elements
        '''
        elementList = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            self.log.info('Element list found with locator: ' + locator +
                          ' and locator type: ' + locatorType)
        except:
            self.log.info('Element list not found with locator: ' + locator +
                          ' and locator type: ' + locatorType)
        return elementList

    def clickElement(self, locator='', locatorType="id", element=None):
        '''
        Click on element.
        Provide locator,locatorType or element itself
        '''
        try:
            if locator: # means locator is not empty!
                element= self.getElement(locator, locatorType)
            element.click() # if locator is empty just click element
            self.log.info("Clicked on element with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on element with locator: " + locator +
                          " and locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id", element=None):
        '''
        Sends keys to element.
        Provide data and locator,locatorType or element itself
        '''
        try:
            if locator: # means locator is not empty!
                element= self.getElement(locator, locatorType)
            element.send_keys(data) # if locator is empty just send data
            self.log.info("Data sent to element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data to element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def sendKeysWhenReady(self, data, locator="", locatorType="id"):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(10) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=10,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator, locatorType="id", element=None, info=''):
        '''
        Gets a 'Text' on element
        Provide locator,locatorType or element itself
        '''
        try:
            if locator: # means locator is not empty!
                self.log.debug('In locator condition')
                element = self.getElement(locator, locatorType)
            self.log.debug('Before finding text')
            text = element.text # method from Selenium
            self.log.debug('After finding text, length is: ' + str(len(text)))
            if len(text)==0:
                text = element.get_attribute('innerText')
            if len(text)!=0:
                self.log.info('Getting text on element ::' + info)
                self.log.info("Text of element is :: '" + text +"'")
                text = text.strip()
        except:
            self.log.error('Failed to get text on element:: ' + info)
            print_stack()
            text = None
        return text

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element
        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def isElementPresent(self, locator, locatorType='id', element=None):
        '''
        Check if element is present
        Provide locator,locatorType or element itself
        '''
        try:
            if locator: # means locator is not empty!
                element= self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is present with locator: " + locator +
                              " and locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element is NOT present with locator : " + locator +
                              " and locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType='id', element=None):
        '''
        Check if element is displayed
        Provide locator,locatorType or element itself
        '''
        isDisplayed = False
        try:
            if locator: # means locator is not empty!
                element= self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            else:
                self.log.info("Element is NOT displayed with locator : " + locator +
                              " and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def screenShot(self, resultMessage):
        '''
        Takes screenshot of a currently open web page
        '''

        # we create a path working on every computer
        fileName = resultMessage + '.' + str(round(time.time() * 1000)) + '.png'
        screenShotsDirectory = '../screenshots/'
        relativeFileName = screenShotsDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info('Screenshot saved to directory: ' + destinationFile)
        except:
            self.log.error("### Exception Occurred - taking screenshot")
        print_stack()

    def scrollPage(self, distance):
        '''
        Scrolls page for given distance
        For scrolling up: negative value e.g. -200
        '''
        self.driver.execute_script(f"window.scrollBy(0, {distance});")
        self.log.info(f'Scrolled by: {distance}')

    def getTitle(self):
        return self.driver.title

    def goToPage(self, www):
        return self.driver.get(www)

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        if name:
            self.driver.switch_to.frame(name)
        if index:
            self.log.info("Switch frame with index:")
            self.log.info(str(index))
            self.driver.switch_to.frame(index)

    def switchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iFrame index not found")
            return result

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()
