# Python Type Hinting Cheat Sheet

Type Hinting, introduced in **Python 3.5 (PEP 484)**, allows developers to explicitly declare the expected data types of variables, function parameters, and return values. 

While Python remains a dynamically typed language at runtime, type hints improve **IDE autocompletion**, **static code analysis** (e.g., using `mypy`), and overall **code readability**.

---

## 1. Basic Types

Declare simple, primitive types directly:

```python
# Variables
age: int = 25
price: float = 19.99
is_active: bool = True
name: str = "Alice"

# Functions
def greet(user_name: str) -> str:
    return f"Hello, {user_name}"
```

---

## 2. Collections (Built-in Syntax: Python 3.9+)

In Python 3.9 and newer, use standard built-in container types directly with brackets `[]`:

```python
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95, "Bob": 88}
unique_ids: set[int] = {101, 102, 103}
point: tuple[int, int, str] = (10, 20, "Label")
```

*(Note: For Python 3.8 and older, these were imported from `typing`: `List[str]`, `Dict[str, int]`, etc.)*

---

## 3. Union & Optional Types

When a value can hold multiple data types or might be `None`.

### Union Types (Python 3.10+)
Use the `|` operator to combine types:

```python
# Can be an integer or a float
val: int | float = 3.14

def process_id(user_id: int | str) -> str:
    return f"User_{user_id}"
```

### Optional Types (Value or None)
Expressing that a value can be of a specific type or `None`:

```python
# Modern syntax (Python 3.10+)
data: str | None = None

# Traditional syntax (typing module)
from typing import Optional
legacy_data: Optional[str] = None
```

---

## 4. Special & Advanced Types

Import these from the standard `typing` module when needed:

### Any
Disables type checking for a variable (use sparingly).
```python
from typing import Any

data: Any = "Could be anything: string, int, object"
```

### Callable
For functions passed as arguments or variables.
```python
from typing import Callable

# Syntax: Callable[[ParamTypes], ReturnType]
def execute(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)
```

### TypeAlias
For creating custom, reusable type shortcuts.
```python
from typing import TypeAlias

# Create readable type aliases
Coordinate: TypeAlias = tuple[float, float]
UserDict: TypeAlias = dict[str, str | int]

def get_location() -> Coordinate:
    return (35.6895, 139.6917)
```

---

## 5. Clean Code Best Practices for Type Hints

1. **Be Selective:** Annotate public function signatures, class methods, and business logic. Avoid over-annotating local variables inside short functions.
2. **Keep It Simple:** If a type annotation becomes too complex, create a `TypeAlias` or encapsulate the data inside a `dataclass` or `Pydantic` model.
3. **Skip for Simple `main()`:** As noted earlier, entry-point functions like `main()` without parameters or return values do not need explicit type hints.
