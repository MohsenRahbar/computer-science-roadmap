"""
lambda_tutorial.py

This file demonstrates how to use lambda functions in Python.

Instructions:
1. Run this file.
2. Observe the final examples.
3. Uncomment each section one by one.
4. Compare lambda expressions with regular functions.
"""

# ============================================================
# STEP 1 - Regular Function
# ============================================================

# def square_sum(num1, num2):
#     return (num1 + num2) ** 2
#
#
# print(square_sum(12, 3))


# ============================================================
# STEP 2 - Lambda Function
# ============================================================

# square_sum = lambda num1, num2: (num1 + num2) ** 2
#
# print(square_sum(12, 3))


# ============================================================
# STEP 3 - Using map()
# ============================================================

# my_list = [12, 13, 16, 17, 11]
#
# cube_numbers = map(lambda num: num ** 3, my_list)
#
# print(list(cube_numbers))


# ============================================================
# STEP 4 - Using filter()
# ============================================================

# my_list = [12, 13, 16, 17, 11]
#
# even_numbers = filter(lambda num: num % 2 == 0, my_list)
#
# print(list(even_numbers))


# ============================================================
# FINAL EXAMPLES
# ============================================================

# Lambda expression
square_sum = lambda num1, num2: (num1 + num2) ** 2

print(square_sum(12, 3))


my_list = [12, 13, 16, 17, 11]

# map() applies the lambda function to every item.
print(list(map(lambda num: num ** 3, my_list)))

# filter() keeps only the items that satisfy the condition.
print(list(filter(lambda num: num % 2 == 0, my_list)))