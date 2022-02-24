from abc import ABC, abstractmethod
import pymongo
from exceptions.DBConnectException import DBConnectException
from utils import AppConfig as ac

class AbstractDBService(ABC):
    """This abstract class exposes common db service"""

    def __init__(self):
        self.client = None

    def _connect(self):
        """Connection method read the db configuration from properties file and try to connect with the database.If
         connection is successful the set the mongoclient object with the object other raise DBConnectionException """
        self.logger.info("Inside connection")
        appUtils = ac.AppConfigUtils()
        # Reading configuration from configuration file
        dbconfig = appUtils.getDBConfig()
        try:
            # connect with the mongoDB

                self.logger.info("Connection is not existing,creating a new connection ")
                client = pymongo.MongoClient(dbconfig.getHost())
                self.logger.info("connect completed")
                return client
        except Exception as e:
            self.logger.warn("exception raise", e)
            raise DBConnectException(e)

    @abstractmethod
    def getDbList(self):
        pass

    @abstractmethod
    def create_db(self, name):
        pass

    @abstractmethod
    def create_collection(self, coll_name):
        """
        This method create a new collection
        """
        pass

    @abstractmethod
    def batch_insert(self, col, records):
        """This method insert multiple documents to the collection"""
        pass

    @abstractmethod
    def single_insert(self, col, record):
        """This method insert single documents to the collection"""
        pass

    @abstractmethod
    def fetch_all(self, col):
        """
        This method fetch all the records from given collection and return list.
        """
        pass

    @abstractmethod
    def find_single_document(self, col):
        """
        This method returns single result to caller
        """
        pass

    @abstractmethod
    def filter_records(self, col, conditions):
        """This method accept the condition and return a list on success execution of query otherwise throw exception"""
        pass

    @abstractmethod
    def update_records(self, col, exp, updated_val):
        """This method takes dictionary as a input and process for update the document"""
        pass

    @abstractmethod
    def delete_documents(self, col, cond, batch_delete=False):
        """This method deletes multiple/single records base on the condition passed to the system"""
        pass

    @abstractmethod
    def drop_collection(self, col):
        """This method drop collection from mongdb """
        pass


