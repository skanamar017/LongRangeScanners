# Task 1: Variable Declaration and Initialization (Python)

## 🎯 Learning Objectives
- Understand Python's dynamic typing system
- Learn variable assignment and initialization patterns
- Practice with Python's built-in data types
- Understand Python's multiple assignment feature
- Explore type conversion in Python

## 📋 Instructions

1. Open the file `src/exercises/task01/variable_exercises.py`
2. Implement each method according to the specifications in the docstrings
3. Remove the `raise NotImplementedError(...)` line and add your implementation
4. Run the tests to verify your solutions

## 🧪 Running Tests

```bash
# Run only Task 1 tests
./run-tests.sh 1

# Or use pytest directly
python3 -m pytest tests/task01/ -v

# Or use unittest
python3 -m unittest tests.task01.test_variable_exercises -v

# Run all tests (if you want to see the full picture)
./run-tests.sh
```

## 📝 What You'll Learn

### Python Data Types
- `int` - Integer numbers (unlimited precision)
- `float` - Floating-point numbers
- `bool` - Boolean values (True/False)
- `str` - Text strings
- `list` - Ordered collections of items

### Variable Assignment Patterns
```python
# Simple assignment
age = 25
name = "Alice"

# Multiple assignment (tuple unpacking)
x, y, z = 1, 2, 3

# Dynamic typing - same variable, different types
variable = 42        # integer
variable = "Hello"   # now it's a string
```

### Python Constants
```python
# Python doesn't have true constants, use naming convention
MAX_ATTEMPTS = 3
PI = 3.14159
```

### Type Conversion
```python
# Convert between types
number_str = "42"
number_int = int(number_str)  # 42

float_num = 3.14
int_num = int(float_num)      # 3 (truncated)
```

## ✅ Success Criteria

Your implementation is correct when:
- All tests pass (10/10 tests should be green)
- You've used appropriate Python variable assignment
- You understand Python's dynamic typing
- You can perform type conversions

## 💡 Hints

1. **initialize_integer()**: Simply assign 42 to a variable and return it
2. **initialize_float()**: Use decimal notation: `3.14159`
3. **initialize_boolean()**: Return the literal value `True`
4. **initialize_string()**: Use double or single quotes: `"Hello, World!"`
5. **initialize_list()**: Use square brackets: `[1, 2, 3, 4, 5]`
6. **variable_reassignment()**: Start with 10, add 5, multiply by 2
7. **work_with_constants()**: Use UPPER_CASE naming convention
8. **type_conversion()**: Use `int()` function to convert float to integer
9. **multiple_assignment()**: Use tuple unpacking: `a, b, c = 1, 2, 3`
10. **dynamic_typing()**: Reassign the same variable to different types

## 🎓 Key Python Concepts to Remember

- **Dynamic Typing** - Variables don't have fixed types
- **Duck Typing** - "If it walks like a duck and quacks like a duck, it's a duck"
- **Multiple Assignment** - Assign multiple variables in one line
- **Type Conversion** - Use built-in functions like `int()`, `float()`, `str()`
- **Naming Conventions** - snake_case for variables, UPPER_CASE for constants
- **No Semicolons** - Line breaks end statements (unlike Java)

## 🔍 Python vs Java Differences

| Aspect | Java | Python |
|--------|------|--------|
| Type Declaration | `int age = 25;` | `age = 25` |
| Constants | `final int MAX = 100;` | `MAX = 100  # convention` |
| String Literals | `"Hello"` | `"Hello"` or `'Hello'` |
| Multiple Assignment | Not directly supported | `a, b = 1, 2` |
| Type Conversion | `(int) 3.14` | `int(3.14)` |
