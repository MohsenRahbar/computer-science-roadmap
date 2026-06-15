# 📘 Big-O Notation & Complexity Cheat Sheet (Python)

## 1. What is Big-O?

Big-O describes how the performance of an algorithm changes as input size grows.

It focuses on:

* Time Complexity → how fast code runs
* Space Complexity → how much memory is used

We ignore:

* constants
* small terms
* hardware differences

We only care about **growth rate**

---

## 2. Time Complexity

Time complexity measures the number of operations an algorithm performs.

---

### O(1) — Constant Time

Execution does not depend on input size.

```python
x = arr[0]   # O(1)
```

✔ Fastest complexity
✔ Always same speed

---

### O(n) — Linear Time

Grows directly with input size.

```python
for item in arr:
    print(item)   # O(n)
```

If input doubles → time doubles

---

### O(n²) — Quadratic Time

Nested loops.

```python
for i in arr:
    for j in arr:
        print(i, j)   # O(n²)
```

Very slow for large input.

---

### O(log n) — Logarithmic Time

Input is divided in each step.

Example: Binary Search

```python
while n > 1:
    n = n // 2   # O(log n)
```

Very efficient for large data.

---

## 3. Space Complexity

Space complexity measures extra memory used by algorithm.

---

### O(1) Space

No extra memory used.

```python
x = 10
y = 20
```

---

### O(n) Space

Memory grows with input size.

```python
result = []
for i in arr:
    result.append(i)
```

---

## 4. List Comprehension

Short way to create lists.

```python
squares = [x**2 for x in arr]
```

Equivalent to loop but cleaner.

---

## 5. Slicing

Extract part of a list.

```python
arr[start:end:step]
```

Examples:

```python
arr[2:5]    # from index 2 to 4
arr[:3]     # first 3 elements
arr[::2]    # step of 2
arr[::-1]   # reverse list
```

---

## 6. Mutable vs Immutable

### Mutable (can change)

Example: list

```python
arr[0] = 100
```

### Immutable (cannot change)

Example: string

```python
text = "hello"
# text[0] = "H"  ❌ Error
```

Correct way:

```python
new_text = "H" + text[1:]
```

---

## 7. append() vs extend()

### append()

Adds a single element.

```python
arr = [1, 2, 3]
arr.append([4, 5])
# [1, 2, 3, [4, 5]]
```

---

### extend()

Adds each element separately.

```python
arr = [1, 2, 3]
arr.extend([4, 5])
# [1, 2, 3, 4, 5]
```

---

## 8. Quick Rules for Big-O

### Loops

* 1 loop → O(n)
* nested loops → O(n²)

### Independent loops

```python
for i in n:
for j in n:
```

→ O(n) (not O(n+n))

---

### Logarithmic pattern

If value is divided or multiplied:

* `/2`, `*2` → O(log n)

---

### Final rule

Keep only the **largest complexity term**

Example:

```
O(n + n²) → O(n²)
```

---

## 9. Quick Cheat Table

| Operation            | Complexity |
| -------------------- | ---------- |
| arr[i]               | O(1)       |
| loop                 | O(n)       |
| nested loop          | O(n²)      |
| binary search        | O(log n)   |
| extra list of size n | O(n) space |

