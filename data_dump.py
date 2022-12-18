import pymongo 
import pandas as pd
import json 
# Provide the mongodb local host url to connect to python to mongodb
#client = pymongo.MongoClient('mongodb+srv://hugar_rajesh:Rajesh_0808@rajesh.ud2bw.mongodb.net/test')
client = pymongo.MongoClient('mongodb://localhost:27017')


# We have stored these records in the folder nut in actual we dont do these 
DATA_FILE_PATH = "aps_failure_training_set1.csv"
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")
    
    # Convert dataframe to json so that we can  dump these records in mongo db
    df.reset_index(drop=True,inplace=True)
    
    json_record =list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    