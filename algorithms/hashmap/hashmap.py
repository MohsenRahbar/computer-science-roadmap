"""
Dictionary (HashMap) in Python
==============================

A Python dictionary (`dict`) is the equivalent of a HashMap in languages
such as Java.

A dictionary stores data as key-value pairs:

    key -> value

Example:

    "Canada" -> ["Calgary", "Toronto", "Vancouver"]

Internally, Python dictionaries are implemented using a hash table.
When you access a value by its key, Python computes the hash of the key
and locates the corresponding value efficiently.

Average Time Complexity
-----------------------
Lookup     : O(1)
Insertion  : O(1)
Deletion   : O(1)

Common Dictionary Methods
-------------------------
dict[key]          -> Access a value
dict.get(key)      -> Safe lookup (returns None or a default)
dict.keys()        -> Returns all keys
dict.values()      -> Returns all values
dict.items()       -> Returns key-value pairs
dict.pop(key)      -> Removes and returns a value
dict.update()      -> Updates the dictionary
dict.clear()       -> Removes all items

In this file we'll go through the most common dictionary operations
step by step.
"""

# ==========================================================
# 1. Creating a Dictionary
# ==========================================================

countries = {
    "Canada": ["Calgary", "Toronto", "Vancouver"],
    "USA": ["New York", "Chicago", "Los Angeles"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"]
}

print("Original Dictionary:")
print(countries)

print("-" * 50)


# ==========================================================
# 2. Accessing a Value
# ==========================================================

print("Cities in Canada:")
print(countries["Canada"])

print("-" * 50)


# ==========================================================
# 3. Safe Lookup using get()
# ==========================================================

print("Safe lookup:")

print(countries.get("Japan"))

# Key does not exist
print(countries.get("Germany"))

# Default value
print(countries.get("Germany", "Country not found"))

print("-" * 50)


# ==========================================================
# 4. Adding a New Item
# ==========================================================

countries["Germany"] = ["Berlin", "Hamburg", "Munich"]

print("After adding Germany:")
print(countries)

print("-" * 50)


# ==========================================================
# 5. Updating an Existing Item
# ==========================================================

countries["Canada"] = ["Calgary", "Toronto", "Vancouver", "Montreal"]

print("After updating Canada:")
print(countries["Canada"])

print("-" * 50)


# ==========================================================
# 6. Dictionary Keys
# ==========================================================

print("Keys:")
print(countries.keys())

print("-" * 50)


# ==========================================================
# 7. Dictionary Values
# ==========================================================

print("Values:")
print(countries.values())

print("-" * 50)


# ==========================================================
# 8. Dictionary Items
# ==========================================================

print("Items:")
print(countries.items())

print("-" * 50)


# ==========================================================
# 9. Iterating through the Dictionary
# ==========================================================

print("Loop through key-value pairs:")

for country, cities in countries.items():
    print(f"{country} -> {cities}")

print("-" * 50)


# ==========================================================
# 10. Checking if a Key Exists
# ==========================================================

print("Checking keys:")

print("Canada" in countries)
print("France" in countries)

print("-" * 50)


# ==========================================================
# 11. Removing an Item
# ==========================================================

removed = countries.pop("USA")

print("Removed:")
print(removed)

print()

print("Dictionary after removal:")
print(countries)

print("-" * 50)


# ==========================================================
# 12. Dictionary Length
# ==========================================================

print("Number of countries:")
print(len(countries))

print("-" * 50)


# ==========================================================
# 13. Nested Access
# ==========================================================

print("First city in Canada:")
print(countries["Canada"][0])

print("-" * 50)


# ==========================================================
# 14. Loop Through Only Keys
# ==========================================================

print("Countries:")

for country in countries:
    print(country)

print("-" * 50)


# ==========================================================
# 15. Loop Through Only Values
# ==========================================================

print("City Lists:")

for cities in countries.values():
    print(cities)

print("-" * 50)


# ==========================================================
# 16. Clear Dictionary
# ==========================================================

temp = {
    "A": 1,
    "B": 2
}

print("Before clear:")
print(temp)

temp.clear()

print()

print("After clear:")
print(temp)
