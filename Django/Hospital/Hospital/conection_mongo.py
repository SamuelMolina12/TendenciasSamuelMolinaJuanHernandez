import pymongo

mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'hospitalDbMongo'
collection_name = 'clinicHistory'

client = pymongo.MongoClient(host=mongo_host,port = mongo_port)
db = client[mongo_db_name]
collection=db[collection_name]