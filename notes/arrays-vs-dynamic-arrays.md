### Difference between Array and Dynamic Array

#### 1) Array (Static Array)

* Size is fixed at creation time and cannot change.
* Data is stored in a contiguous block of memory.
* O(1) access by index.
* If the array is too small or too large, a new array must be created and data copied.

**Key property:** fixed size

---

#### 2) Dynamic Array

* Size can grow automatically.
* When capacity is full, a larger block of memory is allocated (usually 2x), and elements are copied over.
* Still stored in contiguous memory.
* Index access remains O(1).

**Key property:** automatic resizing with amortized cost

---

### Why Python List is a Dynamic Array

In CPython, `list` is implemented as a dynamic array:

* It stores an internal array of pointers to objects.
* When capacity is exceeded:

  * A larger memory block is allocated
  * All existing elements are copied
* Growth follows a geometric strategy (roughly 1.125x to 2x depending on version) to reduce the number of resizes.

---

### Advantages and Disadvantages of Dynamic Arrays (like Python list)

#### Advantages

* Fast index access: O(1)
* Cache-friendly due to contiguous memory layout
* `append` is amortized O(1)
* Good general-purpose data structure

---

#### Disadvantages

* Insert/delete in the middle: O(n)
* Resizing is expensive (full copy of elements)
* Can waste memory (capacity > actual size)
* Not optimal when size is known and fixed or when frequent middle operations are needed

---

### Practical Summary

* Use a list when:

  * You do many appends
  * You need fast random access
* Avoid it when:

  * You frequently insert/delete in the middle (use alternatives like linked lists or deque)
  * Memory usage is highly constrained

