import  Dataset_connection

def query_six_recent():
    col = Dataset_connection.con()
    query = col.find().sort([("published", -1)]).limit(6)
    return query

def query_for_text(testo):
    col = Dataset_connection.con()
    query_text = col.find({"text":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    query_title = col.find({"title":{"$regex" : ":*"+testo+"+.*"}}).sort([("published", -1)]).limit(6)
    return query_title, query_text

def query_for_author(testo):
    col = Dataset_connection.con()
    query_author = col.find({"author":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    return query_author

def query_for_country(testo):
    col = Dataset_connection.con()
    query_country = col.find({"country":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    return query_country

def query_for_leng(testo):
    col = Dataset_connection.con()
    query_leng = col.find({"language":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    return query_leng

def query_for_site(testo):
    col = Dataset_connection.con()
    query_site = col.find({"site_url":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    return query_site

def query_for_date(testo):
    col = Dataset_connection.con()
    query_date = col.find({"published":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(6)
    return query_date