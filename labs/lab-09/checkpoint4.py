import pymongo
import pprint
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["mongo_db_lab"]

col = db["definitions"]

if __name__ == '__main__':
    print("Fetch one record")
    pprint.pprint(col.find_one())
    print("\n---\n")
    print("Fetch all record")
    for record in col.find():
        pprint.pprint(record)
    print("\n\nFetch a specific record")
    pprint.pprint(col.find_one({"word": "Opus"}))
    print("\n\nFetch a record by object id")
    pprint.pprint(col.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b8b7')}))
    print("\n\nInsert a new record")
    pprint.pprint(col.find_one({"word": "Duck"}))
    col.insert_one({"word": "Duck", "definition": "An animal to be feared that quacks."})
    pprint.pprint(col.find_one({"word": "Duck"})) 
