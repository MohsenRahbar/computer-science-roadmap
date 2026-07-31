import json

with open("data.json","r") as file:
    data = json.load(file)
print(data)


new_data = {"name":"mohsen","age":23,"skils":["python","DSA"]},{"name":"ali","age":30,"skils":["network","Desk"]}

with open ("new_data.json","w") as file:
    json.dump(new_data,file,indent=4)