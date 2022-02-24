import configparser
from configs import Dbconfig

class AppConfigUtils:
    def __init__(self):
        pass


    def getDBConfig(self):
        """This method returns config parser"""
        cparser = AppConfigUtils.__getConfigParser()
        props = cparser.read('resources/db_config.properties')
        print(props)
        dbinfo = cparser['MongoDBConfig']
        host = dbinfo['host']
        username = dbinfo['username']
        password = dbinfo['password']
        return Dbconfig.DBConfig(username, password, host)

    @staticmethod
    def __getConfigParser():
        return configparser.ConfigParser()

    @staticmethod
    def getLogConfig():
        """
        This function load default logging properties from log_config.properties and return log_level,log_format
        date_fmt in the map
        """
        logconfiginfo = {}
        cparser = AppConfigUtils.__getConfigParser()
        props = cparser.read('resources/log_config.properties')
        defaultlogprop = cparser['Default']

        logconfiginfo['log_level'] = defaultlogprop['log_level']
        logconfiginfo['log_format'] = defaultlogprop['log_format']
        logconfiginfo['date_fmt'] = defaultlogprop['date_fmt']
        return logconfiginfo


