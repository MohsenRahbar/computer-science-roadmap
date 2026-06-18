# ==========================
# Python List Methods & Operations
# ==========================

mylist = ["", 1, "hello", "hi", 55, 127.3, "ali"]

# Add item to the end
mylist.append("s")
print(mylist)

# Insert item at specific index
mylist.insert(2, "s*")
print(mylist)

# Remove last item
mylist.pop()
print(mylist)

# Remove item by index
mylist.pop(2)
print(mylist)

# Remove first matching value
mylist.remove("")
print(mylist)

# Insert duplicate value
mylist.insert(2, "hi")
print(mylist)

# Remove first occurrence of "hi"
mylist.remove("hi")
print(mylist)

# Create a shallow copy
secondlist = mylist.copy()
secondlist.append("This is the second list")
print(secondlist)

# Add multiple items
mylist.extend([12, 16, 17])
print(mylist)

# Find index of a value
print("Index of 127.3:", mylist.index(127.3))

# Count occurrences of a value
mylist.append("hi")
print('Count of "hi":', mylist.count("hi"))

# ==========================
# Accessing Elements
# ==========================

print("First item:", mylist[0])
print("Second item:", mylist[1])
print("Last item:", mylist[-1])

# List slicing
print("Items from index 1 to 3:", mylist[1:4])
print("First 3 items:", mylist[:3])
print("Items from index 2 to end:", mylist[2:])

# ==========================
# Updating Elements
# ==========================

mylist[0] = "updated"
print(mylist)

# ==========================
# Deleting Elements
# ==========================

del mylist[0]
print(mylist)

# ==========================
# Membership Test
# ==========================

print("ali" in mylist)
print("mohammad" not in mylist)

# ==========================
# List Information
# ==========================

print("Length:", len(mylist))

# Numeric functions require only numbers
numbers = [10, 20, 30, 40]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# ==========================
# Sorting
# ==========================

nums = [5, 1, 8, 3]

nums.sort()
print("Ascending:", nums)

nums.sort(reverse=True)
print("Descending:", nums)

# sorted() returns a new list
nums2 = [7, 2, 9, 1]

sorted_nums = sorted(nums2)

print("Original:", nums2)
print("Sorted:", sorted_nums)

# ==========================
# Reverse List
# ==========================

nums2.reverse()
print("Reversed:", nums2)

# ==========================
# Loop Through a List
# ==========================

names = ["ali", "reza", "sara"]

for name in names:
    print(name)

# Loop with index using enumerate
for index, value in enumerate(names):
    print(index, value)

# Start numbering from 1
for index, value in enumerate(names, start=1):
    print(index, value)

# ==========================
# Concatenate Lists
# ==========================

list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2
print(result)

# ==========================
# Repeat Lists
# ==========================

repeated = [1, 2] * 3
print(repeated)

# ==========================
# List Comprehension
# ==========================

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

# ==========================
# Difference Between Assignment and Copy
# ==========================

a = [1, 2, 3]

b = a
b.append(4)

print("a =", a)
print("b =", b)

c = a.copy()
c.append(5)

print("a =", a)
print("c =", c)

# ==========================
# Convert Other Types to List
# ==========================

text = "hello"

chars = list(text)

print(chars)

# ==========================
# Clear List
# ==========================

mylist.clear()
print(mylist)