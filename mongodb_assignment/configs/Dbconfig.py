''''This file contains db configuration properties and'''
class DBConfig:
    def __init__(self,username,password,host): 
        self.username = username
        self.password = password
        self.host = host

    '''This method return username of the db'''
    def getUsername(self):
        return self.username

    '''This method returns password of db'''
    def getPassword(self):
        return self.getPassword

    '''This method return host url of database'''
    def getHost(self):
        return self.host            
