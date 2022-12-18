import pymongo 
import pandas as pd
# Provide the mongodb local host url to connect to python to mongodb
client = pymongo.MongoClient('')


DATA_FILE_PATH = "D:\Practise API Sensor Fault\aps_failure_training_set1.csv"
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")