from pymongo.mongo_client import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from settings import database_settings


client: MongoClient = MongoClient(database_settings.uri, uuidRepresentation='standard')
db: Database = client[database_settings.database]
coll: Collection = db[database_settings.collection]
