import pandas as pd
import hashlib
import time
from dummydata import generate_fake_data

start_time = time.time() 
df = generate_fake_data(10) 


df.to_csv("data.csv",index=False)
print("dummydata",df)
filtered_df = df[(df["segment_name"].isna() | (df["segment_name"] == "")) &  
                 (df["segment_id"].isna() | (df["segment_id"] == ""))]
print("filtered data",filtered_df)
deleted_df=df.drop(filtered_df.index,inplace=True)
print("cleaned data",deleted_df)
df.to_csv("data.csv",index=False)
print("cleaned data from file",df)

#checking for columns and creating if not exist
columns_check= {'fname': 'fname_hash', 'lname': 'lname_hash', 'email': 'email_hash', 'phone': 'phone_hash'}
for key,missing_columns in columns_check.items():
    if missing_columns not in df.columns:
        df[missing_columns]=""
print(" data with or without columns",df)

def generate_hash(value):
    if pd.isna(value) or value == "":
        return ""
    return hashlib.sha256(value.encode()).hexdigest()

for key,missing_columns in columns_check.items():
    df[missing_columns] = df[missing_columns].mask(df[missing_columns] == "", df[key].astype(str).apply(generate_hash))
    

df.to_csv('data.csv',index=False)


print('final_updated',df)
end_time=time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")