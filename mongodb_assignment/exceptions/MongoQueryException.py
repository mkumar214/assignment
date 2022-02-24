"""This exception is raised during the execution of MongoDB query in database"""


class MongoQueryException(Exception):
    def __init__(self, ex):
        self.ex = ex

    def getDescription(self):
        return self.ex
