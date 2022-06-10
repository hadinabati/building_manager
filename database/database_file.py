import  pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["building"]
user_collection = mydb["user"]
base_collection = mydb['base']
building_collection = mydb['building']