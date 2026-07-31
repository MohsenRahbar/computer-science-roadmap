# Binary Search

## Overview

Binary Search is an efficient searching algorithm that repeatedly divides the search space in half until the target element is found.

Unlike Linear Search, Binary Search only works on **sorted** collections.

---

## Prerequisites

Before using Binary Search:

- The array must be sorted.
- Random access to elements should be available (such as an array or list).

Example:

```text
[2, 5, 8, 12, 17, 23, 30]
```

---

## How It Works

1. Find the middle element.
2. Compare the middle element with the target.
3. If they are equal, return the index.
4. If the target is smaller, continue searching in the left half.
5. If the target is larger, continue searching in the right half.
6. Repeat until the target is found or the search space becomes empty.

---

## Example

Array:

```text
[2, 5, 8, 12, 17, 23, 30]
```

Target:

```text
17
```

Iteration 1

```text
Left = 0
Right = 6
Middle = 3

12 < 17

Search Right Half
```

Iteration 2

```text
Left = 4
Right = 6
Middle = 5

23 > 17

Search Left Half
```

Iteration 3

```text
Left = 4
Right = 4
Middle = 4

17 == Target ✅
```

Result:

```text
Index = 4
```

---

## Algorithm

```text
while left <= right:

    middle = (left + right) // 2

    if middle == target:
        return index

    if target < middle:
        search left half

    else:
        search right half

return -1
```

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

---

## Space Complexity

### Iterative

```text
O(1)
```

### Recursive

```text
O(log n)
```

The recursive version uses the call stack.

---

## Advantages

- Extremely fast for large datasets.
- Reduces the search space by half on every iteration.
- Much more efficient than Linear Search for sorted data.

---

## Disadvantages

- Requires sorted data.
- Less suitable when the collection changes frequently.
- Cannot be efficiently applied to data structures without random access (e.g., linked lists).

---

## Use Cases

Binary Search is commonly used when:

- The data is sorted.
- Fast searching is required.
- The dataset is large.
- Search operations are performed frequently.

---

## Python Implementation

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1
```

---

## Comparison

| Feature | Linear Search | Binary Search |
|----------|---------------|---------------|
| Sorted Data Required | No | Yes |
| Best Time | O(1) | O(1) |
| Average Time | O(n) | O(log n) |
| Worst Time | O(n) | O(log n) |
| Space (Iterative) | O(1) | O(1) |

---

## Summary

Binary Search is one of the most efficient searching algorithms for sorted collections. By repeatedly dividing the search space into two halves, it significantly reduces the number of comparisons compared to Linear Search, making it the preferred choice for large sorted datasets.