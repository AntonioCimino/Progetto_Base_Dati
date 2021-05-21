import  Dataset_connection

def query_six_recent():
    col = Dataset_connection.con()
    query = col.find().sort([("published", -1)]).limit(6)
    return query


