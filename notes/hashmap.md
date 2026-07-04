# Python Dictionary (`dict`) – HashMap in Python

## What is a Dictionary?

A Python **dictionary (`dict`)** is the equivalent of a **HashMap** in languages like Java.

It stores data as **key–value pairs**, allowing fast lookup, insertion, and deletion.

```
Key  -> Value

"Ali"  -> 20
"Sara" -> 18
"Reza" -> 19
```

---

## Creating a Dictionary

```python
students = {
    "Ali": 20,
    "Sara": 18,
    "Reza": 19
}
```

---

## Accessing Values

Retrieve a value using its key:

```python
print(students["Sara"])
```

Output:

```text
18
```

A dictionary computes the hash of the key and directly locates the corresponding entry instead of searching through every element.

---

## Adding a New Item

```python
students["Amir"] = 17
```

Result:

```python
{
    "Ali": 20,
    "Sara": 18,
    "Reza": 19,
    "Amir": 17
}
```

---

## Updating a Value

```python
students["Sara"] = 20
```

---

## Removing Items

Using `del`:

```python
del students["Ali"]
```

Or using `pop()`:

```python
students.pop("Ali")
```

---

## Checking if a Key Exists

```python
if "Sara" in students:
    print("Key exists")
```

---

## Safe Lookup with `get()`

Accessing a missing key with `[]` raises an exception:

```python
students["Mohammad"]
```

```
KeyError
```

A safer approach:

```python
students.get("Mohammad")
```

Output:

```python
None
```

Providing a default value:

```python
students.get("Mohammad", 0)
```

Output:

```python
0
```

---

## Iterating Through a Dictionary

### Iterate over keys

```python
for key in students:
    print(key)
```

### Iterate over keys and values

```python
for key, value in students.items():
    print(key, value)
```

Output:

```text
Ali 20
Sara 18
Reza 19
```

---

## The `hash()` Function

Python exposes the hash value of hashable objects:

```python
print(hash("Sara"))
```

Example output:

```text
8392749237492
```

> The exact value may change between program executions because Python randomizes string hashes for security.

---

## Hashable Keys

Dictionary keys must be **hashable**, meaning their hash value does not change during their lifetime.

### Valid keys

```python
"Ali"      # str
10         # int
3.14       # float
True       # bool
(1, 2)     # tuple
```

### Invalid keys

```python
[1, 2]      # list
{"a": 1}    # dict
```

These objects are mutable and therefore cannot be used as dictionary keys.

Example:

```python
d = {}

d[(1, 2)] = "OK"      # Valid

d[[1, 2]] = "Error"   # TypeError
```

---

## Time Complexity

| Operation | Average Time |
| --------- | ------------ |
| Insert    | O(1)         |
| Lookup    | O(1)         |
| Delete    | O(1)         |

> In the worst case, operations can degrade to **O(n)** due to many hash collisions, although this is uncommon.

---

## Example: Counting Word Frequencies

```python
text = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for word in text:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
```

Output:

```python
{
    "apple": 3,
    "banana": 2,
    "orange": 1
}
```

A shorter version using `get()`:

```python
count = {}

for word in text:
    count[word] = count.get(word, 0) + 1
```

---

# Dictionary vs Set

Both dictionaries and sets use curly braces (`{}`), but their syntax is different.

## Dictionary

Uses **key:value** pairs.

```python
students = {
    "Ali": 20,
    "Sara": 18
}
```

---

## Set

Contains only unique values.

```python
names = {"Ali", "Sara", "Reza"}
```

---

## Empty Dictionary vs Empty Set

An empty pair of braces creates a **dictionary**, not a set.

```python
d = {}
print(type(d))
```

Output:

```text
<class 'dict'>
```

To create an empty set:

```python
s = set()
print(type(s))
```

Output:

```text
<class 'set'>
```

---

## Summary

* `dict` is Python's built-in hash table implementation.
* Data is stored as **key → value** pairs.
* Keys must be **hashable**.
* Average lookup, insertion, and deletion are **O(1)**.
* Dictionaries use `{ key: value }`, while sets use `{ value1, value2 }`.
* `{}` creates an empty dictionary, and `set()` creates an empty set.
