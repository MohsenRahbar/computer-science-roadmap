# Clean Code Cheat Sheet & Study Guide
*Based on Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin (Uncle Bob)*

---

## 1. Meaningful Names

### 1.1 Intention-Revealing Names
Names should explicitly convey why a variable, function, or class exists, what it does, and how it is used. If a name requires a comment to explain itself, it has failed its purpose.

* **Incorrect:** `int d; // elapsed time in days`
* **Correct:** `int elapsedTimeInDays;`

### 1.2 Avoid Disinformation
Do not use names that convey false meanings or conflict with programming terms.
* Avoid using container names like `accountList` unless the variable is actually a `List`.
* Avoid visually confusing identifiers (e.g., using lowercase `l` or uppercase `O` as variable names).

### 1.3 Make Meaningful Distinctions
Avoid subtle variations or noise words just to satisfy the compiler.
* **Noise Words:** Avoid pairs like `a1` / `a2`, or generic additions like `Data`, `Info`, `Object` (e.g., `UserData` vs. `UserInfo`).
* Distinct concepts must have distinct names.

### 1.4 Use Pronounceable and Searchable Names
* **Pronounceable:** Code is read and discussed verbally. Avoid obscure abbreviations like `modymdhms`.
* **Searchable:** Avoid single-letter variables and "magic numbers." Named constants (e.g., `MAX_CLASSES_PER_STUDENT`) are vastly superior to hardcoded numbers (e.g., `7`) because they are easily searchable across a codebase.

### 1.5 Avoid Encoding Prefixes
Modern IDEs eliminate the need for type encoding or scope prefixes.
* Do not use Hungarian Notation (`strName`, `iCount`).
* Do not prefix member variables with `m_` (e.g., use `name` instead of `m_name`).

### 1.6 Naming Conventions for Classes and Methods
* **Class & Object Names:** Must be a **noun** or **noun phrase** (e.g., `Customer`, `WikiPage`, `Account`, `AddressParser`). Avoid vague suffix managers like `Manager`, `Processor`, `Data`, or `Info`.
* **Method & Function Names:** Must be a **verb** or **verb phrase** (e.g., `postPayment`, `deletePage`, `save`).
  * Follow JavaBeans standards for accessors/mutators: `getName()`, `setName()`, `isCustomerActive()`.
  * Use **Static Factory Methods** with descriptive names for overloaded constructors:
    * *Incorrect:* `ComplexNumber point = new ComplexNumber(23.0);`
    * *Correct:* `ComplexNumber point = ComplexNumber.fromRealNumber(23.0);`

### 1.7 Don't Be Cute!
Prioritize clarity over humor, slang, or colloquialisms.
* Avoid whimsical names like `kill()` or `outmaneuver()` when you mean `delete()`.
* Avoid internal jokes like `holyHandGrenade()` when you mean `resetSystem()`.
* **Golden Rule:** *"Say what you mean. Mean what you say."*

---

## 2. Formatting & Spacing

### 2.1 Vertical Openness
Use blank lines to separate distinct concepts and logical steps, similar to paragraphs in a well-structured text.

### 2.2 Vertical Density
Keep tightly related lines of code visually close to each other. Lines of code that depend on one another should remain in close vertical proximity.

### 2.3 Horizontal Openness & Density
Use horizontal spacing to associate strongly related items and disassociate weakly related ones:
* Put spaces around assignment and arithmetic operators: `double b = a + c;`
* Add a space after commas in function parameters: `myFunction(a, b, c);`

### 2.4 Indentation Hierarchy
Indentations represent the structural hierarchy (classes, methods, control blocks). Never skip indentation for short statements or single-line `if` blocks.

### 2.5 The Newspaper Metaphor
A source file should read like a newspaper article:
* **Top:** High-level concepts, summaries, and main algorithms.
* **Bottom:** Low-level details and helper functions.

---

## 3. Writing Clean Functions

### 3.1 Keep Them Small!
* Functions should be extremely short—ideally between 3 to 5 lines, and rarely exceeding 20 lines.
* Keep indentation levels minimal (1 or 2 levels maximum). Avoid deeply nested `if` conditions or loops inside a single function.

### 3.2 Do One Thing (Single Responsibility)
> **Rule:** *Functions should do one thing. They should do it well. They should do it only.*

* If you can extract another function from a given function with a name that is not merely a restatement of its implementation, the original function is doing more than one thing.

### 3.3 Function Arguments
The ideal number of arguments for a function is **zero (Niladic)**.

* **0 Arguments (Niladic):** Ideal; extremely simple to test and understand.
* **1 Argument (Monadic):** Great (e.g., `boolean fileExists("MyFile")`).
* **2 Arguments (Dyadic):** Acceptable, but strive to minimize (e.g., `Point p = new Point(0, 0)` makes sense due to Cartesian axes).
* **3 Arguments (Triadic):** Avoid where possible; significantly harder to test and comprehend.
* **>3 Arguments (Polyadic):** Requires refactoring into separate parameter objects.

#### Avoid Flag Arguments (Boolean Arguments)
Passing a boolean flag (e.g., `render(boolean isSuite)`) explicitly signals that the function performs more than one thing (one path for `true`, another for `false`). Split the function into two distinct methods instead (e.g., `renderForSuite()` and `renderForSingleTest()`).

### 3.4 Command Query Separation (CQS)
A function should either **change the state of an object** OR **return information about that object**, but **never both**.

* *Incorrect:* `if (set("username", "unclebob")) ...` (Unclear if it checks a setting or sets a value)
* *Correct:*
  ```java
  if (attributeExists("username")) {
      setAttribute("username", "unclebob");
  }
  ```

### 3.5 Have No Side Effects
Functions must not make hidden state changes that are not explicitly implied by their name (e.g., modifying global variables or changing session parameters unexpectedly).

* *Example:* A method named `checkPassword(user, password)` should not implicitly initialize a session upon a successful check.

### 3.6 Don't Repeat Yourself (DRY)
Code duplication is the root of many software defects. Whenever identical logic is duplicated across multiple functions, abstract it into a reusable helper function.
