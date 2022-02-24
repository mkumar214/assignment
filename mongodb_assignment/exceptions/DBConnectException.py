class DBConnectException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def getDescription(self):
        return self.msg
