import os
import pymongo
from pymongo import MongoClient

import ssl
import datetime

def db_connect():
    URL = "mongodb://admin:MHFUHVSQTMAMKENR@bluemix-sandbox-dal-9-portal.8.dblayer.com:27271,bluemix-sandbox-dal-9-portal.6.dblayer.com:27271/admin?ssl=true"

    #MONGODB_URL=os.environ.get(URL)
    #print(MONGODB_URL)
    #client = MongoClient(MONGODB_URL,ssl_cert_reqs=ssl.CERT_NONE)
    client = MongoClient(URL, ssl_cert_reqs=ssl.CERT_NONE)
    #db = client.get_default_database()

    db = client.mytestdatabase

    #print(db.collection_names())
    print(db.collection_names)

    #collection = db['monstars']
    collection = db.monsters
    monster = {"name":"Dracula",
           "occupation":"Blood Sucker",
           "tags":["vampire","teeth","bat"],
           "date":datetime.datetime.utcnow()
           }

    count = collection.count()

    print("the number of doc in this collection is :", count)

    collection.remove({"name":"Dracula"})

    monster_id = collection.insert(monster)
    if monster_id:
        print ("OK")
    else:
        print("NG")
    for monster in collection.find():
        print (monster)
    print (collection.find_one({"name":"Dracula"}))
    return db,collection


