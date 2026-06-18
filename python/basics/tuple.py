# ==========================
# Python Tuple Methods & Operations
# ==========================

# Tuple with mixed data types
mytuple = (1, 2, 3, "bye", 4, "hi", "welcome")

# Accessing elements
print(mytuple[-1])
print(mytuple[1])

# Tuple slicing
print(mytuple[1:4])
print(mytuple[:3])
print(mytuple[3:])

# ==========================
# Convert List to Tuple
# ==========================

mylist = [12, 127, "close", 23412, "xyz", 11, 11]

mytuple2 = tuple(mylist)
print(type(mytuple2))
print(mytuple2)

# ==========================
# Convert Tuple to List
# ==========================

tupleexample = (1, 3, 2)

mylist2 = list(tupleexample)
print(type(mylist2))
print(mylist2)

# ==========================
# Tuple Methods
# ==========================

# count() -> counts occurrences of a value
print(mytuple2.count(11))

# index() -> returns index of first occurrence
print(mytuple.index("bye"))

# ==========================
# Membership Test
# ==========================

print("bye" in mytuple)

# ==========================
# Loop Through Tuple
# ==========================

for i in mytuple:
    print(i)

# Loop with index using enumerate
for index, value in enumerate(mytuple):
    print(index, value)

# ==========================
# Tuple Concatenation
# ==========================

join_tuple = mytuple + mytuple2
print(join_tuple)

# ==========================
# Tuple Repetition
# ==========================

print(mytuple2 * 3)

# ==========================
# Access index() method
# ==========================

numbers = (10, 20, 30)

print(numbers.index(20))

# ==========================
# Tuple Unpacking
# ==========================

person = ("Ali", 25, "Developer")

name, age, job = person

print(name)
print(age)
print(job)
