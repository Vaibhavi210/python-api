import pandas as pd
import hashlib

df=pd.read_csv('utilsdata.csv')
print("original data",df)
columns=['segment_id','phone']
def drop_columns(df:pd.DataFrame,columns:list)-> pd.DataFrame:
    return df.drop(columns=columns)
    

df=drop_columns(df,columns)
print("after dropping the columns",df)
df.to_csv('updated_utilsData.csv',index=False)

def viewColumns(df:pd.DataFrame,columns:list)-> pd.DataFrame:
    return df[columns]
df=viewColumns(df,['fname','lname'])
print('df with specified columns',df)

def clean_up(df:pd.DataFrame,columns:list)-> pd.DataFrame:
   for col in columns:
       if col in columns:
           df[col]=df[col].astype(str).apply(lambda row:row.strip())
           return df
df=pd.DataFrame({'fname': ['                  vaibhavi  ', '  riya  '],'lname':['            khatri','shah']})
columns=['fname','lname']
print('before clean up',df)
df=clean_up(df,columns)
print('cleaned columns',df)

def hashValue(df:pd.DataFrame,columns:list,hash_type: str )-> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col]=df[col].astype(str).apply(lambda row:hashlib.md5(row.encode()).hexdigest()  if hash_type=='md5'
                                               else hashlib.sha256(row.encode()).hexdigest())
    return df

df=pd.DataFrame({'fname': ['vaibhavi', 'riya'],'lname':['khatri','shah']})
columns=['fname','lname']
df=hashValue(df,columns,'md5')
print('hashed values',df)