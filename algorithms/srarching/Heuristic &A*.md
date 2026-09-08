# Heuristic

## 1. What is a Heuristic?

A **heuristic** is a rule or estimate that helps an algorithm **make a good decision faster**.

Instead of checking every possible option, we use an educated guess to decide:

> **"Which option looks more promising?"**

```text
Heuristic = Useful estimate
```

---

# 2. Simple Example

Imagine you are looking for a destination in a city.

You don't check every possible road.

Instead, you might use:

```text
Distance to destination
        ↓
Which road looks closer?
```

The distance is being used as a **heuristic**.

It doesn't necessarily tell us the exact best path.

It simply gives us a useful estimate.

---

# 3. Heuristics in Search

Suppose we want to reach:

```text
Start ─── ? ─── ? ─── Goal
```

There may be many possible paths.

A heuristic estimates:

```text
"How far am I from the Goal?"
```

This is commonly represented as:

```text
h(n)
```

Where:

```text
h(n) = estimated cost from node n to the goal
```

For example:

```text
Current Node
     ↓
   h(n) = 7
```

This means:

> "I estimate that the goal is 7 units away."

---

# 4. Heuristic ≠ Exact Answer

A heuristic is an **estimate**, not necessarily the actual value.

For example:

```text
Actual distance = 10 km
Heuristic       = 7 km
```

The heuristic is not exact, but it can still be useful.

The goal is:

```text
Good estimate
     ↓
Better decisions
     ↓
Less unnecessary search
```

---

# 5. A* Search

One of the most famous search algorithms that uses a heuristic is **A***.

A* combines:

```text
Cost so far
     +
Estimated cost remaining
```

It uses two important values:

```text
g(n) = actual cost from Start → n

h(n) = estimated cost from n → Goal
```

Then:

```text
f(n) = g(n) + h(n)
```

The algorithm generally prioritizes the node with the **lowest `f(n)`**.

---

# 6. Example of A*

Imagine:

```text
Start
  │
  A
 / \
B   C
 \   \
  D   Goal
```

Suppose:

```text
Node B:
g(B) = 4
h(B) = 6

f(B) = 4 + 6
     = 10
```

And:

```text
Node C:
g(C) = 3
h(C) = 4

f(C) = 3 + 4
     = 7
```

A* prefers `C` because:

```text
f(C) < f(B)
```

So instead of blindly exploring nodes, A* uses the heuristic to **guide the search**.

---

# 7. Why Not Just Use the Heuristic?

You might ask:

> "Why don't we just choose the node with the smallest `h(n)`?"

Because `h(n)` only tells us about the **estimated remaining cost**.

It ignores how much we have already spent.

For example:

```text
Path A:
g = 2
h = 10
f = 12

Path B:
g = 8
h = 3
f = 11
```

A* considers both:

```text
g(n) + h(n)
```

This balances:

```text
What I've already spent
        +
What I expect to spend
```

---

# 8. Heuristic and A*

The relationship is:

```text
Heuristic
    ↓
   h(n)
    ↓
   A*
    ↓
f(n) = g(n) + h(n)
```

So:

> **A heuristic is a technique/estimate, while A* is a search algorithm that uses a heuristic.**

They are not the same thing.

---

# 9. Good Heuristic

A good heuristic should be:

```text
Useful
  +
Fast to calculate
  +
Reasonably accurate
```

For example, when finding a path on a map:

```text
Straight-line distance
```

can be a useful heuristic.

If two cities are geographically close, their straight-line distance can give the algorithm an idea of how promising a route might be.

---

# 10. BFS vs DFS vs A*

These algorithms approach search differently.

### BFS

```text
Search level by level

Start
 ↓
A → B
 ↓
C → D → E
```

BFS doesn't use a heuristic.

---

### DFS

```text
Go as deep as possible

Start
  ↓
  A
  ↓
  C
  ↓
  ...
```

DFS doesn't normally use a heuristic either.

---

### A*

```text
Use cost + estimated distance

Start
  ↓
g(n) + h(n)
  ↓
Choose promising node
```

---

# 11. Quick Comparison

| Algorithm     | Main Idea                     | Uses Heuristic? | Typical Data Structure | Shortest Path?                |
| ------------- | ----------------------------- | --------------: | ---------------------- | ----------------------------- |
| **BFS**       | Explore level by level        |               ❌ | Queue                  | ✅ Unweighted graph            |
| **DFS**       | Go as deep as possible        |               ❌ | Stack / Recursion      | ❌                             |
| **A***        | Use cost + estimated distance |               ✅ | Priority Queue         | ✅ If conditions are satisfied |
| **Heuristic** | Estimate what looks promising |               — | —                      | —                             |

---

# 12. The Big Picture

You can think about them like this:

```text
                 Search
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
       BFS        DFS        A*
        │          │          │
      Wide        Deep      Guided
                             Search
                                │
                                ↓
                           Heuristic
```

Or even simpler:

```text
BFS → "Search everything nearby."

DFS → "Go as deep as possible."

Heuristic → "Which direction looks promising?"

A* → "What have I spent + what do I expect to spend?"
```

### Final Mental Model

```text
BFS
↓
No guessing
Explore level by level


DFS
↓
No guessing
Explore deeply


Heuristic
↓
Make an estimate
"How promising is this?"


A*
↓
Use the estimate + actual cost
"What's the cheapest-looking path so far?"
```

> **Heuristic is the guidance. A* is the algorithm that uses that guidance to search more intelligently.**
