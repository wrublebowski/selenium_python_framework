# ALLOWS US TO PERFORM FEW ASSERTS WITHOUT STOPPING TEST EXECUTION
# WE VERIFY FEW RESULTS (PASS OR FAILED) AND DO THE FINAL ASSERT

import logging
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl

class CheckStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        '''
        inits checkpoint class
        '''
        super(CheckStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result == True:
                    self.resultList.append("PASS")
                    self.log.info('### VERIFICATION SUCCESSFULL :: + '+ resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error('### VERIFICATION FAILED :: + ' + resultMessage)
                    self.screenShot(resultMessage)
            if result is None:
                self.resultList.append("FAIL")
                self.log.error('### VERIFICATION FAILED :: + ' + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error('### EXCEPTION OCCURRED!!!')
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):
        '''
        Mark the result of the verification point in a test case
        '''
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        '''
        mark the final result of the verification point in a test case
        use it at least once, as a final status of test case
        '''
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName +" ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFULL")
            self.resultList.clear()
            assert True == True