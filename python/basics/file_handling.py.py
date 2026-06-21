"""
Python File Handling Examples

Topics covered:
- open()
- read()
- readline()
- file iteration
- exception handling
- append mode
- write mode
- with statement
"""

# Open a file
f = open("t_example_txt.txt")

# Read the entire file
# print(f.read())

# Read the first 6 characters
# print(f.read(6))

# Read the first line
# print(f.readline())

# Read multiple lines
# print(f.readline())
# print(f.readline())

# Read file line by line
for line in f:
    print(line)

# Always close the file after use
f.close()

# Error handling example

try:
    f = open("NoExistFile", "r")
    print(f.read())

except:
    print("File does not exist or another error occurred.")

finally:
    f.close()
# Or better, use else in this case because
# if open() fails, the file object may not exist,
# and calling f.close() inside finally can raise another error.


# A better way to work with files

with open("newfile.txt", "w+") as f:
    f.write("something new")

# Read lines from a file, sort them, and write the result to a new file

with open("t_example_txt.txt","r") as input_file:
    with open("sorted_titles.txt.txt","w") as output_file:
        titles = input_file.read().split("\n")
        titles.sort()
        output_file.write("\n".join(titles))
