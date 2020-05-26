'''
@ package utilities
Util class implementation
here we implement all common utilities

Example: self.util.getUniqueName()
'''
import logging
import utilities.custom_logger as cl
import time
import traceback
import random, string

class Util(object):

    log = cl.customLogger(logging.INFO)

    def verifyTextContains(self, actualText, expectedText):
        '''
        verify if actualText contains expectedText string
        '''
        self.log.info('Actual text from Application Web UI is: ' + actualText)
        self.log.info('Expected text from Application Web UI is: ' + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info('### VERIFICATION POSITIVE ! text contained')
            return True
        else:
            self.log.info('### VERIFICATION NEGATIVE ! text not contained')
            return False

    def verifyTextMatch(self, actualText, expectedText):
        '''
        verify if texts matches
        '''
        self.log.info('Actual text from Application Web UI is: ' + actualText)
        self.log.info('Expected text from Application Web UI is: ' + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info('### VERIFICATION POSITIVE ! texts matched')
            return True
        else:
            self.log.info('### VERIFICATION NEGATIVE ! texts unmatched')
            return False

    def sleep(self, sec, info=''):
        '''
        make the program to wait for few seconds
        '''
        if info is not None:
            self.log.info('Wait :: ' + str(sec) + ' seconds for: ' + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, lenght, type='letters'):
        '''
        get random string
        Parameters:
            lengt: length of string
            type (letters by default): for example lower/upper/digits
        '''
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_uppercase
        if type == 'upper':
            case = string.ascii_uppercase
        if type == 'digits':
            case = string.digits
        if type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(0,lenght))

    def getUniqueName(self, nameLenght):
        '''
        gets an unique name
        '''
        return self.getAlphaNumeric(nameLenght, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        '''
        gets a list of unique strings
        Parameters:
            listLenght by standard is 5
            itemLenght, e.g. if listLenght = 3 -> item Lenght = [2,4,7]
        '''
        nameList = []
        for i in range(0,listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyListContains(self, expectedList, actualList):
        '''
        verify if actualList contains expectedList
        '''
        for i in expectedList:
            if i not in actualList:
                return False
        else:
            return True

    def verifyListMatch(self, expectedList, actualList):
        '''
        verify if 2 lists match
        '''
        return set(expectedList) == set(actualList)