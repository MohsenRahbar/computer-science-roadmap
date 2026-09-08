# State Space

## 1. What is a State?

A **state** is a snapshot of everything that matters about a system at a specific moment.

Think of it as:

> **"Where am I right now?"**

For example, in a chess game:

```text
State = Position of all pieces
```

In a robot:

```text
State = Position + Speed + Direction
```

In a game:

```text
State = Player position + Health + Score + Inventory
```

---

## 2. What is State Space?

The **State Space** is the set of **all possible states** that a system can be in.

Imagine a game:

```text
        State Space
   ┌───────────────────┐
   │  S1  S2  S3  S4   │
   │  S5  S6  S7  S8   │
   │  S9  S10 S11 S12  │
   └───────────────────┘
```

Each point is a possible **state**.

So:

```text
State      = One situation
State Space = All possible situations
```

---

## 3. States Can Change

A system moves from one state to another through an **action**.

```text
State A
   │
 Action
   ↓
State B
   │
 Action
   ↓
State C
```

For example:

```text
Robot at (0,0)
      ↓
Move Right
      ↓
Robot at (1,0)
      ↓
Move Up
      ↓
Robot at (1,1)
```

The robot is moving through the **State Space**.

---

## 4. State Space as a Map

A useful way to think about State Space is as a **map**.

```text
        S2 ─── S3 ─── S4
        │           │
        │           │
        S1 ─── S5 ───S6
```

* **Nodes** → States
* **Edges** → Actions / Transitions

The Agent's job can then be viewed as:

> **Find a path from the current state to a desired state.**

```text
Start
  ↓
 S1 → S2 → S3 → S4
                  ↓
                Goal
```

---

## 5. State Space in AI Agents

This concept becomes important when building Agents.

Suppose an Agent has the goal:

```text
"Book a flight."
```

Its states might look like:

```text
Start
  ↓
Searching
  ↓
Flights Found
  ↓
Flight Selected
  ↓
Payment Pending
  ↓
Booked
```

The Agent moves through these states by taking actions.

```text
State → Action → New State
```

---

## 6. The Core Idea

Remember this simple model:

```text
       ┌─────────────┐
       │ Current     │
       │   State     │
       └──────┬──────┘
              ↓
           Action
              ↓
       ┌─────────────┐
       │    New      │
       │   State     │
       └─────────────┘
```

And:

```text
All possible states
        ↓
    State Space
```

### In one sentence:

> **State Space is the universe of possible situations a system can be in, and actions move the system between those situations.**
