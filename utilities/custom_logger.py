import inspect
import logging

def customLogger(logLevel=logging.DEBUG):

    # use inspect.stack to get name of the class/method from source
    loggerName = inspect.stack()[1][3]

    # create a variable to get new logger
    # set logging level on DEBUG by default: to get all kind of messages
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # create instance of FileHandler(name, mode = 'w' or 'a')
    # set logging level of filehandler to users choice
    fileHandler = logging.FileHandler('automation.log', mode='a')
    fileHandler.setLevel(logLevel)

    # define the formatter for fileHandler
    # add handler to logger
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                            datefmt="%d/%m/%Y %H:%M:%S")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger