class DBBasicException(Exception):
    """This exception class throws when db schema related exception raised"""
    def __init__(self, ex):
        self.ex = ex

