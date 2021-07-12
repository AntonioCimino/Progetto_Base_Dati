import pymongo

def con():
    client = pymongo.MongoClient("mongodb://gruppo-base-dati:depressione3000@cluster0-shard-00-00.pus89.mongodb.net:27017,"
                             "cluster0-shard-00-01.pus89.mongodb.net:27017,cluster0-shard-00-02.pus89.mongodb.net:27017/"
                             "BaseDati?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=atlas-y6ur9o-shard-0&authSource=admin&retryWrites=true&w=majority")

    col = client["BaseDati"]["FakeNews"]

    return col
