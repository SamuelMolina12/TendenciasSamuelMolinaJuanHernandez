import pymongo

mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'hospitalDbMongo'
collection_nameH = 'clinicHistory'

client = pymongo.MongoClient(host=mongo_host,port = mongo_port)
db = client[mongo_db_name]
collection=db[collection_nameH]

collection_namem = 'visitHistory'
collectionB=db[collection_namem]