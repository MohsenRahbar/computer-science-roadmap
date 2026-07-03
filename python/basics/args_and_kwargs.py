"""
args_kwargs_tutorial.py

This file demonstrates how function parameters evolve from
regular parameters to *args and **kwargs.

Instructions:
1. Run this file first.
2. Observe the final working example.
3. Uncomment each section one by one.
4. Read the output or the error before moving to the next section.
"""

# ============================================================
# STEP 1 - Regular function
# ============================================================

# def tea_order(customer_order, tea_type):
#     print(f"\n{customer_order} ordered a {tea_type} tea")
#
#
# tea_order("Ali", "Green")


# ============================================================
# STEP 2 - Too many positional arguments
# ============================================================

# Uncomment this section to see the error.
#
# TypeError:
# tea_order() takes 2 positional arguments but 3 were given

# def tea_order(customer_order, tea_type):
#     print(f"\n{customer_order} ordered a {tea_type} tea")
#
#
# tea_order("Ali", "Green", "More milk")


# ============================================================
# STEP 3 - Using *args
# ============================================================

# def tea_order(customer_order, tea_type, *args):
#
#     print(f"\n{customer_order} ordered a {tea_type} tea")
#
#     for arg in args:
#         print("__ Add", arg)
#
#
# tea_order("Ali", "Green")
# tea_order("Mohsen", "Black", "More milk")
# tea_order("Sara", "Green", "Honey", "Lemon")


# ============================================================
# STEP 4 - Using **kwargs
# ============================================================

# def tea_order(customer_order, tea_type, **kwargs):
#
#     print(f"\n{customer_order} ordered a {tea_type} tea")
#
#     for key, value in kwargs.items():
#         print("__ Add", key, ":", value)
#
#
# tea_order("Ali", "Green")
# tea_order("Mohsen", "Black", milk="Oat")
# tea_order("Sara", "Green", sugar="Low", lemon=True)


# ============================================================
# FINAL EXAMPLE
# Regular parameters + *args + **kwargs
# ============================================================

def tea_order(customer_order, tea_type, *args, **kwargs):
    print(f"\n{customer_order} ordered a {tea_type} tea")

    for arg in args:
        print("__ Add", arg)

    for key, value in kwargs.items():
        print("__ Add", key, ":", value)


tea_order("Ali", "Green")

tea_order(
    "Mohsen",
    "Black",
    milk="Oat"
)

tea_order(
    "Ramtin",
    "Black",
    "More milk",
    milk="Oat"
)
