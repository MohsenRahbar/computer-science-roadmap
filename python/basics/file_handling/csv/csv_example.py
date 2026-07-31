import csv


with open("names.txt", "r") as reader_csv:
    csv_reader = csv.reader(reader_csv)
    
    with open("new_csv.txt","w") as writer:
        writer_file = csv.writer(writer,delimiter="\t")
    
        for line in csv_reader:
            writer_file.writerow(line)


with open("new_csv.txt","r") as file:
    csv_reader = csv.DictReader(file,delimiter="\t")
    
    for line in csv_reader:
        print(line)
        

print("\n\tread defualt txt:\n")
        
with open("names.txt","r") as file:
    csv_reader = csv.DictReader(file)
    
    for line in csv_reader:
        print(line)
        

with open("names.txt","r") as file:
    csv_reader = csv.DictReader(file)
    
    with open("new_csv_new.txt","w") as writer:
        fieldnames = ["firstname","lastname"]
        
        writer_file = csv.DictWriter(writer,fieldnames=fieldnames,delimiter="\t")
        
        writer_file.writeheader()
        
        for line in csv_reader:
            del line["mail"]
            writer_file.writerow(line)
"""
with open("new_csv.txt","r") as file:
    csv_reader = csv.reader(file,delimiter="\t")
"""