from utils import AppConfig as apc
from dbservice import MongoDBService as mdb


def start():
    # app = apc.AppConfigUtils()
    # configtest = app.getDBConfig()
    # print(configtest.getHost())
    dbService = mdb.MongoDBService()
    #dbService.connect()
    print(dbService.getDbList())
    db = dbService.create_db("db3")
    print(dbService.getDbList())

    col = dbService.create_collection("db3", "nanotubes")
    nanotubes = dbService.load_record_from_file()
   # dbService.batch_insert("db3","nanotubes", nanotubes)
    documents = dbService.fetch_all(col)
    printDocuments(documents)
    #condition_1 = {"Chiral indice n": {'$eq': 2}}

   # dbService.update_records(col, condition_1, {"$set": {'Calculated atomic coordinates u': "0,800000"}})
    #dbService.delete_documents(col, condition_1, batch_delete=True)
    #documents = dbService.filter_records(col, condition_1)
    #printDocuments(documents)
    #dbService.drop_collection(col)


def printDocuments(documents):
    for i in documents:
        print(i)


if __name__ == "__main__":
    start()
