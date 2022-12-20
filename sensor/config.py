import pymongo 
import pandas as pd
import json
from dataclass import dataclass 
# Provide the mongodb local host url to connect to python to mongodb
import os 


@dataclass()
class EnvironmentVariable:
    mongo_db_url:str = os.getenv('MONGO_DB_URL')
    aws_acess_key_id:str = os.getenv("AWS_ACESS_KEY_ID")
    aws_access_secret_key:os.getenv("AWS_SECRET_ACCESS_KEY")
    


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)