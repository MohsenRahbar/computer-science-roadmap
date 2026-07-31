import csv,json

with open("names.txt","r") as file:
    data_reader = csv.DictReader(file,delimiter="\t")
    data = [row for row in data_reader]
    
with open("info.json","w") as file:
    json.dump(data,file,indent=4) 
    
    