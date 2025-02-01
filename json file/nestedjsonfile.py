import json

nestedData=[{
    'name':{'firstname':'vaibhavi',
            'lastname':'khatri'
            },
    'age':20,
    'city':'ahmedabad'
    },
   {
    'name':{'firstname':'riya',
            'lastname':'khatri'
            },
    'age':20,
    'city':'ahmedabad'
    },
     {
    'name':{'firstname':'priya',
            'lastname':'khatri'
            },
    'age':20,
    'city':'ahmedabad'
    } ]
path='nestedjson.json'

with open(path,'w') as jsonFile:
    json.dump(nestedData,jsonFile)
print('this is the nested json file')

with open('nestedndjsonfile.ndjson','w') as ndjsonFile:
    for obj in nestedData:
        json.dump(obj,ndjsonFile)
        ndjsonFile.write('\n')
print('this is the nested ndjson file')

