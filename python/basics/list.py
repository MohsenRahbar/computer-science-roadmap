# Python List Concepts
#
# This file covers:
# 1. List Comprehension
# 2. Slicing
# 3. Mutable vs Immutable objects
# 4. append() vs extend()


# =================================
# List Comprehension
# =================================

# Normal way

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)


# Using List Comprehension

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)


# List Comprehension with condition

numbers = [1, 2, 3, 4, 5]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)


# =================================
# Slicing
# =================================

# list[start:end:step]

numbers = [10, 20, 30, 40, 50]


# Get elements from index 2 to 3
print(numbers[2:4])


# Get elements from index 2 to the end
print(numbers[2:])


# Get elements from the beginning to index 2
print(numbers[:3])


# Reverse the list
print(numbers[::-1])


# =================================
# Mutable vs Immutable
# =================================

# Mutable example (List can be changed)

numbers = [1, 2, 3]

numbers[0] = 100

print(numbers)


# Immutable example (String cannot be changed)

# This code raises TypeError:
#
# text = "Hello"
# text[0] = "h"


# Correct way: create a new string

text = "Hello"

new_text = "h" + text[1:]

print(new_text)


# =================================
# append vs extend
# =================================

# append adds the whole object as a single element

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)


# extend adds each element separately

numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
