import pandas as pd
import hashlib
import time
from dummydata import generate_fake_data
import random

start_time = time.time() 
# df=pd.read_csv("data.csv")

df = generate_fake_data(10) 


df.to_csv("data.csv",index=False)
print("dummydata",df)
filtered_df = df[(df["segment_name"].isna() | (df["segment_name"] == "")) &  
                 (df["segment_id"].isna() | (df["segment_id"] == ""))]
print("fitered data ",filtered_df)
deleted_df=df.drop(filtered_df.index,inplace=True)
print("cleaned data",deleted_df)
df.to_csv("updated_data.csv",index=False)
print("cleaned data from df",df)


def generate_hash(value):
    if pd.isna(value) or value=="":
        return ""
    return hashlib.sha256(value.encode()).hexdigest()

#checking for columns and creating if not exist
columns_check=['fname_hash', 'lname_hash', 'email', 'email_hash', 'phone', 'phone_hash']
for col in columns_check:
    if col not in df.columns:
        df[col]=""
        
    
        

print("data with columns or no columns",df)
for index, row in df.iterrows():
    if not row['fname_hash']:
        df.at[index,'fname_hash']=generate_hash(str(row['fname']))
    if not row['lname_hash']:
        df.at[index,'lname_hash']=generate_hash(str(row['lname']))
    if not row['email_hash']:
        df.at[index,'email_hash']=generate_hash(str(row['lname']))
    if not row['phone_hash']:
        df.at[index,'phone_hash']=generate_hash(str(row['lname']))
    


df.to_csv('updated_data.csv',index=False)


print('final_updated',df)
end_time=time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")