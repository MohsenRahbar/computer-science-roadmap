import json

json_string = '''
    {
        "students":[
            {
                "Id": 1,
                "name": "mohsen",
                "age": 23,
                "full-time": true
            },
            {
                "Id": 2,
                "name": "ali",
                "age": 30,
                "full-time": false
            }
        ]
    }
'''
data = json.loads(json_string)
print(data['students'][0])
data['test'] = True
new_json = json.dumps(data,indent=4,sort_keys=True)
print(new_json)