# BFS & DFS

BFS and DFS are two common algorithms for **searching a graph or tree**.

The main difference is simple:

> **BFS explores wide. DFS explores deep.**

---

# 1. BFS — Breadth-First Search

**BFS** explores nodes **level by level**.

Imagine dropping a stone into water:

```text
          Start
            ↓
        ┌───┴───┐
        A       B
       / \     / \
      C   D   E   F
```

BFS visits:

```text
Start
  ↓
A → B
  ↓
C → D → E → F
```

So the order is:

```text
Start → A → B → C → D → E → F
```

### Mental Model

> **BFS asks: "What is nearby?"**

It explores everything close to the current node before going farther.

---

# 2. DFS — Depth-First Search

**DFS** goes as deep as possible before going back.

Using the same tree:

```text
          Start
            ↓
        ┌───┴───┐
        A       B
       / \     / \
      C   D   E   F
```

DFS might visit:

```text
Start → A → C
            ↑
          back
            ↓
          D → B → E → F
```

One possible order:

```text
Start → A → C → D → B → E → F
```

### Mental Model

> **DFS asks: "How far can I go?"**

It follows one path until it cannot continue, then **backtracks**.

---

# 3. The Main Difference

```text
BFS                         DFS

       Start                     Start
      /     \                   /
     A       B                 A
    / \     / \               /
   C   D   E   F             C
                              ↓
                           go deep
```

### BFS

```text
Explore → Explore → Explore
```

### DFS

```text
Explore → Go deeper → Go deeper
                  ↓
               Backtrack
```

---

# 4. BFS Uses a Queue

BFS typically uses a **Queue**.

```text
First In → First Out

A → B → C → D
↑
Remove first
```

Conceptually:

```python
queue = [start]

while queue:
    node = queue.pop(0)
    visit(node)

    for neighbor in node.neighbors:
        queue.append(neighbor)
```

---

# 5. DFS Uses a Stack

DFS typically uses a **Stack**.

```text
Last In → First Out

A
B
C  ← remove first
```

It can also be implemented naturally using **recursion**.

```python
def dfs(node):
    visit(node)

    for neighbor in node.neighbors:
        dfs(neighbor)
```

---

# 6. Finding the Shortest Path

For an **unweighted graph**, BFS has an important property:

> **BFS finds the shortest path in terms of number of edges.**

Example:

```text
Start ── A ── B ── Goal
   \               ↑
    └────── C ─────┘
```

BFS finds:

```text
Start → C → Goal
```

because it has fewer edges.

DFS does **not** guarantee the shortest path.

---

# 7. Time & Space Complexity

For a graph:

```text
V = Number of vertices
E = Number of edges
```

Both generally have:

```text
Time:  O(V + E)
```

Space can also be:

```text
O(V)
```

The practical difference is **how that memory is organized and how the graph is explored**.

---

# 8. When to Use Which?

### Use BFS when:

```text
You need:
✓ Shortest path in an unweighted graph
✓ Level-by-level exploration
✓ Minimum number of steps
✓ Nearest solution
```

Example:

```text
"What's the fewest moves needed
to reach the target?"
```

---

### Use DFS when:

```text
You need:
✓ Deep exploration
✓ Backtracking
✓ Exploring all possible paths
✓ Maze solving
✓ Detecting certain graph structures
```

Example:

```text
"Explore this path completely,
then try another path."
```

---

# 9. The Simplest Mental Model

Remember:

```text
BFS = Wide
DFS = Deep
```

Or:

```text
BFS:
"What's around me?"

DFS:
"What's down this path?"
```

And technically:

```text
BFS → Queue
DFS → Stack / Recursion
```

That's the core idea.
