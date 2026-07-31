# Linear Search

## Overview

Linear Search (also known as Sequential Search) is the simplest searching algorithm. It checks each element in a collection one by one until the target value is found or the end of the collection is reached.

Unlike Binary Search, Linear Search does **not** require the data to be sorted.

---

## How It Works

1. Start from the first element.
2. Compare the current element with the target.
3. If they are equal, return its index.
4. Otherwise, move to the next element.
5. Repeat until the target is found or the array ends.

---

## Example

Array:

```text
[12, 5, 18, 9, 30]
```

Target:

```text
9
```

Steps:

```text
12 ❌
5  ❌
18 ❌
9  ✅
```

Result:

```text
Index = 3
```

---

## Algorithm

```text
for each element in the array:
    if element == target:
        return index

return -1
```

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

---

## Space Complexity

```text
O(1)
```

No additional memory is required.

---

## Advantages

- Very simple to implement.
- Works on both sorted and unsorted data.
- No preprocessing is required.

---

## Disadvantages

- Inefficient for large datasets.
- May require checking every element.

---

## Use Cases

Linear Search is commonly used when:

- The dataset is small.
- The data is not sorted.
- Simplicity is preferred over performance.

---

## Python Implementation

```python
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
```

---

## Summary

Linear Search is easy to understand and implement, but its performance decreases as the dataset grows. It is a good choice for small or unsorted collections.