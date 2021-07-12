import  Dataset_connection
import matplotlib.pylab as plt

def query_six_recent():
    col = Dataset_connection.con()
    query = col.find().sort([("published", -1)]).limit(3)
    return query

def query_for_text(testo):
    col = Dataset_connection.con()
    query_text = col.find({"text":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(5)
    query_title = col.find({"title":{"$regex" : ":*"+testo+"+.*"}}).sort([("published", -1)]).limit(5)
    return query_title, query_text

def query_for_author(testo):
    col = Dataset_connection.con()
    query_text = []
    query_author = col.find({"author":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(10)
    return query_author, query_text

def query_all_author():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$author"}}])
    return query

def query_for_country(testo):
    col = Dataset_connection.con()
    query_text = []
    query_country = col.find({"country":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(10)
    return query_country, query_text

def query_all_country():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$country"}}])
    return query

def query_all_country_count():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$country","count": {"$sum": 1}}}])

    array_num_c = []
    label_c = []
    for x in query:
        array_num_c.append(x['count'])
        label_c.append(x['_id'])
    array_num_c.sort()
    label_c.sort()
    plt.bar(label_c, array_num_c, color='#F3B253')
    plt.xticks(label_c, label_c)
    plt.title('Number of fake-news for country')
    plt.savefig('static/immagini/country_graph.png')

    plt.close()

def query_for_leng(testo):
    col = Dataset_connection.con()
    query_text = []
    query_leng = col.find({"language":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(10)
    return query_leng, query_text

def query_all_leng():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$language"}}])
    return query

def query_all_len_count():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$language","count": {"$sum": 1}}}])

    array_num_l = []
    label_l = []
    for x in query:
        array_num_l.append(int(x['count']))
        label_l.append(x['_id'])
    array_num_l.sort()
    label_l.sort()
    plt.bar(label_l, array_num_l, color='#F3B253')
    plt.xticks(label_l, label_l)
    plt.title('Number of fake-news for language')
    plt.savefig('static/immagini/len_graph.png')

    plt.close()

def query_for_site(testo):
    col = Dataset_connection.con()
    query_text = []
    query_site = col.find({"site_url":{"$regex" : ".*"+testo+".*"}}).sort([("published", -1)]).limit(10)
    return query_site, query_text

def query_all_site():
    col = Dataset_connection.con()
    query = col.aggregate([{"$group": {"_id": "$site_url"}}])
    return query

def query_for_date(testo):
    col = Dataset_connection.con()
    query_text = []
    query_date = col.find({"published":{"$regex" : ".*"+testo+".*"}}).limit(10)
    return query_date, query_text