import pandas as pd

data=pd.read_parquet('file4.parquet',engine='fastparquet')

print("content :", data)

if 'name' in data.columns:
    print("\n nested child object:",data['name'])
else :
    print('no nested data')