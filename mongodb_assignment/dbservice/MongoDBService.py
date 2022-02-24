import csv

import pymongo

from dbservice.MDBService import AbstractDBService
from exceptions.DBConnectException import DBConnectException
from exceptions.MongoQueryException import MongoQueryException
from logservice.LoggerFactory import LoggerFactory



class MongoDBService(AbstractDBService):
    """This class has method to connect with the mongodb_assignment database as well as method for saving, updating, deleting etc(
    CRUD) """

    def __init__(self):
        self.db = None
        self.logger = LoggerFactory.getLogger("MongoDBService")
        self.client = super()._connect()


    def getDbList(self):
        """
        This method return existing databases's name otherwise raise MongoQueryException
        Parameters:
            self: current pointer

        """

        self.logger.info("Fetching data list from mongodb")
        try:
            # list_database_names () try to fetch the database details with connected mongoDB file
            dbList = self.client.list_database_names()
            self.logger.info("DB list fetch successfully")
            return dbList
        except Exception as e:
            self.logger.warn("exception raise", e)
            raise MongoQueryException(e)

    def create_db(self, name):
        """
        This method create a database in mongodb.
        Parameters:
        :name: takes database name as a input
        :return: DB object
        :raise DBException: return DBException in case of if some unexpected exception comes from the MongoDB
        """
        self.logger.info("creating db")
        self.logger.debug("creating db with name %s", name)
        try:
            db = self.client[name]
            self.logger.info("db created successfully")
            return db
        except Exception as e:
            self.logger.error("exception is raise during db creation", e)
            raise MongoQueryException(e)


    def load_record_from_file(self,path):
        nanotubes = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=";")
            header = next(csv_reader)
            print(header)

            for line in csv_reader:
                nanotube = {}
                nanotube[header[0]] = int(line[0])
                nanotube[header[1]] = int(line[1])
                nanotube[header[2]] = line[2]
                nanotube[header[3]] = line[3]
                nanotube[header[4]] = line[4]
                nanotube[header[5]] = line[5]
                nanotube[header[6]] = line[6]
                nanotube[header[7]] = line[7]
                nanotubes.append(nanotube)
        return nanotubes

    def create_collection(self, db, coll_name):
        """
        This method create a new collection if collection.
        Parameter :
            coll_name : This hold name of collection which user want to create on mongoDB.
        """
        self.logger.info("Creating or getting information of collection")
        db = self.create_db(db)
        return db[coll_name]

    def batch_insert(self, db, col, records):
        """
        This method insert multiple documents to the collection.
        Parameter:
        :col : this is name of collection in which documents will add.
        :db : name of the db
        :records : this is list of all the dictionary which inserted into the collection
        """
        try:
            self.logger.debug("inserting batch records")
            # calling connect method

            db_col = self.create_collection(db, col)
            db_col.insert_many(records)
            self.logger.debug("Batch update finished")
        except Exception as e:
            self.logger.error("Error during batch processing")
            raise MongoQueryException(e)


    def fetch_all(self, col):
        """
        This method fetch all the records from given collection and return list.
        """
        self.logger.info("fetching records from %s", str(col))
        try:
            return col.find()
        except Exception as e:
            self.logger.warn("Exception is raised during execution of find query")
            raise MongoQueryException(e)

    def single_insert(self, col, record):
        """This method insert single documents to the collection"""
        try:
            self.logger.debug("adding single document")
            return col.insert_one(record)
            self.logger.debug("single document added successfully")
        except Exception as e:
            self.logger.error("Exception is raised during insertion of single record into the DB")
            raise MongoQueryException(e)

    def find_single_document(self, col):
        """
        This method returns single result to caller
        """
        try:
            return col.find_one()
        except Exception as e:
            self.logger.error("Exception is raised during execution query for single record")
            raise MongoQueryException(e)

    def filter_records(self, col, conditions):
        """This method accept the condition and return a list on success execution of query otherwise throw exception"""
        try:
            self.logger.debug("filtering records on criteria %s", conditions)
            records = col.find(conditions)
            self.logger.debug("filter records successfully")
            return records
        except Exception as e:
            self.logger.error("exception is raised during proceed the records")
            raise MongoQueryException(e)

    def update_records(self, col, exp, updated_val):
        """This method takes filter condition in **kwargs parameter, collection in col and process for update the
        document """
        try:
            self.logger.info("Updating records")
            self.logger.debug("parameter are ", exp)
            updated_records = col.update_many(exp, updated_val)
            self.logger.info("Records update successfully")
            return updated_records
        except Exception as e:
            self.logger.warn("Exception is raised during updation of records")
            raise MongoQueryException(e)

    def delete_documents(self, col, cond, batch_delete=False):
        """This method deletes multiple/single records base on the condition passed to the system"""
        try:
            self.logger.info("Deleting records")
            # check whether batch delete is true or not
            if batch_delete:
                # delete many records depend upon the condition
                col.delete_many(cond)
            else:
                # delete single records depend upon the condition
                col.delete_one(cond)

            self.logger.info("Deleted record successfully")
        except Exception as e:
            raise MongoQueryException(e)

    def drop_collection(self, col):
        """This method drop collection from mongodb """
        try:
            self.logger.info("Dropping collection")
            self.logger.debug("collection name %s", str(col))
            col.drop()
            self.logger.info("Dropped collection successfully")
        except Exception as e:
            #self.logger.error("Exception is raised during deletion of ", col)
            raise MongoQueryException("error")


