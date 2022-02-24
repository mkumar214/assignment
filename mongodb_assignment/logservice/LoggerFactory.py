import logging
from utils.AppConfig import AppConfigUtils as au
class LoggerFactory(object):

    _LOG = None

    @staticmethod
    def __create_logger(log_file, log_lvl, log_format,date_format):
        """
        A private method that interact with python logservice module
        """
        # set the logservice format
        #log_format = "%(asctime)s:%(levelname)s:%(message)s"

        # Initialize the class variable with logger object
        LoggerFactory._LOG = logging.getLogger(log_file)
        logging.basicConfig(level=logging.INFO, format=log_format, datefmt=date_format)

        # set the logging level based on the user selection
        if log_lvl == "INFO":
            LoggerFactory._LOG.setLevel(logging.INFO)
        elif log_lvl == "ERROR":
            LoggerFactory._LOG.setLevel(logging.ERROR)
        elif log_lvl == "DEBUG":
            LoggerFactory._LOG.setLevel(logging.DEBUG)
        return LoggerFactory._LOG

    @staticmethod
    def getLogger(log_file):
        """
        A static method called by other modules to initialise logger in their own module
        """
        logconfig = au.getLogConfig()
        print(logconfig)
        logger = LoggerFactory.__create_logger(log_file, logconfig['log_level'], logconfig['log_format'], logconfig['date_fmt'])
        # return the logger object
        return logger


