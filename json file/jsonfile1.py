import json

data=[{
    'name':'vaibhavi khatri',
    'age':20,
    'city':'ahmedabad'
    },
   {
    'name':'riya khatri',
    'age':20,
    'city':'ahmedabad'
    },
     {
    'name':'priya khatri',
    'age':20,
    'city':'ahmedabad'
    } ]
path='firstjson.json'

with open(path,'w') as jsonFile:
    json.dump(data,jsonFile)
print('this is the json file')

with open('ndjsonfile.ndjson','w') as ndjsonFile:
    for obj in data:
        json.dump(obj,ndjsonFile)
        ndjsonFile.write('\n')
print('this is the ndjson file')
