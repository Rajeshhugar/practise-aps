import pymongo 

# Provide the mongodb  localhost url t oconnect python to mongodb
client =pymongo.MongoClient('mongodb://localhost:27017')

# Database Name
database = client[]

# Collection Name 
collection = database['Products']


# Sample Data 
d = {}